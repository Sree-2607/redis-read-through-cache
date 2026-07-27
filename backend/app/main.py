from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {
        "message": "Redis Read Through Cache Todo API"
    }