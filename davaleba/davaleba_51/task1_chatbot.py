import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    print("❌ GEMINI_API_KEY ვერ მოიძებნა.")
    print("გთხოვ, შექმენი .env ფაილი და დაამატე:")
    print("GEMINI_API_KEY=შენი_API_KEY")
    exit()

client = genai.Client(api_key=API_KEY)

MODEL = "gemini-2.5-flash"

SYSTEM_INSTRUCTION = """
შენ ხარ მოკლე, მეგობრული და გასაგები ასისტენტი.
უპასუხე მომხმარებელს მარტივი ენით და ეცადე, პასუხები იყოს
კონკრეტული და ადვილად გასაგები.
"""


conversation_history = []

last_response = None

print("🤖 Gemini Chatbot")
print("დაწერე 'exit' საუბრის დასასრულებლად.\n")

for i in range(4):
    user_message = input(f"👤 შენ ({i + 1}/4): ")

    if user_message.lower() == "exit":
        break


    conversation_history.append(
        types.UserContent(
            parts=[
                types.Part.from_text(text=user_message)
            ]
        )
    )

    try:

        response = client.models.generate_content(
            model=MODEL,
            contents=conversation_history,
            config=types.GenerateContentConfig(
                system_instruction=SYSTEM_INSTRUCTION
            )
        )

        print(f"🤖 Gemini: {response.text}\n")


        conversation_history.append(
            types.ModelContent(
                parts=[
                    types.Part.from_text(text=response.text)
                ]
            )
        )

        last_response = response

    except Exception as e:
        print(f"❌ API შეცდომა: {type(e).__name__}")
        print(e)
        break



if last_response and last_response.usage_metadata:
    usage = last_response.usage_metadata

    print("\n========== TOKEN USAGE ==========")
    print(f"Prompt tokens: {usage.prompt_token_count}")
    print(f"Candidate tokens: {usage.candidates_token_count}")
    print(f"Thoughts tokens: {usage.thoughts_token_count}")
    print(f"Total tokens: {usage.total_token_count}")
    print("=================================")

client.close()