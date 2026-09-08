import sys
import os
import asyncio
import argparse

sys.path.insert(0, "/Users/dw/Desktop/讯灵/backend")

from app.core.database import SessionLocal
from app.api.v1.endpoints.company import quick_audit_brand, QuickAuditRequest

async def main():
    parser = argparse.ArgumentParser(description="一键针对任意新品牌启动 GEO 搜索诊断与大模型巡检")
    parser.add_argument("name", help="公司全称或品牌主名 (例如: 蔚来汽车 / 元气森林 / 霸王茶姬)")
    parser.add_argument("--industry", default="科技与创新消费", help="所属行业领域")
    parser.add_argument("--aliases", default="", help="品牌实体别名，以逗号分隔")
    parser.add_argument("--keywords", default="", help="自定义监控提示词，以分号或逗号分隔")
    
    args = parser.parse_args()
    
    custom_kws = [k.strip() for k in args.keywords.replace(";", ",").split(",") if k.strip()]
    
    print(f"🚀 正在为品牌【{args.name}】创建档案并调度各大模型巡检...")
    db = SessionLocal()
    try:
        req = QuickAuditRequest(
            name=args.name,
            short_name=args.name.split("（")[0].replace("有限公司", "").strip(),
            industry=args.industry,
            brand_aliases=args.aliases or args.name,
            custom_keywords=custom_kws if custom_kws else None
        )
        res = await quick_audit_brand(req, db)
        print("\n========================================================")
        print("🎉 品牌 GEO 巡检与报表生成完成！")
        print(f"品牌主体: {res['name']}")
        print(f"专属分享码: {res['share_token']}")
        print(f"👉 查看报告链接: {res['report_url']}")
        print("========================================================\n")
    finally:
        db.close()

if __name__ == "__main__":
    asyncio.run(main())
