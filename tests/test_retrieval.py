from src.vectorstore import get_retriever

retriever = get_retriever(k=2)

query = "What is the password length requirement?"

results = retriever.invoke(query)

print("\nQUERY:")
print(query)

print("\nRESULTS:")
for i, doc in enumerate(results, 1):
    print(f"\n--- Result {i} ---")
    print(doc.page_content)