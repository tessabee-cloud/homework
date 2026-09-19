import os

from dotenv import load_dotenv
from google import genai



load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")



if not API_KEY:
    print("❌ GEMINI_API_KEY was not found.")
    print("Please add it to your .env file.")
    exit()



client = genai.Client(api_key=API_KEY)

MODEL = "gemini-2.5-flash"


def count_text_tokens(text):
    """
    Counts how many tokens are contained in the given text.
    """

    response = client.models.count_tokens(
        model=MODEL,
        contents=text
    )

    return response.total_tokens


def check_token_count(text):
    """
    Counts tokens and checks whether the text is within
    the allowed 300-token limit.
    """

    token_count = count_text_tokens(text)

    print(f"\nText: {text}")
    print(f"Token count: {token_count}")

    if token_count == 0:
        print("⚠️ The text contains 0 tokens.")

    elif token_count > 300:
        print("⚠️ Warning: the text contains more than 300 tokens.")

    else:
        print("✅ The text size is within the allowed limit.")




short_text = "Hello! How are you?"

check_token_count(short_text)




medium_text = """
Python is a popular programming language.
It is widely used for web development,
data analysis, artificial intelligence,
automation and many other tasks.
"""

check_token_count(medium_text)




long_text = """
Python is a powerful and versatile programming language.
It is used by developers, scientists, engineers and students
around the world. Python has a simple syntax, which makes it
relatively easy for beginners to learn. At the same time,
it provides many advanced features for experienced developers.

Python can be used to create websites, APIs, desktop
applications, automation scripts, data analysis programs
and artificial intelligence applications. Libraries such as
FastAPI, SQLAlchemy, Pandas and NumPy make Python useful
for many different types of projects.

One of the reasons Python is popular is its large ecosystem
of libraries and frameworks. Developers can install these
packages and use existing functionality instead of creating
everything from the beginning.

Python is also commonly used when working with machine
learning and large language models. Developers can connect
their applications to external APIs and build chatbots,
recommendation systems and other intelligent applications.
"""

check_token_count(long_text)



client.close()