from fastapi import FastAPI
import uvicorn
from Assistant.controller import BookSummarizer
from Assistant.samples import sample_summary
from typing import Optional

app = FastAPI(title="Your personal book summarizer",
              description="Looking for your next read? Give us a title and we'll give you a sneak peek.", 
              version="1.0.0")


@app.get("/")
def home():
    return {"message": "Hello there! How can I help?"}


@app.get("/summarize", status_code=200, responses=sample_summary)
def summary_request(title: str, author: Optional[str] = ""):
    response = BookSummarizer.get_book_summary(title, author)
    return response


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
