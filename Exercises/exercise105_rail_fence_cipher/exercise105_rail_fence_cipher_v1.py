"""Rail Fence Cipher exercise"""

from itertools import cycle

def encode(message, rails):

    message_list = [['' for _ in range(len(message))] for _ in range(rails)]
    cycler = cycle(list(range(rails)) + list(range(rails))[::-1][1:-1])
    for index, char in enumerate(message):
        message_list[next(cycler)][index] = char
    return ''.join(''.join(message) for message in message_list)

def decode(encoded_message, rails):

    message_list = [['' for _ in range(len(encoded_message))] for _ in range(rails)]
    cycler = cycle(list(range(rails)) + list(range(rails))[::-1][1:-1])
    for index, char in enumerate(encoded_message):
        message_list[next(cycler)][index] = "*"
    msg_iter = iter(encoded_message)
    for row_no in range(len(message_list)):
        for col_no in range(len(message_list[row_no])):
            if message_list[row_no][col_no] == "*":
                message_list[row_no][col_no] = next(msg_iter)
    message_list = zip(*message_list)
    return ''.join(''.join(message) for message in message_list)
