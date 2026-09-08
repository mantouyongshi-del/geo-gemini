from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional
from app.core.database import get_db
from app.models.diagnostic import DiagnosticReport
from app.schemas.diagnostic import DiagnosticCreateRequest, DiagnosticReportOut
from app.services.diagnostic_service import DiagnosticService

router = APIRouter()

@router.post("/run", response_model=DiagnosticReportOut)
async def run_enterprise_diagnostic(payload: DiagnosticCreateRequest, db: Session = Depends(get_db)):
    """
    【蜉蝣小宝 · 售前获客核武器】
    输入准客户企业名称与核心搜索词，真实调度五大主流 AI 搜索引擎，出具深度可见度体检报告
    """
    if not payload.target_company.strip():
        raise HTTPException(status_code=400, detail="企业名称不能为空")
    if not payload.keywords or len(payload.keywords) == 0:
        raise HTTPException(status_code=400, detail="至少需输入一个测试关键词")

    try:
        report = await DiagnosticService.execute_diagnostic(payload, db)
        return DiagnosticService.get_report_by_code(report.report_code, db)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"体检执行异常: {str(e)}")

@router.get("/{report_code}", response_model=DiagnosticReportOut)
def get_diagnostic_report(report_code: str, db: Session = Depends(get_db)):
    """
    通过专属报告码获取公开只读体检诊断书 (支持微信 H5 扫码打开与一键打印 PDF)
    """
    try:
        return DiagnosticService.get_report_by_code(report_code, db)
    except ValueError:
        raise HTTPException(status_code=404, detail="未找到该体检报告，可能已过期或链接有误")

@router.get("/recent/list")
def list_recent_diagnostics(limit: int = 15, db: Session = Depends(get_db)):
    """
    获取加盟商销售顾问近期生成的体检报告列表
    """
    reports = db.query(DiagnosticReport).order_by(DiagnosticReport.created_at.desc()).limit(limit).all()
    results = []
    for r in reports:
        results.append({
            "report_code": r.report_code,
            "target_company": r.target_company,
            "brand_name": r.brand_name,
            "industry": r.industry,
            "visibility_score": r.visibility_score,
            "risk_level": r.risk_level,
            "created_at": r.created_at,
            "share_url": f"http://localhost:5173/#/diagnostic_report?code={r.report_code}"
        })
    return results
