import os

from dotenv import load_dotenv
from pydantic import BaseModel, Field
from langchain_google_genai import ChatGoogleGenerativeAI


load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    print("❌ GEMINI_API_KEY was not found.")
    exit()



class Book(BaseModel):
    title: str
    author: str
    year: int
    genres: list[str]
    pages: int




llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=API_KEY,
    temperature=0
)




structured_llm = llm.with_structured_output(Book)




text = """
George Orwell's famous novel 1984 was published in 1949.
It is a dystopian political fiction book with 328 pages.
"""



book = structured_llm.invoke(text)




print("========== BOOK ==========")
print(f"Title: {book.title}")
print(f"Author: {book.author}")
print(f"Year: {book.year}")
print(f"Genres: {', '.join(book.genres)}")
print(f"Pages: {book.pages}")