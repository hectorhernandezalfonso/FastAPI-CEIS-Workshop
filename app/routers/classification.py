from fastapi import APIRouter
from app.schemas.classification_schema import ClassificationRequest, ClassificationResponse
from app.services.classification_service import classify

router = APIRouter()

@router.post("/classify", response_model=ClassificationResponse)
def classify_endpoint(data: ClassificationRequest):
    return classify(data.text, data.labels)