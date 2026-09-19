import os

from dotenv import load_dotenv
from google import genai
import psycopg2


load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    print("GEMINI_API_KEY was not found.")
    exit()




client = genai.Client(api_key=API_KEY)

MODEL = "gemini-embedding-001"




connection = psycopg2.connect(
    host="localhost",
    port=5432,
    database="pp-38",
    user="postgres",
    password="1810"
)

cursor = connection.cursor()



cursor.execute("""
    CREATE EXTENSION IF NOT EXISTS vector;
""")




cursor.execute("""
    CREATE TABLE IF NOT EXISTS document (
        id SERIAL PRIMARY KEY,
        content TEXT NOT NULL,
        vector vector(768)
    );
""")

connection.commit()




texts = [
    "A small dog running in the park",
    "A puppy playing outside",
    "A new laptop with a fast processor",
    "I love programming in Python",
    "Machine learning is a subset of artificial intelligence",
    "The weather is very cold today",
    "Cats are independent animals",
    "Deep learning uses neural networks"
]




for text in texts:

    response = client.models.embed_content(
        model=MODEL,
        contents=text
    )

    embedding = response.embeddings[0].values

    cursor.execute(
        """
        INSERT INTO document (content, vector)
        VALUES (%s, %s)
        """,
        (text, embedding)
    )

    print(f"Saved: {text}")


connection.commit()

cursor.close()
connection.close()

client.close()

print("\nAll documents were saved successfully.")