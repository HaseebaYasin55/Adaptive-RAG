# 📚 Adaptive RAG — Dynamic Knowledge Base with Real-Time Source Control & Performance Benchmarking

A **Retrieval-Augmented Generation (RAG) assistant** built with **Streamlit**, powered by **Groq** (LLM generation), **HuggingFace** embeddings, and **ChromaDB** (vector storage), that lets you upload documents, chat with them, and manage the knowledge base live — adding or deleting files re-indexes the vector store immediately, and every query is benchmarked for retrieval quality, latency, and faithfulness.

---

## Key Features

- **Dynamic, user-controlled knowledge base** — upload PDF, TXT, or DOCX files at any time; delete files at any time. Deleting a file removes its vectors from ChromaDB itself, not just from the UI list, so stale content is never retrieved again.
- **Grounded question answering** — the LLM is instructed to answer only from retrieved context, and to say so explicitly when the knowledge base doesn't contain the answer, rather than making information up.
- **Semantic retrieval** — top-k similarity search against ChromaDB using HuggingFace sentence embeddings, with the retrieval time and similarity scores surfaced for every answer.
- **Per-query performance benchmarking** — every question logs retrieval time, generation time, total latency, average retrieval score, and a faithfulness score.
- **Faithfulness scoring** — a lightweight lexical-overlap heuristic that estimates how much of the generated answer is actually grounded in the retrieved chunks, as a fast proxy for hallucination detection.
- **Knowledge base growth impact view** — performance is grouped by how many documents were active in the knowledge base at the time of each query, so you can see how adding or deleting files affects retrieval quality and speed over time.
- **Query history** — every question and answer is stored and browsable, separate from the live chat session.
- **Modern, custom-styled Streamlit UI** — dedicated `UI/` module for page styling and reusable UI components (headers, document cards, answer cards, empty states) instead of default Streamlit styling.
- **Persistent by default** — ChromaDB and the SQLite knowledge base both persist to disk, so documents and history survive an app restart.

---

## Project Structure

```
Adaptive-RAG/
│
├── UI/
│   ├── styles.py            # Custom CSS loaded into the Streamlit page
│   └── ui_components.py     # Reusable UI pieces: headers, document cards, answer cards, etc.
│
├── assets/                  # Static assets used by the UI (icons/images)
│
├── chroma_db/                # Persistent ChromaDB vector store (auto-generated)
│
├── app.py                    # Streamlit UI — entry point, ties every module together
├── config.py                  # Central configuration (models, chunking, paths)
├── document_loader.py          # Loads and chunks PDF / TXT / DOCX files
├── datasource_manager.py       # Add/delete files at runtime, list active documents
├── vector_store.py             # Embedding + ChromaDB indexing, deletion, listing
├── retriever.py                 # Top-k semantic similarity search
├── llm_generator.py             # Groq-backed, context-grounded answer generation
├── Knowledge_base.py            # Stores and retrieves query/answer history (SQLite)
├── performance_monitor.py        # Logs latency, retrieval score, faithfulness per query
├── database.py                   # Shared SQLite connection/schema
├── knowledge_base.sqlite3         # SQLite database (auto-generated)
├── requirements.txt
└── .gitignore
```

---

## How It Works

Adaptive RAG follows this flow:

1. **Ingest** — a file is uploaded through the sidebar. `datasource_manager.add_file()` saves it to disk, `document_loader.load_and_chunk()` extracts and splits its text into chunks, and `vector_store.add_documents()` embeds each chunk with a HuggingFace sentence-transformer and stores it in ChromaDB.
2. **Manage** — the sidebar lists every active document with its chunk count. Deleting a document calls `datasource_manager.delete_file()`, which removes the file from disk **and** removes its vectors from ChromaDB via `vector_store.delete_by_source()`, so retrieval always reflects the current document set.
3. **Ask** — a user question goes to `retriever.retrieve()`, which runs a top-k similarity search against ChromaDB and returns the most relevant chunks along with their similarity scores and the retrieval time.
4. **Generate** — `llm_generator.generate_answer()` sends the retrieved chunks and the question to Groq, instructed to answer strictly from the provided context, and returns the answer plus the generation time.
5. **Log** — `performance_monitor.log_query()` records retrieval time, generation time, total latency, average retrieval score, a faithfulness score, and how many documents were active in the knowledge base at that moment. `Knowledge_base.save_qa()` stores the question and answer for later browsing.
6. **Display** — the Streamlit UI shows the answer with live metrics, an expandable view of the exact chunks used, a documents overview tab, a performance dashboard with trend charts, and a full query history tab.

---

## Tech Stack

