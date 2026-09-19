import os

from dotenv import load_dotenv
from google import genai
from google.genai import types


load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")


if not API_KEY:
    print("❌ GEMINI_API_KEY was not found.")
    print("Please add it to your .env file.")
    exit()


client = genai.Client(api_key=API_KEY)

MODEL = "gemini-2.5-flash"




history = []

for i in range(10):

    user_message = f"User question number {i + 1}: Tell me something interesting about Python."

    model_message = (
        f"Model answer number {i + 1}: "
        f"Python is a popular programming language."
    )

    history.append(
        types.UserContent(
            parts=[
                types.Part.from_text(text=user_message)
            ]
        )
    )

    history.append(
        types.ModelContent(
            parts=[
                types.Part.from_text(text=model_message)
            ]
        )
    )


print("========== ORIGINAL HISTORY ==========")
print(f"Number of messages: {len(history)}")




def trim_history(history: list, max_turns: int):
    """
    Keeps only the last max_turns messages from history.
    """

    return history[-max_turns:]




def count_history_tokens(history):
    """
    Counts tokens in a conversation history.
    """

    response = client.models.count_tokens(
        model=MODEL,
        contents=history
    )

    return response.total_tokens




full_tokens = count_history_tokens(history)

print(f"Full history tokens: {full_tokens}")




history_4 = trim_history(history, 4)

tokens_4 = count_history_tokens(history_4)

print("\n========== MAX TURNS = 4 ==========")
print(f"Messages remaining: {len(history_4)}")
print(f"Tokens: {tokens_4}")




history_6 = trim_history(history, 6)

tokens_6 = count_history_tokens(history_6)

print("\n========== MAX TURNS = 6 ==========")
print(f"Messages remaining: {len(history_6)}")
print(f"Tokens: {tokens_6}")




history_10 = trim_history(history, 10)

tokens_10 = count_history_tokens(history_10)

print("\n========== MAX TURNS = 10 ==========")
print(f"Messages remaining: {len(history_10)}")
print(f"Tokens: {tokens_10}")


client.close()