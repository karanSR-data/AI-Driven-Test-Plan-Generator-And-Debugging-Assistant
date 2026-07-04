from langchain_community.vectorstores import FAISS
from src.embeddings import get_embedding_model
from src.config import Config

import os

def build_vector_store(chunks):

    embedding_model = get_embedding_model()

    vector_store = FAISS.from_documents(
        chunks,
        embedding_model
    )

    os.makedirs(
        Config.VECTOR_STORE_PATH,
        exist_ok=True
    )

    vector_store.save_local(
        Config.VECTOR_STORE_PATH
    )

    print(f"Vector store saved to {Config.VECTOR_STORE_PATH}")

    return vector_store

# def build_vector_store(chunks):
#     """Embed document chunks and save FAISS index to disk.
    
#     Args:
#         chunks: List of LangChain Document objects (from ingestion.py)
    
#     Returns:
#         FAISS vector store object (also saved to disk)"""
    
#     embedding_model = get_embedding_model()

#     vector_store = FAISS.from_documents(chunks, embedding_model)

#     vector_store.save_local(Config.VECTOR_STORE_PATH)
#     print(f"Vector store saved to {Config.VECTOR_STORE_PATH}")
    
#     return vector_store

def load_vector_store():

    import os

    print("=" * 60)
    print("CURRENT WORKING DIRECTORY:", os.getcwd())
    print("VECTOR_STORE_PATH:", Config.VECTOR_STORE_PATH)
    print("ABSOLUTE PATH:", os.path.abspath(Config.VECTOR_STORE_PATH))
    print("PATH EXISTS:", os.path.exists(Config.VECTOR_STORE_PATH))
    print("=" * 60)

    embedding_model = get_embedding_model()

    vector_store = FAISS.load_local(
        Config.VECTOR_STORE_PATH,
        embedding_model,
        allow_dangerous_deserialization=True
    )

    print(f"Vector store loaded from {Config.VECTOR_STORE_PATH}")

    return vector_store

def get_retriever(k=None):
    k = k or Config.TOP_K

    vector_store = load_vector_store()

    retriever  = vector_store.as_retriever(search_kwargs={"k":k})

    return retriever

# if __name__ == "__main__":
#     from ingestion import ingest

#     print("Building vector store from sample spec...\n")

#     chunks = ingest("data/sample_specs")
#     print(f"Got {len(chunks)} chunks from ingestion\n")

#     vs = build_vector_store(chunks)
#     print(f"Indexed {vs.index.ntotal}vectors in {vs.index.d}--dim space\n")

#     print("="*60)
#     print("Testing retrival...")
#     print("="*60)

#     retriever = get_retriever(k=2)

#     test_queries = [
#         "What is the clock jitter spec?",
#         "What FPGA does the board use?",
#         "Common failure modes for the DAC?",
#     ]
    
#     for query in test_queries:
#         print(f"\n Query: {query}")
#         results = retriever.invoke(query)
#         for i, r in enumerate(results,1):
#             print(f"\n  ---Result{i} ---")
#             print(f"{r.page_content[:200]}...")
#         print()

