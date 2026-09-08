from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Optional
from app.core.database import get_db
from app.models.keyword import Keyword
from app.models.company import Company
from app.schemas.keyword import KeywordCreate, KeywordBatchCreate, KeywordOut

router = APIRouter()

@router.post("/", response_model=KeywordOut)
def create_keyword(payload: KeywordCreate, db: Session = Depends(get_db)):
    kw = Keyword(
        company_id=payload.company_id,
        task_type=payload.task_type,
        subject=payload.subject,
        keyword=payload.keyword
    )
    db.add(kw)
    db.commit()
    db.refresh(kw)
    return kw

@router.post("/batch", response_model=List[KeywordOut])
def batch_create_keywords(payload: KeywordBatchCreate, db: Session = Depends(get_db)):
    company = db.query(Company).filter(Company.id == payload.company_id).first()
    if not company:
        raise HTTPException(status_code=404, detail="Company not found")

    created = []
    for text in payload.keywords:
        text = text.strip()
        if not text:
            continue
        kw = Keyword(
            company_id=payload.company_id,
            task_type=payload.task_type,
            subject=payload.subject,
            keyword=text
        )
        db.add(kw)
        created.append(kw)
    db.commit()
    for kw in created:
        db.refresh(kw)
    return created

@router.get("/company/{company_id}", response_model=List[KeywordOut])
def list_company_keywords(
    company_id: int, 
    task_type: Optional[int] = None,
    skip: int = 0, 
    limit: int = 200, 
    db: Session = Depends(get_db)
):
    query = db.query(Keyword).filter(Keyword.company_id == company_id)
    if task_type:
        query = query.filter(Keyword.task_type == task_type)
    return query.offset(skip).limit(limit).all()
