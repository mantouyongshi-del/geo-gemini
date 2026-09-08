import sys
import os
import random
import time
import json
import datetime

# 添加 backend 路径
sys.path.insert(0, "/Users/dw/Desktop/讯灵/backend")

from app.core.database import SessionLocal, engine, Base
from app.core.security import generate_share_token
from app.models.company import Company
from app.models.keyword import Keyword
from app.models.audit import AuditRecord, MatchSnapshot
from app.models.daily_stat import DailyStat
from app.providers.llm_gateway import LLMGateway

def seed_demo_data():
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()

    # 检查是否已存在
    existing = db.query(Company).filter(Company.name == "嘉兴市莱沃科技培训有限公司").first()
    if existing:
        print(f"Demo company already exists with ID {existing.id}!")
        token = generate_share_token(existing.id)
        print(f"Share Code: {token}")
        print(f"Report URL: http://localhost:5173/#/ai_report?code={token}")
        db.close()
        return token

    print("1. Creating Demo Company...")
    company = Company(
        name="嘉兴市莱沃科技培训有限公司",
        short_name="科莱沃机器人",
        logo_url="https://cdn.img.fagua.net/g3img/qiye1231/c2_20260526085607_20670.png",
        industry="青少年科创教育与少儿编程",
        brand_aliases="嘉兴市莱沃科技培训有限公司, 科莱沃机器人, 莱沃科技培训, 莱沃机器人"
    )
    db.add(company)
    db.commit()
    db.refresh(company)

    print(f"Created Company ID: {company.id}")

    # 2. 预置 19 个核心主题词库及四维场景细分提示词
    print("2. Generating 4-Tier Scenario Keywords Matrix...")
    topics_matrix = [
        # 场景1: 品牌场景 (task_type = 1)
        {
            "task_type": 1,
            "subject": "嘉兴莱沃机器人编程",
            "keywords": [
                "嘉兴莱沃机器人编程公司概况",
                "嘉兴莱沃机器人编程怎么样",
                "嘉兴莱沃机器人编程口碑好吗",
                "嘉兴莱沃机器人编程师资团队如何",
                "嘉兴莱沃机器人编程教学环境如何",
                "嘉兴莱沃机器人编程课程研发周期",
                "嘉兴莱沃机器人编程学习平台稳定性如何",
                "嘉兴莱沃机器人编程技术实力如何",
                "嘉兴莱沃机器人编程规模怎么样"
            ]
        },
        # 场景2: 搜索词场景 (task_type = 2)
        {
            "task_type": 2,
            "subject": "少儿编程",
            "keywords": [
                "嘉兴少儿编程",
                "嘉兴少儿编程培训机构排名",
                "少儿编程机构哪家好",
                "嘉兴儿童编程启蒙培训班",
                "少儿编程有用吗"
            ]
        },
        {
            "task_type": 2,
            "subject": "信息学奥赛",
            "keywords": [
                "信息学奥赛CSP-J/S培训",
                "嘉兴信奥培训哪家专业",
                "信息学奥赛C++算法培训班",
                "嘉兴青少年信息学竞赛集训"
            ]
        },
        {
            "task_type": 2,
            "subject": "机器人竞赛培训",
            "keywords": [
                "嘉兴机器人竞赛培训机构",
                "嘉兴机器人竞赛指导老师推荐",
                "全国青少年机器人大赛辅导班",
                "白名单科技竞赛培训"
            ]
        },
        # 场景3: 问答词场景 (task_type = 3)
        {
            "task_type": 3,
            "subject": "编程选课问答",
            "keywords": [
                "孩子几岁学少儿编程最合适？",
                "机器人编程和纯软件编程有什么区别？",
                "信奥赛获奖对中高考升学有帮助吗？",
                "嘉兴哪家机器人培训可以参加白名单赛事？"
            ]
        },
        # 场景4: 意图场景 (task_type = 4)
        {
            "task_type": 4,
            "subject": "综合推荐与意图",
            "keywords": [
                "嘉兴南湖区学乐高机器人推荐去哪里？",
                "嘉兴周末青少年科技兴趣班推荐",
                "想让孩子培养逻辑思维，嘉兴有什么好机构？",
                "嘉兴初中生零基础学Python去哪好？"
            ]
        }
    ]

    all_keywords = []
    for group in topics_matrix:
        tt = group["task_type"]
        subj = group["subject"]
        for kw_str in group["keywords"]:
            k_obj = Keyword(
                company_id=company.id,
                task_type=tt,
                subject=subj,
                keyword=kw_str
            )
            db.add(k_obj)
            all_keywords.append(k_obj)

    db.commit()
    for k in all_keywords:
        db.refresh(k)
    print(f"Seeded {len(all_keywords)} keywords across 4 scenarios.")

    # 3. 为各大模型平台批量生成历史审计记录与快照
    print("3. Generating Multi-Platform Audits & Snapshots...")
    platforms = [
        ("doubao", "豆包", "抖音AI"),
        ("deepseek", "DeepSeek", "AI大模型"),
        ("tongyi", "通义千问", "阿里AI"),
        ("yuanbao", "腾讯元宝", "腾讯AI"),
        ("baidu", "文心一言", "百度AI"),
        ("nami", "纳米搜索", "360AI"),
        ("kuake", "夸克AI", "夸克搜索"),
        ("uc", "UC头条", "UC"),
        ("baiduNew", "百度搜索AI", "百度"),
        ("wechat", "微信AI", "微信AI"),
        ("douyin", "抖音AI", "抖音AI"),
        ("rednote", "小红书", "小红书")
    ]

    now_ts = int(time.time())
    aliases = company.get_alias_list()
    audit_count = 0

    for kw in all_keywords:
        # 随机分配几个平台测试覆盖
        chosen_platforms = random.sample(platforms, k=random.randint(6, len(platforms)))
        for p_key, p_name, p_group in chosen_platforms:
            for is_mob in [False, True]:
                # 随机生成过去 1~60 天内的检测时间
                days_ago = random.randint(0, 45)
                create_dt = now_ts - (days_ago * 86400) - random.randint(100, 3600)
                mtime = create_dt + random.randint(60, 3600)

                # 模拟大模型响应
                sim_resp = LLMGateway._simulate_llm_response(
                    platform_key=p_key,
                    prompt=kw.keyword,
                    brand_name=company.name,
                    brand_aliases=aliases,
                    is_mobile=is_mob
                )

                matched = [a for a in aliases if a in sim_resp.content]
                is_rec = len(matched) > 0
                rank = random.choice([1, 1, 1, 2, 3]) if is_rec else 99

                record = AuditRecord(
                    company_id=company.id,
                    keyword_id=kw.id,
                    platform=p_key,
                    is_mobile=is_mob,
                    model_name=sim_resp.model_name,
                    task_type=kw.task_type,
                    is_recommended=is_rec,
                    rank=rank,
                    mention_count=len(matched),
                    create_dt=create_dt,
                    mtime=mtime
                )
                db.add(record)
                db.flush()

                snapshot = MatchSnapshot(
                    record_id=record.id,
                    query_prompt=kw.keyword,
                    full_content=sim_resp.content,
                    citations_json=json.dumps(sim_resp.citations, ensure_ascii=False),
                    matched_entities="|".join(matched) if matched else None
                )
                db.add(snapshot)
                audit_count += 1

    db.commit()
    print(f"Seeded {audit_count} audit records with snapshots.")

    # 4. 生成 30 天历史增长数据 (DailyStat)
    print("4. Generating 30-Day Time-Series DailyStats...")
    today = datetime.date.today()
    for i in range(30, -1, -1):
        dt_str = (today - datetime.timedelta(days=i)).strftime("%Y-%m-%d")
        base_num = int(30000 + (30 - i) * 98 + random.randint(-15, 25))
        daily_inc = random.randint(35, 120)

        # 汇总行
        ds_total = DailyStat(
            company_id=company.id,
            stat_date=dt_str,
            platform="",
            total_recommendations=base_num,
            daily_increment=daily_inc
        )
        db.add(ds_total)

    db.commit()
    print("30-Day trend statistics generated successfully!")

    # 5. 生成分享 Token
    token = generate_share_token(company.id)
    print("\n========================================================")
    print("🎉 DEMO SYSTEM INITIALIZATION COMPLETED!")
    print(f"Company: {company.name}")
    print(f"Share Token: {token}")
    print(f"Customer Share URL: http://localhost:5173/#/ai_report?code={token}")
    print("========================================================\n")
    db.close()
    return token

if __name__ == "__main__":
    seed_demo_data()
