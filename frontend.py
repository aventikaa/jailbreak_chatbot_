import streamlit as st

from app.vulnerable_bot import vulnerable_chat
from app.secure_bot import secure_chat

from app.attack_classifier import classify_attack
from app.attack_library import ATTACKS

from app.logger import (
    log_attack,
    get_logs
)

st.set_page_config(
    page_title="AI Security Dashboard",
    layout="wide"
)

st.title("AI Security Demo w/ Logging and Attack Classification")

# -------------------
# Sidebar
# -------------------

with st.sidebar:

    st.header("Attack History")

    st.text_area(
        "Logs",
        get_logs(),
        height=400
    )

# -------------------
# Preset attacks
# -------------------

selected_attack = st.selectbox(
    "Choose an attack",
    list(ATTACKS.keys())
)

message = st.text_area(
    "Prompt",
    ATTACKS[selected_attack]
)

# -------------------
# Launch
# -------------------

if st.button("Send Prompt"):

    attack_type = classify_attack(message)

    st.info(
        f"Detected Prompt Type: {attack_type}"
    )

    vuln = vulnerable_chat(message)

    secure = secure_chat(message)

    secure_blocked = (
        "Potential jailbreak"
        in secure["response"]
    )

    log_attack(
        message,
        attack_type,
        "BLOCKED" if secure_blocked else "PASSED"
    )

    col1, col2 = st.columns(2)

    # -------------------
    # Vulnerable
    # -------------------

    with col1:

        st.subheader("🚨 Vulnerable Bot")

        st.write(vuln["response"])

        st.error(
            "Attack Successful"
        )

    # -------------------
    # Secure
    # -------------------

    with col2:
        st.subheader("🔒 Secure Bot")
        st.write(
            secure["response"]
            )
        if secure["blocked"]:
            st.success(
            "🛡️ Attack Blocked"
            )
        else:
            st.warning(
            " 📩 Prompt Passed"
            )