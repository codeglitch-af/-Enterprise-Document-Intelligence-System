# Enterprise Document Intelligence System

A Python + LangChain + OpenAI RAG application for searching, summarizing, and analyzing large collections of enterprise PDFs.

## Problem
Organizations may have thousands of policies, contracts, and reports. Finding reliable answers across these documents is slow and manual.

## Features
- PDF upload and text extraction
- Chunking and persistent vector indexing with ChromaDB
- RAG question answering with source citations
- Document summarization
- Document analyst workflow
- Automatic executive-summary generation
- Streamlit web interface
- Architecture diagram and project report

## Tech Stack
### Mandatory
- Python
- OpenAI API (chat + embeddings)
- LangChain

### Optional
- ChromaDB
- Streamlit

## Project Structure
```text
enterprise_document_intelligence/
├── app.py
├── requirements.txt
├── .env.example
├── README.md
├── src/
│   ├── __init__.py
│   ├── config.py
│   ├── document_processor.py
│   ├── rag_pipeline.py
│   ├── analyst.py
│   └── summary.py
├── data/
│   ├── policies/
│   ├── contracts/
│   └── reports/
├── docs/
│   ├── architecture.mmd
│   └── demo_script.md
└── report/
    └── Project_Report.pdf
```

## Setup

1. Create a virtual environment:
```bash
python -m venv .venv
```

2. Activate it:
- Windows: `.venv\Scripts\activate`
- macOS/Linux: `source .venv/bin/activate`

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create `.env` from `.env.example` and add your OpenAI API key.

5. Run:
```bash
streamlit run app.py
```

## Usage
1. Open the Streamlit URL.
2. Upload one or more PDFs.
3. Choose a category: Policies, Contracts, or Reports.
4. Click **Index documents**.
5. Ask a question such as:
   - "What is the employee leave approval process?"
   - "Summarize the termination obligations."
   - "What risks are mentioned in the reports?"
6. Review the generated answer and source documents.
7. Use the summarization/analyst controls for a selected document.

## Environment Variables
```text
OPENAI_API_KEY=your_key_here
OPENAI_CHAT_MODEL=gpt-4o-mini
OPENAI_EMBEDDING_MODEL=text-embedding-3-small
CHROMA_DIR=./chroma_db
```

## Notes
- The application uses local Chroma persistence by default.
- PDF extraction quality depends on the source PDF. Scanned PDFs require OCR, which is not included in this baseline.
- Do not upload confidential documents to an external model unless your organization's security and data-processing policies permit it.
- For production, add authentication, access control, encryption, audit logs, metadata filters, document-level permissions, and evaluation monitoring.

## Demo
See `docs/demo_script.md` for a 3–5 minute demonstration script.

## Architecture
The architecture source is in `docs/architecture.mmd`. It can be rendered with Mermaid-compatible tooling.

## Evaluation
Suggested evaluation dimensions:
- Retrieval relevance
- Answer faithfulness
- Citation correctness
- Latency
- Summarization coverage
- Performance across document types

## Future Enhancements
- OCR for scanned PDFs
- Enterprise SSO/RBAC
- Hybrid BM25 + vector retrieval
- Reranking
- Document versioning
- PII redaction
- Human feedback loop
- Batch executive-summary generation
- Observability and automated RAG evaluation
