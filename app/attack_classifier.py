def classify_attack(prompt):

    text = prompt.lower()

    if "ignore" in text:
        return "Prompt Injection"

    elif "pretend" in text:
        return "Roleplay Jailbreak"

    elif "developer mode" in text:
        return "Developer Mode"

    elif "system prompt" in text:
        return "System Prompt Extraction"

    elif "manipulat" in text:
        return "Unsafe Request"

    else:
        return "Benign Query"