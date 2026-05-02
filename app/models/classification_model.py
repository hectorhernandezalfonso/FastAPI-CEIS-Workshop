from transformers import pipeline

classifier = pipeline("zero-shot-classification")

def classify_text(text: str, labels: list[str]):
    result = classifier(text, candidate_labels=labels)
    return result