from pathlib import Path
from typing import List
from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document 
from src.config import Config
from src.utils import get_logger

log = get_logger(__name__)

def load_document(file_path: str) -> List[Document]:
    """Load a PDF or .txt file into LangChain Documents."""
    path  = Path(file_path)
    if path.suffix.lower() == ".pdf":      #check if file is .pdf
        loader = PyPDFLoader(str(path))    #if it is  pdf then ye text ko extract kerta hai pdf se
    else:
        loader = TextLoader(str(path), encoding="utf-8")
    docs = loader.load()                   #read file
    log.info(f"Loaded {len(docs)} document(s) from {file_path}")  #writes a log message
    return docs          #return loaded document 


def chunk_documents(docs: List[Document]) -> List[Document]:
    """Split documents into semantic chunks for embedding."""
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=Config.CHUNK_SIZE,
        chunk_overlap=Config.CHUNK_OVERLAP,
        separators=["\n\n", "\n", ". ", " ", ""],
    )
    chunks = splitter.split_documents(docs)
    log.info(f"Split into {len(chunks)} chunks")
    return chunks