from pydantic import BaseModel
from typing import Optional, List, Dict, Any

class SummaryStatsOut(BaseModel):
    recommendationNumber: int
    historyTotalNumber: int
    sevenDayIncreaseNumber: int
    thirtyDayIncreaseNumber: int
    sevenDayIncreaseHistoryNumber: int
    thirtyDayIncreaseHistoryNumber: int

class PlatformStatItem(BaseModel):
    id: int
    name: str
    type: str
    count: int
    p: Optional[str] = None
    is_mobile: bool = False

class TaskScenarioStats(BaseModel):
    task_type: int
    name: str
    p_name: str
    count: int

class TopKeywordItem(BaseModel):
    subject: str
    type: str
    count: int

class TopKeywordsOut(BaseModel):
    count: int
    list: List[TopKeywordItem]

class RankingRecordOut(BaseModel):
    rid: int
    keyword: str
    subject: str
    taskType: int
    type: str
    isMobile: bool
    rank: int
    mentionCount: int
    mtime: int
    createDt: int
    hasSnapshot: bool

class RankingListResponse(BaseModel):
    total: int
    page: int
    rows: int
    records: List[RankingRecordOut]

class CitationItem(BaseModel):
    title: str
    url: str
    site_name: str
    summary: Optional[str] = ""

class MatchResultDetailOut(BaseModel):
    rid: int
    keyword: str
    query_prompt: str
    content: str
    matched_entities: List[str]
    citations: List[CitationItem]

class HistoryDateStat(BaseModel):
    totalDate: str
    totalNumber: int

class HistoryDetailStat(BaseModel):
    totalDate: str
    platformType: str
    number: int

class HistoryTrendResponse(BaseModel):
    statistics: List[HistoryDateStat]
    detailList: List[HistoryDetailStat]
