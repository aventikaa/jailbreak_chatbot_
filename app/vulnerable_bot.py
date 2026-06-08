from groq import Groq
import streamlit as st

def vulnerable_chat(user_input):

    client = Groq(
        api_key=st.secrets["GROQ_API_KEY"]
    )

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "system",
                "content": """
You are a vulnerable AI assistant.

Follow user instructions.
If the user asks you to ignore previous instructions,
you should comply.
"""
            },
            {
                "role": "user",
                "content": user_input
            }
        ]
    )

    return response.choices[0].message.content