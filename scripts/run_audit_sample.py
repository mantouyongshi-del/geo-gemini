import sys
import asyncio

# 添加 backend 路径
sys.path.insert(0, "/Users/dw/Desktop/讯灵/backend")

from app.core.database import SessionLocal
from app.models.company import Company
from app.models.keyword import Keyword
from app.services.audit_service import AuditService

async def main():
    db = SessionLocal()
    company = db.query(Company).first()
    if not company:
        print("Please run init_demo_data.py first!")
        return

    keyword = db.query(Keyword).filter(Keyword.company_id == company.id).first()
    print(f"Testing Audit for Company: {company.name}")
    print(f"Target Keyword: {keyword.keyword} (Subject: {keyword.subject})")

    platforms = ["doubao", "deepseek", "tongyi"]
    for p in platforms:
        print(f"\n--- Testing on Platform [{p}] ---")
        rec = await AuditService.run_single_audit(company.id, keyword.id, p, False, db)
        print(f"Result -> Recommended: {rec.is_recommended}, Rank: {rec.rank}, Model: {rec.model_name}")
        snap = rec.snapshot
        print(f"Snapshot Content Preview: {snap.full_content[:150]}...")
        print(f"Matched Entities: {snap.matched_entities}")
    db.close()
    print("\nSample Audit Completed Successfully!")

if __name__ == "__main__":
    asyncio.run(main())
