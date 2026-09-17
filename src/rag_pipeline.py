from langchain_chroma import Chroma
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.documents import Document

from .config import CHROMA_DIR, CHAT_MODEL, EMBEDDING_MODEL, TOP_K


def get_embeddings():
    return OpenAIEmbeddings(model=EMBEDDING_MODEL)


def get_vectorstore():
    return Chroma(
        collection_name="enterprise_documents",
        embedding_function=get_embeddings(),
        persist_directory=CHROMA_DIR,
    )


def index_documents(documents: list[Document]) -> int:
    if not documents:
        return 0
    vectorstore = get_vectorstore()
    vectorstore.add_documents(documents)
    return len(documents)


def retrieve(question: str, k: int = TOP_K) -> list[Document]:
    return get_vectorstore().similarity_search(question, k=k)


def answer_question(question: str, k: int = TOP_K) -> tuple[str, list[Document]]:
    docs = retrieve(question, k=k)

    if not docs:
        return "No indexed documents were found. Upload and index PDFs first.", []

    context_parts = []
    for i, doc in enumerate(docs, start=1):
        meta = doc.metadata
        context_parts.append(
            f"[Source {i}: {meta.get('source', 'unknown')}, "
            f"page {meta.get('page', '?')}, category {meta.get('category', 'unknown')}]\n"
            f"{doc.page_content}"
        )

    context = "\n\n".join(context_parts)

    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "You are an enterprise document analyst. Answer only from the supplied context. "
                "If the context does not support an answer, say so. Cite sources inline as "
                "[Source N]. Be concise but precise.",
            ),
            ("human", "Question: {question}\n\nContext:\n{context}"),
        ]
    )

    chain = prompt | ChatOpenAI(model=CHAT_MODEL, temperature=0)
    response = chain.invoke({"question": question, "context": context})
    return response.content, docs
