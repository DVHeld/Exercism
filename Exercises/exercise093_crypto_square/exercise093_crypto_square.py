"""Crypto Square exercise"""

from re import sub
from math import ceil, sqrt

def cipher_text(plain_text):
    """Encodes the given text using the crypto square method.
 
    :param str plain_text: The text to be encoded.
    :raises ValueError: Raised when the input is empty.
    :raises TypeError: Raised when the input is not a string.
    :return str: The encoded text.
    """

    if plain_text is None:
        raise ValueError("No input.")
    if not isinstance(plain_text, str):
        raise TypeError("Input must be a string.")

    normalized_text = sub(r"\W", "", plain_text).lower()
    measure = sqrt(len(normalized_text))
    rectangle_length = ceil(measure)
    rectangle_height = round(measure)
    text_rectangle = []
    for row_no in range(rectangle_height):
        line = normalized_text[row_no * rectangle_length:(row_no + 1) * rectangle_length]
        for _ in range(rectangle_length - len(line)):
            line = line + " "
        text_rectangle.append(line)
    linearized_text = ""
    for col_no in range(rectangle_length):
        for row in text_rectangle:
            linearized_text += row[col_no]
    encoded_text = ""
    for char_index, character in enumerate(linearized_text, 1):
        encoded_text += character
        if char_index % rectangle_height == 0 and\
           char_index < rectangle_length**2 and\
           char_index < rectangle_height**2 + 1:
            encoded_text += " "
    return encoded_text
