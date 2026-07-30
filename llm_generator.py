import time
from langchain_groq import ChatGroq
from config import GROQ_API_KEY, LLM_MODEL

_llm = None

SYSTEM_PROMPT = (
    "You are a helpful assistant that answers questions using ONLY the "
    "context provided below. If the answer is not contained in the context, "
    "say you don't have enough information in the knowledge base to answer. "
    "Do not make up information that is not present in the context."
)

def get_llm():
    global _llm
    if _llm is None:
        if not GROQ_API_KEY:
            raise ValueError("GROQ_API_KEY is not set. Add it to your .env file.")
        _llm = ChatGroq(api_key=GROQ_API_KEY, model=LLM_MODEL, temperature=0.2)
    return _llm


def generate_answer(query: str, retrieved_chunks: list):
    if retrieved_chunks:
        context = "\n\n".join(
            f"[Source: {c['source']}]\n{c['content']}" for c in retrieved_chunks
        )
    else:
        context = "No relevant context was found in the knowledge base."

    prompt = f"{SYSTEM_PROMPT}\n\nContext:\n{context}\n\nQuestion: {query}\nAnswer:"

    llm = get_llm()
    start = time.perf_counter()
    response = llm.invoke(prompt)
    elapsed = time.perf_counter() - start

    return response.content, elapsed