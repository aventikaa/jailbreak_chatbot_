BLOCKED_PHRASES = [

    "ignore previous instructions",
    "ignore all instructions",
    "developer mode",
    "reveal system prompt",
    "jailbreak",
    "bypass safeguards",
    "pretend you are"

]

UNSAFE_TOPICS = [

    "scam",
    "fraud",
    "steal",
    "hack",
    "malware",
    "manipulate"

]

def detect_jailbreak(text):

    text = text.lower()

    for phrase in BLOCKED_PHRASES:

        if phrase in text:
            return True

    return False

def detect_unsafe_request(text):

    text = text.lower()

    for topic in UNSAFE_TOPICS:

        if topic in text:
            return True

    return False