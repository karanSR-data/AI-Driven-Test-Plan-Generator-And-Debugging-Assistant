from src.vectorstore import get_retriever
from src.llm_client import get_llm
from src.prompts import TEST_PLAN_PROMPT
from src.prompts import DEBUG_ASSISTENT_PROMPT


retriever = get_retriever()
llm = get_llm()


def generate_test_plan(requirement: str):

    docs = retriever.invoke(requirement)

    context = "\n\n".join(
        doc.page_content for doc in docs
    )

    prompt = TEST_PLAN_PROMPT.format(
        context=context,
        requirement=requirement
    )

    response = llm.invoke(prompt)

    return response.content


def debug_code(error: str, code: str):

    search_query = f"{error}\n{code}"

    docs = retriever.invoke(search_query)

    context = "\n\n".join(
        doc.page_content for doc in docs
    )

    prompt = DEBUG_ASSISTENT_PROMPT.format(
        context=context,
        error=error,
        code=code
    )

    response = llm.invoke(prompt)

    return response.content