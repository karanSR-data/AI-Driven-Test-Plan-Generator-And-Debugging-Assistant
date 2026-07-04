from pathlib import Path
import os
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv(BASE_DIR / ".env")

class Config:
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")

    LLM_MODEL = os.getenv(
        "LLM_MODEL",
        "gpt-4o-mini"
    )

    EMBEDDING_MODEL = os.getenv(
        "EMBEDDING_MODEL",
        "sentence-transformers/all-MiniLM-L6-v2"
    )

    VECTOR_STORE_PATH = str(
        BASE_DIR / "data" / "vector_store"
    )

    CHUNK_SIZE = 800
    CHUNK_OVERLAP = 100
    TOP_K = 4