import streamlit as st

from app.vulnerable_bot import vulnerable_chat
from app.secure_bot import secure_chat

st.title("🔐 AI Security Demo")

message = st.text_input("Enter a prompt")

if st.button("Send") and message:

    vulnerable_response = vulnerable_chat(message)
    secure_response = secure_chat(message)

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("🚨 Vulnerable Bot")
        st.write(vulnerable_response)

    with col2:
        st.subheader("🔒 Secure Bot")
        st.write(secure_response)