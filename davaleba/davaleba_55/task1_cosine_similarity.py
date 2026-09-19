import os

from dotenv import load_dotenv
from google import genai


load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    print("GEMINI_API_KEY was not found.")
    exit()


client = genai.Client(api_key=API_KEY)

MODEL = "gemini-embedding-001"


def get_embedding(text):
    response = client.models.embed_content(
        model=MODEL,
        contents=text
    )

    return response.embeddings[0].values


def cosine_similarity(vector_a, vector_b):
    dot_product = sum(a * b for a, b in zip(vector_a, vector_b))

    magnitude_a = sum(a * a for a in vector_a) ** 0.5
    magnitude_b = sum(b * b for b in vector_b) ** 0.5

    if magnitude_a == 0 or magnitude_b == 0:
        return 0.0

    return dot_product / (magnitude_a * magnitude_b)


pairs = [
    (
        "A small dog running in the park",
        "A puppy playing outside"
    ),
    (
        "A small dog running in the park",
        "A new laptop with a fast processor"
    ),
    (
        "I love programming in Python",
        "Python is a great programming language"
    ),
    (
        "I love programming in Python",
        "The capital of France is Paris"
    )
]


for i, (text1, text2) in enumerate(pairs, start=1):

    embedding1 = get_embedding(text1)
    embedding2 = get_embedding(text2)

    similarity = cosine_similarity(
        embedding1,
        embedding2
    )

    print(f"{i}. {similarity:.4f}")


client.close()