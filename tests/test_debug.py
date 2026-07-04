# test_debug.py

from src.rag_chain import debug_code

error = "NameError: name 'x' is not defined"

code = """
print(x)
"""

response = debug_code(error, code)

print(response)