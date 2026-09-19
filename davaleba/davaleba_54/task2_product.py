import os

from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate



load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    print("❌ GEMINI_API_KEY was not found.")
    exit()




class Product(BaseModel):
    name: str
    price: float
    currency: str
    in_stock: bool
    colors: list[str]




llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=API_KEY,
    temperature=0
)




structured_llm = llm.with_structured_output(Product)




prompt = PromptTemplate.from_template(
    """
Extract the product information from the following text.

Return:
- product name
- price
- currency
- whether it is in stock
- available colors

Text:
{text}
"""
)




chain = prompt | structured_llm




text = """
The new wireless headphones cost 149.99 USD.
Available in black, white and blue.
Currently in stock.
"""



product = chain.invoke({
    "text": text
})




print("========== PRODUCT ==========")
print(f"Name: {product.name}")
print(f"Price: {product.price}")
print(f"Currency: {product.currency}")
print(f"In stock: {product.in_stock}")
print(f"Colors: {', '.join(product.colors)}")