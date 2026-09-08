from pydantic import BaseModel
from typing import Optional

class KeywordBase(BaseModel):
    task_type: int = 2  # 1: 品牌, 2: 搜索, 3: 问答, 4: 意图
    subject: str
    keyword: str

class KeywordCreate(KeywordBase):
    company_id: int

class KeywordBatchCreate(BaseModel):
    company_id: int
    task_type: int = 2
    subject: str
    keywords: list[str]

class KeywordOut(KeywordBase):
    id: int
    company_id: int
    created_at: int

    class Config:
        from_attributes = True
