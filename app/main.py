from fastapi import FastAPI
from app.routers import sentiment, summarization, classification


app = FastAPI()

app.include_router(sentiment.router, prefix="/api")
app.include_router(summarization.router, prefix="/api")
app.include_router(classification.router, prefix="/api")
    
@app.get("/")
def root():
    return {"message": "API is running"}