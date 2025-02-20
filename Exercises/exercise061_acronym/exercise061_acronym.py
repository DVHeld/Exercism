"""Acronym exercise"""

from re import match, sub

def abbreviate(words,/):
    """Transforms the input string into an acronym.
 
    :param str words: The words to be turned into an acronym.
    :raises TypeError: Raised when the input is not a string.
    :return str: The acronym.
    """

    if not isinstance(words, str):
        raise TypeError("The input must be a string.")
    return "".join(x if match(r"[0-9]+", x) else x[0] for x\
                   in sub(r"[^a-zA-Z0-9 ]", "", words.replace("-", " ")).title().split())
