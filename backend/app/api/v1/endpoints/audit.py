from fastapi import APIRouter, Depends, HTTPException, BackgroundTasks
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import List, Optional
from app.core.database import get_db, SessionLocal
from app.models.keyword import Keyword
from app.services.audit_service import AuditService

router = APIRouter()

class SingleAuditRequest(BaseModel):
    company_id: int
    keyword_id: int
    platform: str = "doubao"
    is_mobile: bool = False

class BatchAuditRequest(BaseModel):
    company_id: int
    platforms: List[str] = ["doubao", "deepseek", "tongyi", "yuanbao", "baidu", "nami"]
    limit_keywords: int = 20

@router.post("/run-single")
async def run_single_audit(payload: SingleAuditRequest, db: Session = Depends(get_db)):
    try:
        record = await AuditService.run_single_audit(
            company_id=payload.company_id,
            keyword_id=payload.keyword_id,
            platform=payload.platform,
            is_mobile=payload.is_mobile,
            db=db
        )
        return {
            "success": True,
            "record_id": record.id,
            "is_recommended": record.is_recommended,
            "rank": record.rank,
            "mention_count": record.mention_count
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

async def _do_batch_audit(company_id: int, platforms: List[str], limit: int):
    """后台异步批处理任务，创建独立 SessionLocal 避免请求结束后 session 已被 close"""
    db = SessionLocal()
    try:
        keywords = db.query(Keyword).filter(Keyword.company_id == company_id).limit(limit).all()
        for kw in keywords:
            for p in platforms:
                try:
                    await AuditService.run_single_audit(company_id, kw.id, p, False, db)
                    await AuditService.run_single_audit(company_id, kw.id, p, True, db)
                except Exception as e:
                    print(f"[BatchAudit] Error on kw {kw.id} platform {p}: {e}")
    finally:
        db.close()

@router.post("/run-batch")
def trigger_batch_audit(
    payload: BatchAuditRequest, 
    background_tasks: BackgroundTasks
):
    background_tasks.add_task(_do_batch_audit, payload.company_id, payload.platforms, payload.limit_keywords)
    return {"success": True, "message": "Batch audit task scheduled in background"}
