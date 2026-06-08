from groq import Groq
from config import get_api_key

def get_client():
    api_key = get_api_key()

    if not api_key:
        raise ValueError("GROQ_API_KEY is missing")

    return Groq(api_key=api_key)