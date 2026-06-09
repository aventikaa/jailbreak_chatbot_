import streamlit as st

from app.vulnerable_bot import vulnerable_chat
from app.secure_bot import secure_chat

from app.attack_library import ATTACKS
from app.attack_classifier import classify_attack

from app.logger import (
    log_attack,
    get_logs
)

st.set_page_config(
    page_title="AI Security Dashboard",
    layout="wide"
)

st.title("🔐 AI Security Testing Dashboard")

# Sidebar

st.sidebar.title("📊 Security Dashboard")

logs = get_logs()

st.sidebar.subheader("Attack History")

st.sidebar.text_area(
    "Logs",
    logs,
    height=400
)

# Attack Selector

attack_choice = st.selectbox(
    "Select Attack Type",
    list(ATTACKS.keys())
)

prompt = st.text_area(
    "Prompt",
    value=ATTACKS[attack_choice],
    height=150
)

if st.button("🚀 Launch Attack"):

    attack_type = classify_attack(prompt)

    vuln = vulnerable_chat(prompt)

    secure = secure_chat(prompt)

    secure_result = (
        "BLOCKED"
        if secure["blocked"]
        else "ALLOWED"
    )

    log_attack(
        prompt,
        attack_type,
        secure_result
    )

    st.subheader(
        f"Detected Attack Type: {attack_type}"
    )

    col1, col2 = st.columns(2)

    with col1:

        st.markdown("## 🚨 Vulnerable Agent")

        st.write(vuln["response"])

        st.error(
            "Attack Successful"
        )

    with col2:

        st.markdown("## 🔒 Secure Agent")

        st.write(secure["response"])

        if secure["blocked"]:

            st.success(
                "Attack Blocked"
            )

        else:

            st.warning(
                "Attack Passed"
            )