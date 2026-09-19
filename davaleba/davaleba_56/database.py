import os

import psycopg2

from google import genai
from dotenv import load_dotenv


load_dotenv()




API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError(
        "GEMINI_API_KEY was not found."
    )


client = genai.Client(api_key=API_KEY)

EMBEDDING_MODEL = "gemini-embedding-001"



def get_connection():
    return psycopg2.connect(
        host=os.getenv("DB_HOST", "localhost"),
        port=os.getenv("DB_PORT", "5432"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER", "postgres"),
        password=os.getenv("DB_PASSWORD")
    )




def create_table():

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        CREATE EXTENSION IF NOT EXISTS vector;
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS document (
            id SERIAL PRIMARY KEY,
            content TEXT NOT NULL,
            vector vector(768),
            file_name TEXT NOT NULL,
            chunk_index INTEGER NOT NULL
        );
    """)

    connection.commit()

    cursor.close()
    connection.close()




def get_embedding(text: str):

    response = client.models.embed_content(
        model=EMBEDDING_MODEL,
        contents=text
    )

    return response.embeddings[0].values




def insert_chunk(
    content: str,
    file_name: str,
    chunk_index: int
):

    embedding = get_embedding(content)

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO document
        (
            content,
            vector,
            file_name,
            chunk_index
        )
        VALUES (%s, %s, %s, %s)
        """,
        (
            content,
            embedding,
            file_name,
            chunk_index
        )
    )

    connection.commit()

    cursor.close()
    connection.close()




def similarity_search(
    query: str,
    top_k: int = 3,
    max_distance: float = 0.7
):

    query_embedding = get_embedding(query)

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT
            id,
            content,
            file_name,
            chunk_index,
            vector <=> %s::vector AS distance
        FROM document
        WHERE vector <=> %s::vector <= %s
        ORDER BY vector <=> %s::vector
        LIMIT %s;
        """,
        (
            query_embedding,
            query_embedding,
            max_distance,
            query_embedding,
            top_k
        )
    )

    results = cursor.fetchall()

    cursor.close()
    connection.close()

    return results