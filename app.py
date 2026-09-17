import os
import streamlit as st

from src.document_processor import process_pdf
from src.rag_pipeline import index_documents, answer_question
from src.summary import summarize_text
from src.analyst import analyze_document


st.set_page_config(
    page_title="Enterprise Document Intelligence",
    page_icon="📄",
    layout="wide",
)

st.title("📄 Enterprise Document Intelligence System")
st.caption("RAG-powered question answering, summarization, and document analysis.")

if not os.getenv("OPENAI_API_KEY"):
    st.warning("Set OPENAI_API_KEY in a .env file before indexing or analyzing documents.")

with st.sidebar:
    st.header("Upload & Index")
    category = st.selectbox("Document category", ["Policies", "Contracts", "Reports"])
    uploaded = st.file_uploader(
        "Upload PDF documents",
        type=["pdf"],
        accept_multiple_files=True,
    )

    if st.button("Index documents", type="primary", use_container_width=True):
        if not uploaded:
            st.error("Upload at least one PDF.")
        else:
            total = 0
            with st.spinner("Extracting, chunking, embedding, and indexing..."):
                for file in uploaded:
                    chunks = process_pdf(file.getvalue(), file.name, category)
                    total += index_documents(chunks)
            st.success(f"Indexed {total} chunks from {len(uploaded)} PDF(s).")

st.subheader("Question Answering")
question = st.text_input(
    "Ask a question across the indexed enterprise documents",
    placeholder="e.g. What are the termination obligations in the contracts?",
)

if st.button("Ask", use_container_width=True) and question:
    with st.spinner("Retrieving relevant passages and generating answer..."):
        answer, sources = answer_question(question)

    st.markdown("### Answer")
    st.write(answer)

    if sources:
        st.markdown("### Retrieved Sources")
        for i, doc in enumerate(sources, start=1):
            meta = doc.metadata
            with st.expander(
                f"Source {i}: {meta.get('source')} — page {meta.get('page', '?')}"
            ):
                st.write(doc.page_content)

st.divider()
st.subheader("Single-Document Analyst")

analysis_text = st.text_area(
    "Paste document text for direct analysis",
    height=180,
    placeholder="Paste extracted document text here...",
)
analysis_question = st.text_input(
    "Analysis request",
    value="Identify key obligations, risks, dates, and ambiguous areas.",
)

col1, col2 = st.columns(2)
with col1:
    if st.button("Generate Summary") and analysis_text:
        with st.spinner("Summarizing..."):
            st.write(summarize_text(analysis_text))

with col2:
    if st.button("Analyze Document") and analysis_text:
        with st.spinner("Analyzing..."):
            st.write(analyze_document(analysis_text, analysis_question))
