from io import BytesIO
from pathlib import Path
from typing import Iterable
from pypdf import PdfReader
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter

from .config import CHUNK_OVERLAP, CHUNK_SIZE


def extract_pdf_text(file_bytes: bytes) -> list[Document]:
    reader = PdfReader(BytesIO(file_bytes))
    documents = []

    for page_number, page in enumerate(reader.pages, start=1):
        text = (page.extract_text() or "").strip()
        if text:
            documents.append(
                Document(
                    page_content=text,
                    metadata={"page": page_number},
                )
            )
    return documents


def split_documents(documents: Iterable[Document], source_name: str, category: str) -> list[Document]:
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP,
        separators=["\n\n", "\n", ". ", " ", ""],
    )

    chunks = splitter.split_documents(list(documents))
    for index, chunk in enumerate(chunks):
        chunk.metadata.update(
            {
                "source": source_name,
                "category": category,
                "chunk_id": index,
            }
        )
    return chunks


def process_pdf(file_bytes: bytes, source_name: str, category: str) -> list[Document]:
    pages = extract_pdf_text(file_bytes)
    return split_documents(pages, source_name, category)
