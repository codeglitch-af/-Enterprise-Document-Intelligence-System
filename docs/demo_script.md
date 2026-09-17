# 3–5 Minute Demo Video Script

## 0:00–0:30 — Problem
Explain that enterprises may have thousands of PDFs across policies, contracts, and reports, making search and analysis slow.

## 0:30–1:00 — Architecture
Show `docs/architecture.mmd` and explain:
User → Streamlit → PDF extraction/chunking → OpenAI embeddings → ChromaDB → retrieval → OpenAI LLM → cited response.

## 1:00–2:00 — Upload and RAG
1. Start `streamlit run app.py`.
2. Upload sample policy/contract/report PDFs.
3. Select the category.
4. Click **Index documents**.
5. Ask a cross-document question.
6. Show the answer and retrieved source passages.

## 2:00–3:00 — Summarization
Paste a document excerpt into the Single-Document Analyst area.
Click **Generate Summary**.
Explain how the system turns long text into an executive-oriented summary.

## 3:00–4:00 — Document Analyst
Use:
"Identify key obligations, risks, dates, and ambiguous areas."
Click **Analyze Document**.
Point out that the analyst separates facts from interpretation.

## 4:00–5:00 — Evaluation and Future Work
Mention retrieval relevance, answer faithfulness, citation correctness, latency, and summary coverage.
Close with future enhancements: OCR, RBAC, hybrid retrieval, reranking, audit logs, and automated evaluation.
