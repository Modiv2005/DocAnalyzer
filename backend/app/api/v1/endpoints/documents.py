import os
import uuid
from typing import List
from fastapi import APIRouter, Depends, UploadFile, File, HTTPException, BackgroundTasks
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.models.user import User
from app.models.document import Document
from app.schemas.document import DocumentResponse, DocumentDetailResponse
from app.api.v1.dependencies import get_current_active_user
from app.tasks.document_tasks import process_document_task

router = APIRouter()

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.post("/upload", response_model=DocumentResponse)
async def upload_document(
    background_tasks: BackgroundTasks,
    file: UploadFile = File(...),
    category: str = "general",
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    file_ext = file.filename.split(".")[-1]
    unique_filename = f"{uuid.uuid4()}.{file_ext}"
    file_path = os.path.join(UPLOAD_DIR, unique_filename)

    with open(file_path, "wb") as f:
        content = await file.read()
        f.write(content)

    doc = Document(
        title=file.filename,
        filename=unique_filename,
        file_path=file_path,
        file_type=file_ext,
        category=category,
        uploader_id=current_user.id
    )
    db.add(doc)
    db.commit()
    db.refresh(doc)

    # Trigger processing task via BackgroundTasks
    background_tasks.add_task(process_document_task, doc.id)

    return doc

@router.get("/", response_model=List[DocumentResponse])
def get_documents(
    skip: int = 0, limit: int = 100, 
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    docs = db.query(Document).filter(Document.uploader_id == current_user.id).offset(skip).limit(limit).all()
    return docs

@router.get("/{document_id}", response_model=DocumentDetailResponse)
def get_document(
    document_id: int, 
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    doc = db.query(Document).filter(Document.id == document_id, Document.uploader_id == current_user.id).first()
    if not doc:
        raise HTTPException(status_code=404, detail="Document not found")
    return doc