| Component        | Choice                                        | Why |
|-------------------|------------------------------------------------|-----|
| Vector DB          | **ChromaDB**                                    | Simple, embeddable, persistent local vector store — no external service to run. |
| Embeddings         | **HuggingFace** (`sentence-transformers/all-MiniLM-L6-v2`) | Runs locally, free, no API key required, fast, and pairs well with Chroma. |
| LLM Backend        | **Groq** (`llama-3.3-70b-versatile`)             | Very fast inference and a generous free tier — well suited to a project that measures response latency as a first-class metric. |
| Orchestration      | **LangChain** (`langchain-community`, `langchain-chroma`, `langchain-huggingface`, `langchain-groq`) | Provides ready-made document loaders, text splitters, and vector store / LLM integrations. |
| UI                 | **Streamlit**, with a custom `UI/` styling module | Fast to build a chat + document management + dashboard interface, with a more polished look than Streamlit's defaults. |
| Storage            | **SQLite**                                       | Lightweight, file-based persistence for query history and performance logs. |
| Language           | **Python**                                       | |

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/HaseebaYasin55/Adaptive-RAG.git
```

### 2. Move into the project folder

```bash
cd Adaptive-RAG
```

### 3. Open the project in VS Code

```bash
code .
```

### 4. Install all dependencies

Open the terminal inside VS Code and run:

```bash
pip install -r requirements.txt
```

### 5. Create a `.env` file

Inside the project folder, create a file named:

```
.env
```

Add your API key:

```
GROQ_API_KEY=your_groq_api_key_here
```

Get a free key here: **Groq** — <https://console.groq.com/keys>

---

## Run the Application

Launch the app using Streamlit:

```bash
streamlit run app.py
```

This opens at `http://localhost:8501`.

## How to Use the App

1. **Upload documents** — in the sidebar, use the file uploader to add one or more PDF, TXT, or DOCX files, then click **Add to Knowledge Base**. Each file is chunked and indexed into ChromaDB.
2. **Check active documents** — still in the sidebar, every indexed document is listed with its chunk count. Click 🗑️ next to a document to delete it — this removes it from disk and wipes its vectors from ChromaDB.
3. **Ask questions** — go to the **💬 Chat** tab, type a question, and click **Get Answer**. The assistant retrieves the most relevant chunks and answers strictly from them, showing retrieval time, generation time, retrieval score, and a faithfulness score alongside the answer. Expand **📑 Retrieved Context Used** to see exactly which chunks informed the answer.
4. **Review the knowledge base** — the **📄 Documents** tab shows every indexed document and the total chunk count across the whole knowledge base.
5. **Check performance** — the **📊 Dashboard** tab shows aggregate metrics (total queries, average latency, average retrieval time, average generation time, average faithfulness), trend charts of latency and retrieval quality over time, and a table grouping performance by how many documents were active in the knowledge base at query time — useful for seeing how growing or shrinking the knowledge base affects speed and quality.
6. **Browse history** — the **🕘 History** tab lists every past question and answer.

---

## Notes on the Metrics

- **Retrieval score**: ChromaDB's default distance metric (L2) — a **lower** score means the chunk is **more** similar to the query.
- **Faithfulness score**: a lightweight lexical-overlap heuristic measuring what fraction of the meaningful words in the answer also appear in the retrieved context. It's a fast, dependency-free proxy for hallucination detection — closer to 1.0 means the answer stayed close to the retrieved context.
- **Active document count**: recorded per query so the dashboard can show how retrieval quality and latency change as documents are added to or removed from the knowledge base.

---

## Notes & Limitations

- Requires a valid `GROQ_API_KEY` — the app raises a clear error if it's missing.
- The faithfulness score is a lexical heuristic, not an LLM-graded judgment, so it's best read as a directional signal rather than an exact hallucination rate.
- ChromaDB and the SQLite knowledge base persist locally on disk (`chroma_db/`, `knowledge_base.sqlite3`); there is no multi-user isolation — all uploaded documents and history are shared across whoever uses the running app.
- Very large PDFs will take longer to embed and index the first time they're uploaded, since embedding runs locally on CPU by default.

---

# Live Demo

You can try the deployed application here: [RAG Knowledge Assistant](https://adaptive-rag-11.streamlit.app/)

 ---

## 💡 Future Improvements

- Support for additional vector databases (Pinecone, Qdrant, LanceDB) as swappable providers
- LLM-graded faithfulness/relevance scoring as an alternative to the lexical heuristic
- Per-user or per-session document isolation
- Support for website/URL ingestion in addition to file uploads
- Exportable performance reports (CSV/PDF) from the dashboard

---

## 👩‍💻 Author

**Haseeba Yasin**

If you found this project helpful, feel free to ⭐ the repository.
