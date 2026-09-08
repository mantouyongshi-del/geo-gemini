from pydantic import BaseModel
from typing import Optional, List, Dict, Any

class DiagnosticCreateRequest(BaseModel):
    target_company: str
    brand_name: str
    industry: str
    city: Optional[str] = "全国"
    keywords: List[str]
    agency_name: Optional[str] = "蜉蝣小宝 · 官方直营授权运营中心"
    consultant_name: Optional[str] = "资深数字化营销顾问"
    consultant_phone: Optional[str] = None

class CitationDetail(BaseModel):
    title: str
    url: str
    site_name: str
    summary: Optional[str] = ""

class DiagnosticItemOut(BaseModel):
    id: int
    keyword: str
    platform: str
    platform_name: str
    model_name: Optional[str] = ""
    is_target_mentioned: bool
    target_rank: int
    mined_competitors: List[str]
    raw_content: str
    citations: List[CitationDetail]
    duration_ms: int

class CompetitorAnalysisItem(BaseModel):
    name: str
    mention_count: int
    dominant_platforms: List[str]
    advantage_points: str

class GeoPrescription(BaseModel):
    scenario: str
    task_type: int
    urgency: str
    action: str
    expected_result: str

class FunnelLayerItem(BaseModel):
    layer_key: str
    name: str
    score: int
    max_score: int = 25
    status: str
    status_label: str
    diagnosis: str
    core_evidence: str

class DualDeviceItem(BaseModel):
    platform_key: str
    platform_name: str
    device: str
    is_mobile: bool
    is_indexed: bool
    status_desc: str

class CompetitorSourceItem(BaseModel):
    site_name: str
    source_type: str
    citation_count: int
    target_coverage: str
    competitor_names: List[str]
    threat_level: str

class EconomicLossEstimate(BaseModel):
    industry: str
    estimated_unit_price: int
    unit_price_desc: str
    monthly_search_inquiries: int
    monthly_lost_leads_min: int
    monthly_lost_leads_max: int
    monthly_loss_amount_min: int
    monthly_loss_amount_max: int
    annual_loss_amount_est: int
    payback_leads_needed: int
    calculation_note: str

class ImplementationPhase(BaseModel):
    phase: int
    day_range: str
    title: str
    core_action: str
    deliverable: str
    expected_kpi: str

class DiagnosticReportOut(BaseModel):
    id: int
    report_code: str
    target_company: str
    brand_name: str
    industry: str
    city: str
    search_keywords: List[str]
    agency_name: str
    consultant_name: str
    consultant_phone: Optional[str] = None
    visibility_score: int
    risk_level: str
    summary_verdict: str
    competitors: List[CompetitorAnalysisItem]
    prescriptions: List[GeoPrescription]
    funnel_metrics: Optional[List[FunnelLayerItem]] = []
    dual_device_matrix: Optional[List[DualDeviceItem]] = []
    competitor_sources: Optional[List[CompetitorSourceItem]] = []
    economic_loss: Optional[EconomicLossEstimate] = None
    implementation_roadmap: Optional[List[ImplementationPhase]] = []
    created_at: int
    items: List[DiagnosticItemOut]
    share_url: Optional[str] = None
