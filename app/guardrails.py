BLOCKED_PHRASES = [

    "ignore previous instructions",
    "reveal system prompt",
    "developer mode",
    "jailbreak",
    "pretend you are",
    "act as",
    "bypass rules"

]

def detect_jailbreak(text):

    text = text.lower()

    for phrase in BLOCKED_PHRASES:
        if phrase in text:
            return True

    return False