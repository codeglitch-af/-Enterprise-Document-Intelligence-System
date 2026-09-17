from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from .config import CHAT_MODEL


def summarize_text(text: str, style: str = "executive") -> str:
    if style == "executive":
        instruction = (
            "Create an executive summary with: purpose, key points, risks/obligations, "
            "important dates or numbers, and recommended follow-up questions."
        )
    else:
        instruction = "Create a concise structured summary with headings and bullet points."

    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "You summarize enterprise documents accurately. Do not invent facts. "
                + instruction,
            ),
            ("human", "{text}"),
        ]
    )
    chain = prompt | ChatOpenAI(model=CHAT_MODEL, temperature=0)
    response = chain.invoke({"text": text[:50000]})
    return response.content
