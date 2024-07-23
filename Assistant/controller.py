from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

class BookSummarizer:
    @staticmethod
    def get_book_summary(title: str, author: str=""):
        client = OpenAI()
        prompt = f"In less than 100 words, provide a summary of {title}"
        if author:
            prompt += f" written by {author}"
        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system",
                 "content": "You are an avid reader and have immense knowledge in books. \
                    Your task is to present a summary of a given book title along with the author's name. The author name may or may not be given. \
                       Note that the user may have given an imaginary title. If so, suggest the right title and request them to check the title once again."
                    },
                {"role": "user", "content": prompt}
            ],
            temperature=0.1
            )
        return {"message": completion.choices[0].message.content}