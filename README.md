# FastAPI + AI CEIS Workshop

This project demonstrates how to build a backend API using FastAPI and integrate multiple AI capabilities using pretrained models.

---

## Features

This API exposes multiple AI-powered endpoints:

* Sentiment Analysis → `/api/sentiment`
* Text Summarization → `/api/summarize`
* Zero-shot Classification → `/api/classify`

---

## Project Structure

app/

├── main.py


├── routers/


├── services/


├── models/


└── schemas/



### Architecture

* routers/ → HTTP layer (endpoints)
* services/ → business logic
* models/ → AI models (Hugging Face)
* schemas/ → Data models for validation

---

## Setup

### 1. Clone the repo

git clone https://github.com/hectorhernandezalfonso/FastAPI-CEIS-Workshop.git


cd folder

---

### 2. Create virtual environment

python3 -m venv .venv
source .venv/bin/activate

---

### 3. Install dependencies

pip install -r requirements.txt

---

## Run the API

fastapi dev

Open in browser:
[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

or

[http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## Notes

* Models are downloaded automatically on first run
* This may take some time depending on your internet connection
* After that, everything runs locally

---

## Learning Goals

This project demonstrates:

* How APIs work (HTTP + JSON)
* Clean backend architecture (router/service/model)
* How to integrate AI into backend systems
* How pretrained models can be used in production

---

## Requirements

fastapi[standard]
transformers==4.41.2
torch

---

## Author

Workshop by Héctor Alfonso
