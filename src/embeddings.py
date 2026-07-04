from langchain_huggingface import HuggingFaceEmbeddings
from src.config import Config

def get_embedding_model():
    """Returns a sentence-transformers embedding model (runs locally, free)."""
    return HuggingFaceEmbeddings(
        model_name=Config.EMBEDDING_MODEL,
        model_kwargs={"device": "cpu"},
        encode_kwargs={"normalize_embeddings": True},
    )

if __name__ == "__main__":
    model = get_embedding_model()
    vec = model.embed_query("voltage regulator failure")
    print(f"Vector length: {len(vec)}")
    print(f"First 5 values: {vec[:5]}")
    print(f"Vector norm: {sum(x*x for x in vec) ** 0.5:.4f}")