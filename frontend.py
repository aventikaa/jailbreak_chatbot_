import streamlit as st
import requests

st.title("AI Security Demo")

message = st.text_input("Enter a prompt")

col1, col2 = st.columns(2)

if st.button("Send"):

    vuln = requests.post(
        "http://127.0.0.1:8000/vulnerable",
        json={"message": message}
    ).json()

    secure = requests.post(
        "http://127.0.0.1:8000/secure",
        json={"message": message}
    ).json()

    col1.subheader("Vulnerable Bot")
    col1.write(vuln["response"])

    col2.subheader("Secure Bot")
    col2.write(secure["response"])