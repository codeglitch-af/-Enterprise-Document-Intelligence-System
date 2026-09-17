from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from .config import CHAT_MODEL


def analyze_document(text: str, question: str) -> str:
    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "You are a document analyst. Analyze the provided enterprise document. "
                "Separate explicit facts from interpretation, flag ambiguity, and identify "
                "missing information. Do not invent clauses, dates, or obligations.",
            ),
            (
                "human",
                "Analysis request: {question}\n\nDocument:\n{text}",
            ),
        ]
    )
    chain = prompt | ChatOpenAI(model=CHAT_MODEL, temperature=0)
    response = chain.invoke({"question": question, "text": text[:50000]})
    return response.content
