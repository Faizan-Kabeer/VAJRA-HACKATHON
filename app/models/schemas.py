from pydantic import BaseModel, Field
from typing import List, Optional

# --- Input Schemas ---

class ClientContext(BaseModel):
    """Configuration that influences analysis based on business rules."""
    domain: str = Field(..., example="Banking")
    products: List[str] = Field(..., example=["Credit Cards", "Savings Accounts"])
    policies: List[str] = Field(..., example=["No remote desktop software allowed"])
    risk_triggers: List[str] = Field(..., example=["AnyDesk", "crypto", "unauthorized transfer"])

class AnalysisRequest(BaseModel):
    """Schema for text-based conversation analysis."""
    transcript: str
    client_context: ClientContext

# --- Output Schemas ---

class CoreIntelligence(BaseModel):
    """Mandatory intelligence markers."""
    summary: str
    detected_languages: List[str]
    overall_sentiment: str
    primary_intents: List[str]
    key_topics: List[str]

class AdvancedAnalysis(BaseModel):
    """Enterprise-level flags and classifications."""
    compliance_violations: List[str]
    risk_score: int = Field(ge=0, le=100) # Scale of 0-100
    risk_flags: List[str]
    call_outcome: str # e.g., Resolved, Escalated, Dropped
    agent_quality_score: Optional[int] = None

class AnalysisResponse(BaseModel):
    """The final structured JSON response sent to the client."""
    status: str
    input_type: str # "audio" or "text"
    core_intelligence: CoreIntelligence
    advanced_analysis: AdvancedAnalysis
    raw_transcript: Optional[str] = None