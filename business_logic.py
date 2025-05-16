from fastapi import FastAPI
import time

app = FastAPI()

@app.get("/")
def root():
    return {"message": "BS is processing data"}

@app.get("/health")
def health():
    return {"status": "OK"}

@app.post("/process")
def process(payload: dict):
    time.sleep(2)
    return {"original": payload, "processed": True}