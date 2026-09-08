import time
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base

class Keyword(Base):
    __tablename__ = "keywords"

    id = Column(Integer, primary_key=True, index=True)
    company_id = Column(Integer, ForeignKey("companies.id", ondelete="CASCADE"), nullable=False, index=True)
    
    # 场景类型: 1: 品牌场景, 2: 搜索词场景, 3: 问答词场景, 4: 意图场景
    task_type = Column(Integer, default=2, index=True, comment="1:品牌, 2:搜索, 3:问答, 4:意图")
    
    # 主题词与提示词
    subject = Column(String(100), nullable=False, index=True, comment="核心主题词(如: 少儿编程, 嘉兴机器人竞赛)")
    keyword = Column(String(255), nullable=False, index=True, comment="用户实际输入提问词(如: 嘉兴少儿编程哪家强)")
    
    created_at = Column(Integer, default=lambda: int(time.time()))

    # 关联
    company = relationship("Company", back_populates="keywords")
    audit_records = relationship("AuditRecord", back_populates="keyword_rel", cascade="all, delete-orphan")
