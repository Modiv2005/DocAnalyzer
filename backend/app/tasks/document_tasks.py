import time
import random
from app.db.session import SessionLocal
from app.models.document import Document, RiskScore, Clause

def process_document_task(document_id: int):
    # This is a placeholder for real AI/OCR pipeline
    db = SessionLocal()
    try:
        doc = db.query(Document).filter(Document.id == document_id).first()
        if not doc:
            return "Document not found"

        doc.status = "processing"
        db.commit()

        # Simulate OCR and AI Extraction delay
        time.sleep(5)

        # Generate fake clauses
        sample_clauses = [
            {"clause_type": "Payment", "text": "The client shall pay the invoice within 30 days."},
            {"clause_type": "Termination", "text": "Either party may terminate this agreement with a 60-day written notice."},
            {"clause_type": "Confidentiality", "text": "All proprietary information must remain confidential."}
        ]

        for c in sample_clauses:
            clause = Clause(document_id=doc.id, clause_type=c["clause_type"], text=c["text"], page_number=1)
            db.add(clause)

        # Generate fake risk
        risk = RiskScore(
            document_id=doc.id, 
            risk_type="Payment Terms", 
            severity="medium", 
            description="Net 30 payment terms might cause cash flow issues."
        )
        db.add(risk)

        doc.risk_score = random.uniform(20.0, 80.0)
        doc.status = "completed"
        db.commit()

        return f"Document {document_id} processed successfully."
    except Exception as e:
        db.rollback()
        if doc:
            doc.status = "failed"
            db.commit()
        raise e
    finally:
        db.close()
