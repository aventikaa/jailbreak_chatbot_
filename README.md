# AI Jailbreak Security Demo

## Overview

This project demonstrates the difference between a **vulnerable AI chatbot** and a **secure AI chatbot** when exposed to prompt injection and jailbreak attacks.

Users can enter the same prompt and compare how each chatbot responds:

* 🚨 **Vulnerable Bot** – intentionally follows unsafe instructions and is susceptible to prompt injection.
* 🔒 **Secure Bot** – uses guardrails and system-level protections to detect and block jailbreak attempts.



---

## Features

### Vulnerable Chatbot

* Follows user instructions with minimal restrictions
* Demonstrates prompt injection vulnerabilities
* Useful for studying attack techniques

### Secure Chatbot

* Detects common jailbreak attempts
* Blocks malicious prompts
* Refuses requests to reveal hidden instructions or bypass safeguards

### Side-by-Side Comparison

* Compare secure and vulnerable responses simultaneously
* Observe how guardrails affect model behavior

## Project Structure

```text
jailbreak-chatbot/

├── app/
│   ├── vulnerable_bot.py
│   ├── secure_bot.py
│   ├── guardrails.py
│   └── logger.py
│
├── logs/
│   
│
├── frontend.py
├── requirements.txt
├── README.md
└── .env
```

---


## Running the Application

### Streamlit

```bash
streamlit run frontend.py
```

The application will be available at:

```text
(https://jailbreakchatbot.streamlit.app/)
```

---

