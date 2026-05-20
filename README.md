# Intelligent Document Analytics for Legal / Tax / Compliance

Enterprise-grade AI-powered document intelligence platform processing legal, tax, audit, compliance, and regulatory documents using NLP, OCR, LLMs, and RAG.

## Architecture
- **Frontend**: React, TypeScript, Vite, TailwindCSS, Zustand, TanStack Query
- **Backend**: FastAPI, SQLAlchemy, PostgreSQL, Celery, Redis
- **AI/NLP**: LangChain, HuggingFace, ChromaDB, spaCy
- **Infrastructure**: Docker Compose

## Setup Instructions

1. **Prerequisites**
   - Docker and Docker Compose installed
   - Node.js (for local frontend dev)
   - Python 3.11+ (for local backend dev)

2. **Environment Variables**
   Create a `.env` file in the root directory and add:
   ```env
   POSTGRES_USER=postgres
   POSTGRES_PASSWORD=password
   POSTGRES_DB=doc_analytics
   SECRET_KEY=your_secret_key
   OPENAI_API_KEY=your_openai_api_key_if_applicable
   ```

3. **Running the Application via Docker**
   ```bash
   docker-compose up --build -d
   ```
   - Frontend: `http://localhost:3000`
   - Backend API Docs: `http://localhost:8080/docs`

4. **Local Development**
   - **Backend**:
     ```bash
     cd backend
     python -m venv venv
     source venv/bin/activate
     pip install -r requirements.txt
     uvicorn app.main:app --reload
     ```
   - **Frontend**:
     ```bash
     cd frontend
     npm install
     npm run dev
     ```

## Features
- JWT Authentication & Role-based Access
- Asynchronous Document Processing Pipeline (Celery)
- Risk & Clause Extraction (Mocked/Configurable via AI models)
- Analytics Dashboard
- Responsive Enterprise UI
