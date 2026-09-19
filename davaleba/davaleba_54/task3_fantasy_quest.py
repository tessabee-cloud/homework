import os

from dotenv import load_dotenv
from pydantic import BaseModel, Field
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage



load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    print("❌ GEMINI_API_KEY was not found.")
    exit()




class FantasyQuest(BaseModel):
    quest_name: str
    hero_name: str
    enemy: str
    magical_item: str
    danger_level: int = Field(ge=1, le=10)
    reward: str
    side_quests: list[str]
    is_cursed: bool




llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=API_KEY,
    temperature=0.7
)




structured_llm = llm.with_structured_output(FantasyQuest)




system_message = SystemMessage(
    content="""
You are an epic fantasy storyteller.

Transform the user's text into a structured fantasy quest.

Your writing should be maximally epic, magical and imaginative.

If some information is missing from the text, invent a logical
and interesting detail yourself. However, always return a
complete and correctly structured FantasyQuest object.

The danger_level must always be an integer from 1 to 10.

Choose the danger_level realistically based on the enemies,
journey, magical dangers and other information in the story.

Do not make the danger level unnecessarily high just to make
the story sound more dramatic.
"""
)




prompt = ChatPromptTemplate.from_messages([
    system_message,
    (
        "human",
        """
Create an epic fantasy quest from the following text:

{text}
"""
    )
])




chain = prompt | structured_llm




text = """
ახალგაზრდა ჯადოქარი სახელად ლირა უნდა გაემგზავროს
ჩრდილოეთის ტყეებში, რათა იპოვოს დაკარგული მთვარის ხმალი.
გზად მას ელოდება უძველესი ტყის სული, რომელიც სძულს ადამიანებს.
თუ წარმატებას მიაღწევს, მიიღებს უკვდავების ელექსირს.
"""




quest = chain.invoke({
    "text": text
})



print("========== FANTASY QUEST ==========")
print(quest)