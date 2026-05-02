from fastapi import APIRouter
from app.schemas.sentiment_schema import TextRequest, SentimentResponse
from app.services.sentiment_service import analyze_sentiment

router = APIRouter()

@router.post("/sentiment", response_model=SentimentResponse)
def get_sentiment(data: TextRequest):
    return analyze_sentiment(data.text)