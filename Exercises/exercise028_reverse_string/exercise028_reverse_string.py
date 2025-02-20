"""Reverse String exercise"""

def reverse(text):
    """Reverses the text.

    :param str text: The text to reverse.
    :return str: The reversed text.
    """

    text = list(text)
    reversed = ""
    while text:
        reversed += text.pop()
    return reversed
