import json
import time
from typing import List, Optional, Dict
from sqlalchemy.orm import Session
from app.models.company import Company
from app.models.keyword import Keyword
from app.models.audit import AuditRecord, MatchSnapshot
from app.providers.llm_gateway import LLMGateway

class AuditService:
    @staticmethod
    async def run_single_audit(
        company_id: int,
        keyword_id: int,
        platform: str,
        is_mobile: bool = False,
        cached_citations: Optional[List[Dict[str, str]]] = None,
        db: Session = None
    ) -> AuditRecord:
        company = db.query(Company).filter(Company.id == company_id).first()
        if not company:
            raise ValueError("Company not found")

        keyword_obj = db.query(Keyword).filter(Keyword.id == keyword_id).first()
        if not keyword_obj:
            raise ValueError("Keyword not found")

        aliases = company.get_alias_list()
        
        # 调用基于全网实时探针的大模型网关
        resp = await LLMGateway.query(
            platform=platform,
            prompt=keyword_obj.keyword,
            brand_name=company.name,
            brand_aliases=aliases,
            industry=company.industry or "",
            is_mobile=is_mobile,
            cached_citations=cached_citations
        )

        # 检查是否命中品牌词及计算命中频次
        matched = []
        mention_count = 0
        for alias in aliases:
            count = resp.content.count(alias)
            if count > 0:
                matched.append(alias)
                mention_count += count

        is_recommended = len(matched) > 0
        rank = 1 if is_recommended else 99

        # 创建或更新审计记录
        record = AuditRecord(
            company_id=company.id,
            keyword_id=keyword_obj.id,
            platform=platform,
            is_mobile=is_mobile,
            model_name=resp.model_name,
            task_type=keyword_obj.task_type,
            is_recommended=is_recommended,
            rank=rank,
            mention_count=mention_count,
            create_dt=int(time.time()),
            mtime=int(time.time())
        )
        db.add(record)
        db.flush()

        # 创建问答快照
        snapshot = MatchSnapshot(
            record_id=record.id,
            query_prompt=keyword_obj.keyword,
            full_content=resp.content,
            citations_json=json.dumps(resp.citations, ensure_ascii=False),
            matched_entities="|".join(matched) if matched else None
        )
        db.add(snapshot)
        db.commit()
        db.refresh(record)
        return record
