from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import Optional, List
from app.core.database import get_db
from app.core.security import verify_share_token
from app.models.company import Company
from app.services.report_service import ReportService
from app.schemas.report import (
    SummaryStatsOut, PlatformStatItem, TopKeywordsOut,
    RankingListResponse, MatchResultDetailOut, HistoryTrendResponse
)

router = APIRouter()

def resolve_company_id(code: Optional[str] = None, company_id: Optional[int] = None) -> int:
    if code:
        cid = verify_share_token(code)
        if not cid:
            # 宽容处理：如果传的是纯数字ID，方便开发测试
            if code.isdigit():
                return int(code)
            raise HTTPException(status_code=403, detail="无效或已过期的报表访问授权码 (Invalid Share Token)")
        return cid
    if company_id:
        return company_id
    raise HTTPException(status_code=400, detail="Missing share code or company_id")

@router.get("/company-info")
def get_report_company_info(
    code: Optional[str] = Query(None),
    company_id: Optional[int] = Query(None),
    db: Session = Depends(get_db)
):
    cid = resolve_company_id(code, company_id)
    company = db.query(Company).filter(Company.id == cid).first()
    if not company:
        raise HTTPException(status_code=404, detail="Company not found")
    
    aliases = company.get_alias_list()
    return {
        "id": company.id,
        "name": company.name,
        "short_name": company.short_name or company.name,
        "logo_url": company.logo_url,
        "industry": company.industry,
        "brand_aliases": aliases
    }

@router.get("/summary", response_model=SummaryStatsOut)
def get_report_summary(
    code: Optional[str] = Query(None),
    company_id: Optional[int] = Query(None),
    db: Session = Depends(get_db)
):
    cid = resolve_company_id(code, company_id)
    return ReportService.get_summary_stats(cid, db)

@router.get("/platforms", response_model=List[PlatformStatItem])
def get_report_platforms(
    code: Optional[str] = Query(None),
    company_id: Optional[int] = Query(None),
    taskType: int = Query(0, description="0:全部, 1:品牌, 2:搜索, 3:问答, 4:意图"),
    db: Session = Depends(get_db)
):
    cid = resolve_company_id(code, company_id)
    return ReportService.get_platform_stats(cid, taskType, db)

@router.get("/top-keywords", response_model=TopKeywordsOut)
def get_report_top_keywords(
    code: Optional[str] = Query(None),
    company_id: Optional[int] = Query(None),
    db: Session = Depends(get_db)
):
    cid = resolve_company_id(code, company_id)
    return ReportService.get_top_keywords(cid, db)

class RankingQueryRequest(BaseModel):
    page: int = 1
    rows: int = 10
    taskType: int = 0
    type: Optional[str] = None
    sort: str = "mtime"
    order: str = "SORT_DESC"

@router.post("/rankings", response_model=RankingListResponse)
def get_report_rankings(
    query: RankingQueryRequest,
    code: Optional[str] = Query(None),
    company_id: Optional[int] = Query(None),
    db: Session = Depends(get_db)
):
    cid = resolve_company_id(code, company_id)
    return ReportService.get_ranking_list(
        company_id=cid,
        task_type=query.taskType,
        platform=query.type,
        page=query.page,
        rows=query.rows,
        sort=query.sort,
        order=query.order,
        db=db
    )

@router.get("/match-detail/{rid}", response_model=MatchResultDetailOut)
def get_report_match_detail(
    rid: int,
    code: Optional[str] = Query(None),
    company_id: Optional[int] = Query(None),
    db: Session = Depends(get_db)
):
    cid = resolve_company_id(code, company_id)
    detail = ReportService.get_match_detail(rid, db)
    if not detail:
        raise HTTPException(status_code=404, detail="Match record not found")
    return detail

@router.get("/trend", response_model=HistoryTrendResponse)
def get_report_trend(
    code: Optional[str] = Query(None),
    company_id: Optional[int] = Query(None),
    days: int = Query(30, ge=7, le=90),
    db: Session = Depends(get_db)
):
    cid = resolve_company_id(code, company_id)
    return ReportService.get_history_trend(cid, days, db)
