import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    print("❌ GEMINI_API_KEY ვერ მოიძებნა.")
    print("გთხოვ, დაამატე API key .env ფაილში.")
    exit()

client = genai.Client(api_key=API_KEY)

MODEL = "gemini-2.5-flash"

QUESTION = "შემიძლია თუ არა თანხის დაბრუნება, თუ უბრალოდ აზრი შევიცვალე?"

instructions = {
    "FORMAL": """
შენ ხარ პროფესიონალი და ზუსტი ასისტენტი.
უპასუხე ოფიციალური, ფრთხილი და პროფესიონალური ტონით.
არ გააკეთო დაუდასტურებელი იურიდიული დასკვნები.
""",

    "FRIENDLY": """
შენ ხარ თბილი და მეგობრული ასისტენტი.
უპასუხე მარტივი და გასაგები ენით, თითქოს მეგობარს უხსნი.
""",

    "HUMOROUS": """
შენ ხარ მსუბუქად იუმორისტული და ირონიული ასისტენტი.
უპასუხე მეგობრულად და გამოიყენე მსუბუქი იუმორი,
მაგრამ პასუხი მაინც უნდა იყოს ინფორმაციულად სწორი.
"""
}

for name, instruction in instructions.items():
    print("\n" + "=" * 60)
    print(f"📝 {name}")
    print("=" * 60)

    try:
        response = client.models.generate_content(
            model=MODEL,
            contents=QUESTION,
            config=types.GenerateContentConfig(
                system_instruction=instruction,
                temperature=0.7
            )
        )

        print(response.text)

    except Exception as e:
        print(f"❌ შეცდომა: {type(e).__name__}")
        print(e)

client.close()