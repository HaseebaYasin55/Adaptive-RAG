"""
Central configuration for the RAG Assistant.
"""
import os
from dotenv import load_dotenv

load_dotenv()

# ---------- Embeddings (HuggingFace, local, free, no API key needed) ----------
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

# ---------- LLM backend ----------
# Groq is used because it offers very fast inference and a generous free
# tier, which makes it well suited for a demo where response latency is
# itself something we want to measure and showcase.
GROQ_API_KEY = os.getenv("GROQ_API_KEY", "")
LLM_MODEL = "llama-3.3-70b-versatile"

# ---------- Vector store (Chroma) ----------
CHROMA_PERSIST_DIR = "chroma_db"
COLLECTION_NAME = "rag_knowledge_base"

# ---------- Chunking ----------
CHUNK_SIZE = 1000
CHUNK_OVERLAP = 150

# ---------- Retrieval ----------
TOP_K = 4

# ---------- Storage paths ----------
UPLOAD_DIR = "uploaded_docs"
KB_DB_PATH = "knowledge_base.sqlite3"