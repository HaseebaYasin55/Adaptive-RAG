"""
Shared SQLite connection used by the Knowledge Base and Performance
Monitor tools.
"""
import sqlite3

from config import KB_DB_PATH


def get_connection():
    conn = sqlite3.connect(KB_DB_PATH, check_same_thread=False)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS qa_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            query TEXT,
            answer TEXT
        )
    """)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS performance_log (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            query TEXT,
            retrieval_time REAL,
            generation_time REAL,
            total_latency REAL,
            avg_retrieval_score REAL,
            num_chunks_retrieved INTEGER,
            faithfulness_score REAL,
            active_doc_count INTEGER
        )
    """)
    conn.commit()
    return conn