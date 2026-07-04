from pathlib import Path
from src.ingestion import load_document, chunk_documents
from src.vectorstore import build_vector_store

all_chunks = []

spec_folder = Path("data/sample_specs")

for file in spec_folder.glob("*"):
    docs = load_document(str(file))
    chunks = chunk_documents(docs)
    all_chunks.extend(chunks)

print(f"Total chunks: {len(all_chunks)}")

build_vector_store(all_chunks)

print("Vector store built successfully!")