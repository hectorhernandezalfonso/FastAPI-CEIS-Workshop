from app.models.sentiment_model import predict_sentiment

def analyze_sentiment(text: str):
    result = predict_sentiment(text)

    label = result["label"]

    if label == "POSITIVE":
        sentiment = "positive"
    elif label == "NEGATIVE":
        sentiment = "negative"
    else:
        sentiment = "neutral"

    return {
        "sentiment": sentiment,
        "confidence": result["score"]
    }