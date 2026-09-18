from fastapi import FastAPI
from config import APP_VERSION

app = FastAPI(title="students-api")

@app.get("/health")
def health():
    return {status: "ok"}