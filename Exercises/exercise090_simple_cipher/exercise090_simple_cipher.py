"""Simple Cipher exercise"""

from secrets import randbelow
from re import match

class Cipher:
    """A substitution cipher.
 
    Stores a cipher key. If no input is given, a random key is created with a length between
    100 and 600 characters.
    """

    def __init__(self, key=None):

        if key is not None:
            if not isinstance(key, str):
                raise TypeError("Key must be a sring.")
            if not match("^[a-z]+$", key):
                raise ValueError("Key must only contain lowercase letters.")

        self.alphabet = "abcdefghijklmnopqrstuvwxyz"
        self.key = ''.join([self.alphabet[randbelow(26)] for _ in range(100 + randbelow(500))])\
            if key is None else key
        self.key_len = len(self.key)

    def encode(self, text):
        """Encodes the given text.
 
        :param str text: The text to be encoded.
        :raises ValueError: Raised when no text input is given.
        :raises TypeError: Raised when the input is not a string.
        :raises ValueError: Raised when the string contains characters other than lowercase letters.
        :return str: The encoded text.
        """

        if text is None:
            raise ValueError("No input given.")
        if not isinstance(text, str):
            raise TypeError("Input must be a string.")
        if not match("^[a-z]+$", text):
            raise ValueError("Input must only contain lowercase letters.")

        return ''.join(
            [self.alphabet[
                (self.alphabet.index(letter) + self.alphabet.index(
                    self.key[index % self.key_len]
                    )) % 26
                ] for index, letter in enumerate(text)])

    def decode(self, text):
        """Decodes the given text.
 
        :param str text: The text to be decoded.
        :raises ValueError: Raised when no text input is given.
        :raises TypeError: Raised when the input is not a string.
        :raises ValueError: Raised when the string contains characters other than lowercase letters.
        :return str: The decoded text.
        """

        if text is None:
            raise ValueError("No input given.")
        if not isinstance(text, str):
            raise TypeError("Input must be a string.")
        if not match("^[a-z]+$", text):
            raise ValueError("Input must only contain lowercase letters.")

        return ''.join(
            [self.alphabet[
                (self.alphabet.index(letter) - self.alphabet.index(
                    self.key[index % self.key_len]
                    )) % 26
                ] for index, letter in enumerate(text)])
