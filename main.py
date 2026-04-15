from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello from FastAPI!"}

@app.get("/predict/{number}")
def predict(number: int):
    if number % 2 == 0:
        result = "even"
    else:
        result = "odd"
    return {"number": number, "result": result}