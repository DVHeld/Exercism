"""Secret Handshake exercise"""

ACTIONS = {
    0: "wink",
    1: "double blink",
    2: "close your eyes",
    3: "jump"
}

def commands(binary_str):
    handshake = []
    action_amount = len(binary_str)
    if action_amount == 5:
        action_amount -= 1
    for action in range(action_amount):
        if int(binary_str[-action - 1]):
            handshake.append(ACTIONS[action])
    try:
        if int(binary_str[-5]):
            handshake.reverse()
    finally:
        return handshake
