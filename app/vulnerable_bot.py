import streamlit as st

from app.vulnerable_bot import vulnerable_chat
from app.secure_bot import secure_chat

st.title("AI Jailbreak Security Demo")

mode = st.selectbox(
    "Choose Bot",
    ["Secure Bot", "Vulnerable Bot"]
)

user_input = st.text_area("Enter Prompt")

if st.button("Send") and user_input:

    if mode == "Secure Bot":
        response = secure_chat(user_input)
    else:
        response = vulnerable_chat(user_input)

    st.write("### Response")
    st.write(response)