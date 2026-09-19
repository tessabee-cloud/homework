import os
from dotenv import load_dotenv
from google import genai
from google.genai import errors

load_dotenv()




def test_missing_api_key():
    print("\n" + "=" * 60)
    print("1. MISSING API KEY")
    print("=" * 60)

    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        print("❌ API Key ვერ მოიძებნა.")
        print("💡 გთხოვ, შექმენი .env ფაილი და დაამატე:")
        print("GEMINI_API_KEY=შენი_API_KEY")
        return

    print("ℹ️ API Key არსებობს, ამიტომ Missing API Key შეცდომა")
    print("ამ გაშვებაზე არ გამოწვეულა.")




def test_invalid_api_key():
    print("\n" + "=" * 60)
    print("2. INVALID API KEY")
    print("=" * 60)

    try:
        fake_key = "this-is-definitely-not-a-real-api-key"

        client = genai.Client(api_key=fake_key)

        client.models.generate_content(
            model="gemini-2.5-flash",
            contents="Hello"
        )

    except errors.ClientError as e:
        print("❌ ავტორიზაციის შეცდომა.")
        print("💡 API Key არასწორია ან credentials-ის პრობლემაა.")
        print(f"Status: {e.code}")

    except Exception as e:
        print(f"❌ სხვა შეცდომა: {type(e).__name__}")
        print(e)




def test_invalid_model():
    print("\n" + "=" * 60)
    print("3. INVALID MODEL NAME")
    print("=" * 60)

    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        print("❌ API Key არ არსებობს.")
        return

    try:
        client = genai.Client(api_key=api_key)

        client.models.generate_content(
            model="gemini-this-model-does-not-exist-123",
            contents="Hello"
        )

    except errors.ClientError as e:
        print("❌ მოდელის სახელის შეცდომა.")
        print("💡 მითითებული model name არასწორია ან აღარ არსებობს.")
        print(f"Status: {e.code}")

    except Exception as e:
        print(f"❌ სხვა შეცდომა: {type(e).__name__}")
        print(e)




def test_general_error():
    print("\n" + "=" * 60)
    print("4. GENERAL API ERROR")
    print("=" * 60)

    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        print("❌ API Key არ არსებობს.")
        return

    try:
        client = genai.Client(api_key=api_key)

        # განზრახ არასწორი პარამეტრი
        client.models.generate_content(
            model="gemini-2.5-flash",
            contents="Hello",
            config={
                "invalid_parameter": True
            }
        )

    except Exception as e:
        print("❌ მოულოდნელი API შეცდომა.")
        print(f"Error type: {type(e).__name__}")
        print(f"Description: {e}")




if __name__ == "_main_":
    test_missing_api_key()
    test_invalid_api_key()
    test_invalid_model()
    test_general_error()

    print("\n✅ Error handling tests დასრულებულია.")