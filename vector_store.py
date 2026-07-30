from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from config import EMBEDDING_MODEL, CHROMA_PERSIST_DIR, COLLECTION_NAME

_embeddings = None
_vectorstore = None


def get_embeddings():
    global _embeddings
    if _embeddings is None:
        _embeddings = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL)
    return _embeddings


def get_vectorstore():
    global _vectorstore
    if _vectorstore is None:
        _vectorstore = Chroma(
            collection_name=COLLECTION_NAME,
            embedding_function=get_embeddings(),
            persist_directory=CHROMA_PERSIST_DIR,
        )
    return _vectorstore


def add_documents(chunks):
    """Embed and store a list of document chunks."""
    if not chunks:
        return 0
    store = get_vectorstore()
    ids = [f"{c.metadata['source']}_{c.metadata['chunk_id']}" for c in chunks]
    store.add_documents(chunks, ids=ids)
    return len(chunks)


def delete_by_source(source_name: str):
    """Remove all vectors/chunks belonging to a given source file (not just the UI)."""
    store = get_vectorstore()
    existing = store.get(where={"source": source_name})
    ids_to_delete = existing.get("ids", [])
    if ids_to_delete:
        store.delete(ids=ids_to_delete)
    return len(ids_to_delete)


def list_sources():
    """Return the distinct source file names currently indexed, with chunk counts."""
    store = get_vectorstore()
    data = store.get(include=["metadatas"])
    sources = {}
    for meta in data.get("metadatas", []):
        src = meta.get("source", "unknown")
        sources[src] = sources.get(src, 0) + 1
    return sources  # {filename: chunk_count}


def collection_size():
    store = get_vectorstore()
    return len(store.get(include=[]).get("ids", []))