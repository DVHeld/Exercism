"""Run-Length Encoding exercise"""

import re

def decode(string):
    """Decodes the string using run-length decoding.
 
    :param str string: The encoded string.
    :raises TypeError: Raised when the input is not a string.
    :return str: The decoded string.
    """

    if not isinstance(string, str):
        raise TypeError("Input must be string.")

    alpha_list = re.findall(r"\D", string)
    number_list = re.split(r"\D", string)[:-1]
    decoded = ""
    for i,n in enumerate(number_list):
        decoded += int(n if n else 1) * f"{alpha_list[i]}"
    return decoded

def encode(string):
    """Encodes the string using run-length encoding.
 
    :param str string: The plain string.
    :raises TypeError: Raised when the input is not a string.
    :return str: The encoded string.
    """

    if not isinstance(string, str):
        raise TypeError("Input must be string.")

    encoded = ""
    alpha = string[0] if string else ""
    number = 0
    while string:
        if string[0] != alpha:
            encoded += bool(number-1) * f"{number}" + f"{alpha}"
            number = 1
            alpha = string[0]
        else:
            number += 1
        string = string[1:]
    return encoded + bool(number-1 if number else 0) * f"{number}" + f"{alpha}"
