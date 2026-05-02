from fastapi import APIRouter
from app.schemas.summarization_schema import SummarizationRequest, SummarizationResponse
from app.services.summarization_service import summarize

router = APIRouter()

@router.post("/summarize", response_model=SummarizationResponse)
def summarize_endpoint(data: SummarizationRequest):
    return summarize(data.text)