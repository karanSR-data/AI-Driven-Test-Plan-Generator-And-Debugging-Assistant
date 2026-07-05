# 🚀 AI-Powered Test Plan Generator & Debug Assistant

> An end-to-end Retrieval-Augmented Generation (RAG) application that automates software test plan generation and provides AI-assisted code debugging using Large Language Models (LLMs), semantic search, and vector databases.

---

## 📌 Overview

Software testing and debugging are two of the most time-consuming phases of the Software Development Life Cycle (SDLC). Writing comprehensive test plans manually requires domain expertise, while debugging often involves searching through documentation, understanding error messages, and identifying the root cause.

This project leverages **Retrieval-Augmented Generation (RAG)** to build an intelligent assistant capable of:

- 📄 Generating structured software test plans from requirement specifications.
- 🐞 Assisting developers in debugging code by analyzing errors and providing detailed explanations.
- 🔍 Retrieving relevant contextual information using semantic similarity search before generating responses.
- 🤖 Producing context-aware, structured, and professional outputs using a Large Language Model.

Instead of relying solely on the LLM's pre-trained knowledge, the system retrieves relevant information from a custom knowledge base, improving both accuracy and relevance.

---

# 🎯 Objectives

The primary objectives of this project are:

- Automate software test plan generation.
- Reduce manual effort during software testing.
- Provide intelligent debugging assistance.
- Demonstrate an end-to-end RAG pipeline.
- Learn and implement modern Generative AI technologies.
- Build an industry-level AI application suitable for real-world workflows.

---

# ✨ Features

## 📄 AI Test Plan Generation

Generate professional software test plans from requirement documents including:

- Functional Test Cases
- Boundary Test Cases
- Negative Test Cases
- Security Test Cases
- Performance Test Cases

Each generated test case includes:

- Test ID
- Scenario
- Preconditions
- Test Steps
- Expected Result
- Priority

---

## 🐞 AI Debug Assistant

Analyze source code and runtime errors to generate:

- Root Cause Analysis
- Detailed Explanation
- Corrected Code
- Best Practices
- Prevention Tips

---

## 📚 Retrieval-Augmented Generation (RAG)

Instead of directly querying the LLM, the system:

- Processes requirement documents
- Splits them into chunks
- Generates semantic embeddings
- Stores vectors in FAISS
- Retrieves only the most relevant context
- Sends retrieved context to the LLM

This significantly improves response quality while reducing unnecessary token usage.

---

## 💻 Interactive Web Application

Built using Streamlit with an easy-to-use interface supporting:

- Test Plan Generation
- Debug Assistance
- Clean UI
- Fast AI Responses

---

# 🏗️ System Architecture

```
                    Requirement Documents
                             │
                             ▼
                     Document Ingestion
                             │
                             ▼
                    Text Chunking
                             │
                             ▼
              Sentence Transformer Embeddings
                             │
                             ▼
                   FAISS Vector Database
                             │
────────────────────────────────────────────────────
                             │
                       User Query
                             │
                             ▼
                 Semantic Similarity Search
                             │
                             ▼
                 Top Relevant Document Chunks
                             │
                             ▼
                   Prompt Engineering
                             │
                             ▼
                Groq Llama 3.3 Large Language Model
                             │
                             ▼
                    Structured AI Response
```

---

# 🔄 Project Workflow

## Phase 1 — Knowledge Base Creation

```
Requirement Documents
        ↓
Load Documents
        ↓
Chunk Documents
        ↓
Generate Embeddings
        ↓
Store in FAISS Vector Database
```

This step runs only once (or whenever new documents are added).

---

## Phase 2 — User Query Processing

```
User Requirement / Error
        ↓
Retriever
        ↓
Semantic Search
        ↓
Relevant Context
        ↓
Prompt Template
        ↓
Groq LLM
        ↓
Final Response
```

---

# 📂 Project Structure

```
AI-Driven-Test-Plan-Generator-And-Debugging-Assistant/
│
├── data/
│   ├── sample_specs/
│   └── vector_store/
│
├── notebooks/
│
├── src/
│   ├── config.py
│   ├── embeddings.py
│   ├── ingestion.py
│   ├── llm_client.py
│   ├── prompts.py
│   ├── rag_chain.py
│   ├── utils.py
│   └── vectorstore.py
│
├── testpilot/
│   └── app.py
│
├── tests/
│
├── build_index.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

# ⚙️ Technology Stack

## Programming Language

- Python 3.11

## Large Language Model

- Groq API
- Llama 3.3 70B Versatile

## AI Framework

- LangChain

## Vector Database

- FAISS

## Embedding Model

- Sentence Transformers
- all-MiniLM-L6-v2 (384-dimensional embeddings)

## Frontend

- Streamlit

## Document Processing

- LangChain Document Loaders

## Environment Management

- python-dotenv

## Version Control

- Git
- GitHub

---

# 🧠 Core AI Concepts Implemented

- Retrieval-Augmented Generation (RAG)
- Semantic Search
- Dense Vector Embeddings
- Vector Databases
- Similarity Search
- Prompt Engineering
- Context Injection
- Document Chunking
- Information Retrieval
- Large Language Models (LLMs)

---

# 📈 End-to-End Pipeline

```
Documents
      │
      ▼
Ingestion
      │
      ▼
Chunking
      │
      ▼
Embeddings
      │
      ▼
FAISS
      │
      ▼
Retriever
      │
      ▼
Relevant Context
      │
      ▼
Prompt Template
      │
      ▼
Groq LLM
      │
      ▼
Generated Test Plan / Debug Report
```

---

# 🚀 Installation

Clone the repository

```bash
git clone https://github.com/karanSR-data/AI-Driven-Test-Plan-Generator-And-Debugging-Assistant.git
```

Move into the project

```bash
cd AI-Driven-Test-Plan-Generator-And-Debugging-Assistant
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env` file

```
GROQ_API_KEY=your_api_key
```

Build the FAISS index

```bash
python build_index.py
```

Run the application

```bash
streamlit run testpilot/app.py
```

---

# 📸 Screenshots
<img width="1848" height="831" alt="image" src="https://github.com/user-attachments/assets/c39144e3-8d9d-4895-ad05-70e6b226a08c" />
<img width="1854" height="612" alt="image" src="https://github.com/user-attachments/assets/48f72fef-4ffa-4f3c-9ef1-4966099f1109" />
<img width="1846" height="904" alt="image" src="https://github.com/user-attachments/assets/f8df056f-1df9-4431-a727-45c95cabe09c" />




---

# 🔮 Future Enhancements

- PDF Upload Support
- Automatic Vector Store Update
- Multi-Document Retrieval
- Chat Memory
- Export Test Plans to PDF
- Export Reports to Excel
- Authentication
- Docker Deployment
- Cloud Deployment
- Multi-LLM Support
- Source Citation Viewer
- Retrieval Confidence Score

---

# 🎯 Learning Outcomes

This project demonstrates practical implementation of:

- Retrieval-Augmented Generation (RAG)
- LangChain Framework
- Vector Databases (FAISS)
- Semantic Search
- Embedding Models
- Prompt Engineering
- LLM Integration
- Streamlit Deployment
- AI-powered Software Engineering Tools

---

# 👨‍💻 Author

**Karan Singh Rajput**

Integrated M.Tech – Computational Data Science  
VIT Bhopal University

---

# ⭐ If you found this project useful, consider giving it a star!
