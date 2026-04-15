from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello from FastAPI!"}

def test_predict_even():
    response = client.get("/predict/4")
    assert response.json()["result"] == "even"

def test_predict_odd():
    response = client.get("/predict/3")
    assert response.json()["result"] == "odd"