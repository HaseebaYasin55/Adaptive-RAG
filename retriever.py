"""
Retriever Tool
---------------
Performs semantic similarity search against the Chroma vector store
and returns the top-k relevant chunks along with retrieval latency.

Note: Chroma returns an L2 distance score by default, so a LOWER
score means a MORE relevant chunk.
"""
import time

from vector_store import get_vectorstore
from config import TOP_K


def retrieve(query: str, top_k: int = TOP_K):
    """Return top-k relevant chunks with similarity scores and elapsed time."""
    store = get_vectorstore()

    start = time.perf_counter()
    results = store.similarity_search_with_score(query, k=top_k)
    elapsed = time.perf_counter() - start

    chunks = []
    for doc, score in results:
        chunks.append({
            "content": doc.page_content,
            "source": doc.metadata.get("source", "unknown"),
            "chunk_id": doc.metadata.get("chunk_id"),
            "score": float(score),
        })
    return chunks, elapsed