from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1.endpoints import auth, documents, analytics, chat
from app.core.config import settings

app = FastAPI(
    title="Intelligent Document Analytics API",
    description="Enterprise-grade AI-powered document intelligence platform API",
    version="1.0.0",
)

from app.db.base import Base
from app.db.session import engine
from app.models import user, document

# Create tables
Base.metadata.create_all(bind=engine)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins in development
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include Routers
app.include_router(auth.router, prefix="/api/v1/auth", tags=["auth"])
app.include_router(documents.router, prefix="/api/v1/documents", tags=["documents"])
app.include_router(analytics.router, prefix="/api/v1/analytics", tags=["analytics"])
app.include_router(chat.router, prefix="/api/v1/chat", tags=["chat"])

@app.get("/")
def root():
    return {"message": "Welcome to Intelligent Document Analytics API"}
