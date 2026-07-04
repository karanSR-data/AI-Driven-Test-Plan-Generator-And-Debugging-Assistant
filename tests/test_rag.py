# test_rag.py

from src.rag_chain import generate_test_plan

requirement = "Generate a test plan for login functionality"

response = generate_test_plan(requirement)

print(response)