from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship
from app.core.database import Base

class DailyStat(Base):
    __tablename__ = "daily_stats"

    id = Column(Integer, primary_key=True, index=True)
    company_id = Column(Integer, ForeignKey("companies.id", ondelete="CASCADE"), nullable=False, index=True)
    stat_date = Column(String(20), nullable=False, index=True, comment="日期: YYYY-MM-DD")
    platform = Column(String(50), nullable=True, comment="大模型名称(为空时表示汇总)")
    
    total_recommendations = Column(Integer, default=0, comment="当日累计推荐量")
    daily_increment = Column(Integer, default=0, comment="当日净增推荐量")

    __table_args__ = (
        UniqueConstraint("company_id", "stat_date", "platform", name="uix_company_date_platform"),
    )

    company = relationship("Company", back_populates="daily_stats")
