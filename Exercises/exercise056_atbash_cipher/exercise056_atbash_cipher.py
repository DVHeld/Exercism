"""Atbash Cipher exercise"""

import re

KEY_DICT = {
    'a': 'z',
    'b': 'y',
    'c': 'x',
    'd': 'w',
    'e': 'v',
    'f': 'u',
    'g': 't',
    'h': 's',
    'i': 'r',
    'j': 'q',
    'k': 'p',
    'l': 'o',
    'm': 'n',
    'n': 'm',
    'o': 'l',
    'p': 'k',
    'q': 'j',
    'r': 'i',
    's': 'h',
    't': 'g',
    'u': 'f',
    'v': 'e',
    'w': 'd',
    'x': 'c',
    'y': 'b',
    'z': 'a',
    '1': '1',
    '2': '2',
    '3': '3',
    '4': '4',
    '5': '5',
    '6': '6',
    '7': '7',
    '8': '8',
    '9': '9',
    '0': '0'    
}

def encode(plain_text):
    """Encodes the text using the Atbash cipher.
 
    :param str plain_text: The text to be encoded.
    :raises TypeError: Raised if the parameter is not a string.
    :return str: The encoded text.
    """

    if not isinstance(plain_text, str):
        raise TypeError("Parameter must be a string.")
    plain_text = re.sub(r'\W', '', plain_text).casefold()
    encoded = ''
    counter = 0
    for character in plain_text:
        if counter == 5:
            counter = 0
            encoded += ' '
        encoded += KEY_DICT[character]
        counter += 1
    return encoded

def decode(ciphered_text):
    """Decodes a text encoded with the Atbash cipher.
 
    :param str ciphered_text: The encoded text to be decoded.
    :raises TypeError: Raised if the parameter passed is not a string.
    :return str: The decoded text.
    """

    if not isinstance(ciphered_text, str):
        raise TypeError("Parameter must be a string.")
    ciphered_text = re.sub(r'\W', '', ciphered_text).casefold()
    decoded = ''
    for character in ciphered_text:
        decoded += KEY_DICT[character]
    return decoded
