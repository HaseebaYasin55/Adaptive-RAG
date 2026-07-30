"""
Knowledge Base
----------------
Stores past user queries and assistant responses for reference, and
provides simple stats for the Streamlit UI.
"""
from datetime import datetime

import pandas as pd

from database import get_connection


def save_qa(query: str, answer: str):
    conn = get_connection()
    conn.execute(
        "INSERT INTO qa_history (timestamp, query, answer) VALUES (?, ?, ?)",
        (datetime.now().isoformat(timespec="seconds"), query, answer),
    )
    conn.commit()


def get_history(limit: int = 50) -> pd.DataFrame:
    conn = get_connection()
    df = pd.read_sql_query(
        "SELECT timestamp, query, answer FROM qa_history ORDER BY id DESC LIMIT ?",
        conn,
        params=(limit,),
    )
    return df


def stats():
    df = get_history(limit=1_000_000)
    return {"total_queries": len(df)}