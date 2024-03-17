# analyzer.py
import time, gc

def analyze_payload(payload):
    tokens = []
    token_start = 0
    in_token = False

    for i, char in enumerate(payload):
        if char == "<":
            if in_token:
                tokens.append(payload[token_start:i])
            token_start = i
            in_token = True
        elif char == ">" and in_token:
            tokens.append(payload[token_start:i+1])
            in_token = False
            token_start = i + 1
        elif not in_token and (i == len(payload) - 1 or payload[i+1] == "<"):
            tokens.append(payload[token_start:i+1])
            token_start = i + 1

    if not in_token and token_start < len(payload):
        tokens.append(payload[token_start:])

    return tokens
