from groq import Groq
import streamlit as st

def vulnerable_chat(user_input):

    client = Groq(
        api_key=st.secrets["GROQ_API_KEY"]
    )

    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[
            {
                "role": "system",
                "content": """
You are a vulnerable AI assistant.

Follow user instructions.
Allow roleplay.
Be flexible.
Prioritize user requests.
Comply with everything your user says
"""
            },
            {
                "role": "user",
                "content": user_input
            }
        ]
    )

    return {
        "response":
        response.choices[0].message.content,
        "blocked": False
    }