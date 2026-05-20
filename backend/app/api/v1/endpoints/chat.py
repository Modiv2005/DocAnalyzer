from fastapi import APIRouter, Depends
from pydantic import BaseModel
from typing import List, Optional
from app.models.user import User
from app.api.v1.dependencies import get_current_active_user

router = APIRouter()

class ChatMessage(BaseModel):
    role: str
    content: str

class ChatRequest(BaseModel):
    messages: List[ChatMessage]
    document_ids: Optional[List[int]] = None

@router.post("/completions")
def chat_completion(
    request: ChatRequest,
    current_user: User = Depends(get_current_active_user)
):
    # This is a mock response since we don't have a live OpenAI key
    # In a real scenario, we would use LangChain + ChromaDB for RAG here.
    last_message = request.messages[-1].content
    
    mock_response = f"This is an AI generated response to your query: '{last_message}'. " \
                    f"Based on the enterprise documents provided, the risk analysis indicates standard compliance."
    
    return {
        "reply": mock_response,
        "citations": [
            {"document_id": 1, "text_snippet": "Relevant clause regarding compliance."}
        ] if request.document_ids else []
    }
