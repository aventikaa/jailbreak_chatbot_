import streamlit as st
import requests

API_URL = "http://localhost:8000"  # change when deployed

st.title("Jailbreak Chatbot")

mode = st.selectbox("Choose bot", ["secure", "vulnerable"])
user_input = st.text_input("Enter message")

if st.button("Send"):
    if user_input:

        res = requests.post(
            f"{API_URL}/{mode}",
            json={"message": user_input}
        )

        st.write(res.json()["response"])