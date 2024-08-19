from openai import OpenAI
from dotenv import load_dotenv
from pydantic import BaseModel, Field
load_dotenv()
import json


class BookBiteModel(BaseModel):
    title: str = Field(description="Name of the book")
    author: str = Field(description="Name of the books author")
    dop: str = Field(description="Date of publishing the book")
    summary: str = Field(description="Short summary of the book in less than 100 words")
    ecom_url: str = Field(description="Online URL from Amazon to purchase book")


class BookSummarizer:
    @staticmethod
    def get_book_summary(title: str, author: str=""):
        client = OpenAI()
        prompt = f"Tell me about {title}"
        if author:
            prompt += f" written by {author}"
        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system",
                 "content": "You are a librarian with an immense knowledge in books. \
                    Your task is to present a summary of a given book title along with the author's name. The author name may or may not be given. \
                       Note that the user may have given an imaginary title. If so, suggest the right title and request them to check the title once again."
                    },
                {"role": "user", "content": prompt}
            ],
            response_format={"type": "json_schema",  "json_schema": {"name": "BookBiteModel", "schema": BookBiteModel.model_json_schema()}},
            temperature=0
            )
        return json.loads(completion.choices[0].message.content)
