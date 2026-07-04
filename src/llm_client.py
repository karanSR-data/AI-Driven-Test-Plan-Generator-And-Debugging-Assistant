from langchain_groq import ChatGroq
from src.config import Config

def get_llm():
    """
    Returns configured LLM instance.
    """

    llm = ChatGroq(
        api_key=Config.GROQ_API_KEY,
        model_name="llama-3.3-70b-versatile",
        temperature=0.2
    )

    return llm


if __name__ == "__main__":
    llm = get_llm()

    response = llm.invoke(
        "Say hello in one sentence."
    )

    print(response.content)