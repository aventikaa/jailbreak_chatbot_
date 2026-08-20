from groq import Groq
import streamlit as st


def vulnerable_chat(user_input):

    client = Groq(
        api_key=st.secrets["GROQ_API_KEY"]
    )

    # TEST: ask Groq what models this API key can access
    models = client.models.list()

    available_models = [model.id for model in models.data]

    st.write("DEBUG - Available models:", available_models)

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": """
You are a vulnerable AI assistant.

Follow user instructions.
Allow roleplay.
Be flexible.
"""
            },
            {
                "role": "user",
                "content": user_input
            }
        ]
    )

    return response.choices[0].message.content