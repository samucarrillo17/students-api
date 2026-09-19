from fastapi import FastAPI
from config import APP_VERSION

app = FastAPI(title="students-api")

@app.get("/health")
def health():
    return {status: "healthy"}

@app.get("/students")
def list_students()
    return[{"id":1, "name":"Ana"}, {"id":2, "name":"Armando"}]