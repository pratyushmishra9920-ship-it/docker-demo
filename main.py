from fastapi import FastAPI
from textblob import TextBlob

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to Sentiment Analyzer API!"}

@app.get("/analyze")
def analyze(text: str):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity

    if polarity > 0:
        sentiment = "positive"
        emoji = "😊"
    elif polarity < 0:
        sentiment = "negative"
        emoji = "😞"
    else:
        sentiment = "neutral"
        emoji = "😐"

    confidence = str(round(abs(polarity) * 100)) + "%"

    return {
        "text": text,
        "sentiment": sentiment,
        "confidence": confidence,
        "emoji": emoji
    }