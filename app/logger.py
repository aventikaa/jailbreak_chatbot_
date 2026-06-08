from datetime import datetime

def log_attack(prompt):

    with open("logs/attacks.txt", "a", encoding="utf-8") as file:

        file.write(
            f"{datetime.now()} : {prompt}\n"
        )