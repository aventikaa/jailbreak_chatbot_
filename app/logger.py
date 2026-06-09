from datetime import datetime
import os

LOG_FILE = "logs/attacks.txt"

os.makedirs("logs", exist_ok=True)

def log_attack(prompt, attack_type, result):

    with open(LOG_FILE, "a", encoding="utf-8") as f:

        f.write(
            f"{datetime.now()} | {attack_type} | {result} | {prompt}\n"
        )

def get_logs():

    if not os.path.exists(LOG_FILE):
        return ""

    with open(LOG_FILE, "r", encoding="utf-8") as f:
        return f.read()