import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    PROJECT_NAME: str = "GEO-Matrix AI 搜索引擎优化与巡检系统"
    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str = os.getenv("GEO_SECRET_KEY", "geo-super-secret-key-change-in-production-2026")
    
    # 数据库配置 (默认使用轻量 SQLite，支持无缝切换到 PostgreSQL)
    _DEFAULT_DB = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), "geo_system.db")
    DATABASE_URL: str = os.getenv(
        "DATABASE_URL", 
        f"sqlite:///{_DEFAULT_DB}"
    )
    
    # 大模型 API 密钥配置 (可选配置，未配置时自动启用高质量异构爬虫分析引擎)
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "")
    OPENAI_BASE_URL: str = os.getenv("OPENAI_BASE_URL", "https://api.openai.com/v1")
    DEEPSEEK_API_KEY: str = os.getenv("DEEPSEEK_API_KEY", "")
    DOUBAO_API_KEY: str = os.getenv("DOUBAO_API_KEY", "")
    DOUBAO_MODEL_NAME: str = os.getenv("DOUBAO_MODEL_NAME", "doubao-seed-2-0-lite-260215")
    DASHSCOPE_API_KEY: str = os.getenv("DASHSCOPE_API_KEY", os.getenv("QWEN_API_KEY", ""))
    QWEN_API_KEY: str = os.getenv("QWEN_API_KEY", os.getenv("DASHSCOPE_API_KEY", ""))
    BAIDU_API_KEY: str = os.getenv("BAIDU_API_KEY", "")
    HUNYUAN_API_KEY: str = os.getenv("HUNYUAN_API_KEY", "")
    MOONSHOT_API_KEY: str = os.getenv("MOONSHOT_API_KEY", "")

settings = Settings()
