from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func
from app.db.session import get_db
from app.models.document import Document, RiskScore, Clause
from app.models.user import User
from app.api.v1.dependencies import get_current_active_user

router = APIRouter()

@router.get("/dashboard")
def get_dashboard_stats(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    total_docs = db.query(Document).filter(Document.uploader_id == current_user.id).count()
    completed_docs = db.query(Document).filter(Document.uploader_id == current_user.id, Document.status == "completed").count()
    
    docs_query = db.query(Document.id).filter(Document.uploader_id == current_user.id)
    total_risks = db.query(RiskScore).filter(RiskScore.document_id.in_(docs_query)).count()
    total_clauses = db.query(Clause).filter(Clause.document_id.in_(docs_query)).count()
    
    avg_risk_query = db.query(func.avg(Document.risk_score)).filter(Document.uploader_id == current_user.id).scalar()
    avg_risk = float(avg_risk_query) if avg_risk_query else 0.0

    return {
        "total_documents": total_docs,
        "processed_documents": completed_docs,
        "total_risks_identified": total_risks,
        "total_clauses_extracted": total_clauses,
        "average_risk_score": round(avg_risk, 2)
    }
