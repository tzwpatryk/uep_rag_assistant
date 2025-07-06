from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"status": "UEP RAG Assistant is live"}