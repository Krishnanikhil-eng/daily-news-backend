from fastapi import FastAPI
from .database import get_all_news


app = FastAPI()

@app.get("/")
def home():
    return {"message": "API is working"}

@app.get("/news")
def read_news():
    data = get_all_news()
    return {"news": data}
