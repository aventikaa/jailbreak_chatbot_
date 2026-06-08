import os

def get_api_key():
    return os.getenv("GROQ_API_KEY")