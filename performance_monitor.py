"""
Performance Monitor Tool
---------------------------
Logs retrieval quality, latency (embedding + retrieval + generation),
and a lightweight faithfulness score for every query. Also provides
aggregated data for the Streamlit performance dashboard, including
before/after comparisons as the knowledge base changes size.
"""
import re
from datetime import datetime

import pandas as pd

from database import get_connection


def _faithfulness_score(answer: str, retrieved_chunks: list) -> float:
    """
    Lightweight lexical-overlap heuristic: the fraction of meaningful
    words in the answer that also appear in the retrieved context.
    Closer to 1.0 = well grounded in the retrieved context.
    Closer to 0.0 = more likely to contain hallucinated content.
    """
    context_text = " ".join(c["content"] for c in retrieved_chunks).lower()
    context_words = set(re.findall(r"[a-z0-9]+", context_text))

    answer_words = re.findall(r"[a-z0-9]+", answer.lower())
    stopwords = {
        "the", "a", "an", "is", "are", "of", "to", "in", "and", "it", "that",
        "this", "was", "for", "on", "with", "as", "be", "by", "or", "i",
        "you", "your", "do", "not", "have", "information", "knowledge",
        "base", "answer", "question", "enough",
    }
    meaningful = [w for w in answer_words if w not in stopwords and len(w) > 2]

    if not meaningful:
        return 1.0
    overlap = sum(1 for w in meaningful if w in context_words)
    return round(overlap / len(meaningful), 3)


def log_query(query, answer, retrieved_chunks, retrieval_time, generation_time, active_doc_count):
    """Record retrieval + generation metrics for one query."""
    avg_score = (
        sum(c["score"] for c in retrieved_chunks) / len(retrieved_chunks)
        if retrieved_chunks else 0.0
    )
    faithfulness = _faithfulness_score(answer, retrieved_chunks)
    total_latency = retrieval_time + generation_time

    conn = get_connection()
    conn.execute(
        """INSERT INTO performance_log
           (timestamp, query, retrieval_time, generation_time, total_latency,
            avg_retrieval_score, num_chunks_retrieved, faithfulness_score, active_doc_count)
           VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""",
        (
            datetime.now().isoformat(timespec="seconds"), query, retrieval_time,
            generation_time, total_latency, avg_score, len(retrieved_chunks),
            faithfulness, active_doc_count,
        ),
    )
    conn.commit()

    return {
        "avg_retrieval_score": avg_score,
        "faithfulness_score": faithfulness,
        "total_latency": total_latency,
    }


def get_logs(limit: int = 200) -> pd.DataFrame:
    conn = get_connection()
    df = pd.read_sql_query(
        "SELECT * FROM performance_log ORDER BY id DESC LIMIT ?",
        conn,
        params=(limit,),
    )
    return df


def summary():
    df = get_logs(limit=1_000_000)
    if df.empty:
        return None
    return {
        "total_queries": len(df),
        "avg_total_latency": round(df["total_latency"].mean(), 3),
        "avg_retrieval_time": round(df["retrieval_time"].mean(), 3),
        "avg_generation_time": round(df["generation_time"].mean(), 3),
        "avg_retrieval_score": round(df["avg_retrieval_score"].mean(), 3),
        "avg_faithfulness": round(df["faithfulness_score"].mean(), 3),
    }