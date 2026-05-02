from app.models.summarization_model import summarize_text

def summarize(text: str):
    summary = summarize_text(text)
    return {
        "summary": summary
    }