from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, Text, Float
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.db.base import Base

class Document(Base):
    __tablename__ = "documents"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    filename = Column(String)
    file_path = Column(String)
    file_type = Column(String)
    status = Column(String, default="uploaded") # uploaded, processing, completed, failed
    risk_score = Column(Float, nullable=True)
    category = Column(String, nullable=True) # legal, tax, compliance, audit
    
    uploader_id = Column(Integer, ForeignKey("users.id"))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    uploader = relationship("User")
    clauses = relationship("Clause", back_populates="document", cascade="all, delete-orphan")
    risks = relationship("RiskScore", back_populates="document", cascade="all, delete-orphan")

class Clause(Base):
    __tablename__ = "clauses"

    id = Column(Integer, primary_key=True, index=True)
    document_id = Column(Integer, ForeignKey("documents.id"))
    clause_type = Column(String) # payment, termination, confidentiality
    text = Column(Text)
    page_number = Column(Integer, nullable=True)
    
    document = relationship("Document", back_populates="clauses")

class RiskScore(Base):
    __tablename__ = "risk_scores"

    id = Column(Integer, primary_key=True, index=True)
    document_id = Column(Integer, ForeignKey("documents.id"))
    risk_type = Column(String)
    severity = Column(String) # low, medium, high, critical
    description = Column(Text)
    clause_reference_id = Column(Integer, ForeignKey("clauses.id"), nullable=True)
    
    document = relationship("Document", back_populates="risks")
