import os
from config import UPLOAD_DIR
from document_loader import load_and_chunk
from vector_store import add_documents, delete_by_source, list_sources

os.makedirs(UPLOAD_DIR, exist_ok=True)


def add_file(uploaded_file):
    file_path = os.path.join(UPLOAD_DIR, uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    chunks = load_and_chunk(file_path, source_name=uploaded_file.name)
    num_added = add_documents(chunks)
    return {"file": uploaded_file.name, "chunks_added": num_added}


def delete_file(file_name: str):
    num_removed = delete_by_source(file_name)
    file_path = os.path.join(UPLOAD_DIR, file_name)
    if os.path.exists(file_path):
        os.remove(file_path)
    return {"file": file_name, "chunks_removed": num_removed}


def active_documents():
    return list_sources()