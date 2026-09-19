import os

from dotenv import load_dotenv
from google import genai
from google.genai import types
from pydantic import BaseModel



load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")


if not API_KEY:
    print("❌ GEMINI_API_KEY was not found.")
    print("Please add it to your .env file.")
    exit()




class Book(BaseModel):
    title: str
    author: str
    year: int
    genres: list[str]




client = genai.Client(api_key=API_KEY)

MODEL = "gemini-2.5-flash"




prompt = """
Recommend one interesting mystery book to read.

Return only the information required by the Book structure.
Do not add explanations outside the requested structure.
"""


try:

    response = client.models.generate_content(
        model=MODEL,
        contents=prompt,
        config=types.GenerateContentConfig(
            response_mime_type="application/json",
            response_schema=Book
        )
    )




    book = Book.model_validate_json(response.text)




    print("\n========== BOOK ==========")

    print(f"Title: {book.title}")
    print(f"Author: {book.author}")
    print(f"Year: {book.year}")
    print(f"Genres: {', '.join(book.genres)}")


except Exception as e:

    print("❌ An error occurred.")
    print(f"Error type: {type(e).__name__}")
    print(f"Description: {e}")


client.close()