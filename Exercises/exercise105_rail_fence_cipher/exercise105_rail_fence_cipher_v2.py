"""Rail Fence Cipher exercise"""

from itertools import cycle

def encode(message, rails):
    cycler = cycle(list(range(rails)) + list(range(rails))[::-1][1:-1])
    return ''.join(sorted(message, key=lambda index: next(cycler)))

def decode(encoded_message, rails):
    cycler = cycle(list(range(rails)) + list(range(rails))[::-1][1:-1])
    indices = sorted(range(len(encoded_message)), key=lambda index: next(cycler))
    return ''.join([element[1] for element in sorted(zip(indices, encoded_message))])
