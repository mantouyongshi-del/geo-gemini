import time
from sqlalchemy import Column, Integer, String, Text, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base

class AuditRecord(Base):
    __tablename__ = "audit_records"

    id = Column(Integer, primary_key=True, index=True)
    company_id = Column(Integer, ForeignKey("companies.id", ondelete="CASCADE"), nullable=False, index=True)
    keyword_id = Column(Integer, ForeignKey("keywords.id", ondelete="CASCADE"), nullable=False, index=True)
    
    # 平台: doubao, deepseek, tongyi, yuanbao, baidu, nami, kuake, uc, wechat, douyin, rednote
    platform = Column(String(50), nullable=False, index=True)
    is_mobile = Column(Boolean, default=False, comment="是否为移动端环境")
    model_name = Column(String(100), nullable=True, comment="调用模型内核代号")
    
    # 场景类型(冗余字段以支持高速过滤)
    task_type = Column(Integer, default=2, index=True)
    
    # 监控结果
    is_recommended = Column(Boolean, default=True, comment="是否命中推荐")
    rank = Column(Integer, default=1, comment="推荐位次排名")
    mention_count = Column(Integer, default=1, comment="品牌命中提及次数")
    
    # 时间戳
    create_dt = Column(Integer, default=lambda: int(time.time()), index=True)
    mtime = Column(Integer, default=lambda: int(time.time()), onupdate=lambda: int(time.time()), index=True)

    # 关联
    company = relationship("Company", back_populates="audit_records")
    keyword_rel = relationship("Keyword", back_populates="audit_records")
    snapshot = relationship("MatchSnapshot", back_populates="record", uselist=False, cascade="all, delete-orphan")


class MatchSnapshot(Base):
    __tablename__ = "match_snapshots"

    id = Column(Integer, primary_key=True, index=True)
    record_id = Column(Integer, ForeignKey("audit_records.id", ondelete="CASCADE"), nullable=False, unique=True, index=True)
    
    query_prompt = Column(String(500), nullable=False, comment="向大模型实际提问的提示词")
    full_content = Column(Text, nullable=False, comment="大模型返回的完整生成回答内容")
    
    # JSON 格式存储引文溯源 RAG 搜索来源
    # 格式: [{"title": "...", "url": "...", "site_name": "...", "summary": "..."}]
    citations_json = Column(Text, nullable=True, comment="大模型引用的联网搜索源数据")
    
    # 命中的实体词 (如: 嘉兴市莱沃科技培训有限公司|科莱沃机器人)
    matched_entities = Column(String(500), nullable=True)

    # 关联
    record = relationship("AuditRecord", back_populates="snapshot")
