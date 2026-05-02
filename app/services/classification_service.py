from app.models.classification_model import classify_text

def classify(text: str, labels: list[str]):
    result = classify_text(text, labels)

    return {
        "labels": result["labels"],
        "scores": result["scores"]
    }