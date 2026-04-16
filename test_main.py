from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_home():
    response = client.get("/")
    assert response.status_code == 200

def test_positive_sentiment():
    response = client.get("/analyze?text=I love this!")
    assert response.json()["sentiment"] == "positive"

def test_negative_sentiment():
    response = client.get("/analyze?text=I hate this!")
    assert response.json()["sentiment"] == "negative"