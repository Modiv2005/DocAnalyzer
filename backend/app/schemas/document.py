from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class RiskScoreBase(BaseModel):
    risk_type: str
    severity: str
    description: str
    clause_reference_id: Optional[int] = None

class ClauseBase(BaseModel):
    clause_type: str
    text: str
    page_number: Optional[int] = None

class DocumentBase(BaseModel):
    title: str
    category: Optional[str] = None

class DocumentResponse(DocumentBase):
    id: int
    filename: str
    status: str
    risk_score: Optional[float] = None
    created_at: datetime
    uploader_id: int

    class Config:
        from_attributes = True

class DocumentDetailResponse(DocumentResponse):
    clauses: List[ClauseBase] = []
    risks: List[RiskScoreBase] = []
