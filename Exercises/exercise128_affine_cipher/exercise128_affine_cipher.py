"""Affine Cipher exercise"""

from re import sub

BASE_INDEX = ord("a")
ALPHABET_LENGTH = ord("z") - BASE_INDEX + 1

def _coprime(a):

    for divisor in range(max(a, ALPHABET_LENGTH), 1, -1):
        if a % divisor == 0 and ALPHABET_LENGTH % divisor == 0:
            return False
    return True

def _letter_index(letter):

    return ord(letter) - BASE_INDEX

def _letter_from_index(letter_index):

    return chr(letter_index + BASE_INDEX)

def _mmi(a):

    q, r, s = [], [a, ALPHABET_LENGTH], [1, 0]
    index = 1
    while r[-1] != 0:
        q.append(r[index-1] // r[index])
        r.append(r[index-1] - q[index-1] * r[index])
        s.append(s[index-1] - q[index-1] * s[index])
        index += 1
    return s[-2] % ALPHABET_LENGTH

def encode(plain_text, a, b, word_length = 5):
    """Encodes the given plain text using the Affine cipher with keys a and b. The output word
    length can be optionally specified.
 
    :param str plain_text: The text to be encrypted.
    :param int a: The first key.
    :param int b: The second key.
    :param int word_length: The length of the output words, defaults to 5.
    :raises ValueError: Raised when there is a missing input.
    :raises TypeError: Raised when the text input is not a string.
    :raises TypeError: Raised when the keys are not integers.
    :raises ValueError: Raised when the keys are not greater than zero.
    :raises ValueError: Raised when a is not coprime with the alphabet length.
    :raises TypeError: Raised when the output word length is not an integer.
    :raises ValueError: Raised when the output word length is not greater than zero.
    :return str: The encoded text.
    """

    if None in (plain_text, a, b, word_length):
        raise ValueError("Missing input.")
    if not isinstance(plain_text, str):
        raise TypeError("The input text must be a string.")
    if not (isinstance(a, int) and isinstance(b, int)):
        raise TypeError("The keys must be integers.")
    if a <= 0 or b <= 0:
        raise ValueError("Keys must be greater than zero.")
    if not _coprime(a):
        raise ValueError("a and m must be coprime.")
    if not isinstance(word_length, int):
        raise TypeError("The output word length must be an integer.")
    if word_length <= 0:
        raise ValueError("The output word length must be greater than zero.")

    encoded = ""
    purged_text = sub(r"[^a-z0-9]", "", plain_text.lower())

    for count, letter in enumerate(purged_text):
        if count and count % word_length == 0:
            encoded += " "
        if letter.isdigit():
            encoded += letter
        else:
            encoded_letter_index = (a * _letter_index(letter) + b) % ALPHABET_LENGTH
            encoded += _letter_from_index(encoded_letter_index)
    return encoded

def decode(ciphered_text, a, b):
    """Decodes the given encoded text using the Affine cipher with keys a and b.
 
    :param str plain_text: The text to be decrypted.
    :param int a: The first key.
    :param int b: The second key.
    :raises ValueError: Raised when there is a missing input.
    :raises TypeError: Raised when the text input is not a string.
    :raises TypeError: Raised when the keys are not integers.
    :raises ValueError: Raised when the keys are not greater than zero.
    :raises ValueError: Raised when a is not coprime with the alphabet length.
    :return str: The decoded text.
    """

    if None in (ciphered_text, a, b):
        raise ValueError("Missing input.")
    if not isinstance(ciphered_text, str):
        raise TypeError("The input text must be a string.")
    if not (isinstance(a, int) and isinstance(b, int)):
        raise TypeError("The keys must be integers.")
    if a <= 0 or b <= 0:
        raise ValueError("Keys must be greater than zero.")
    if not _coprime(a):
        raise ValueError("a and m must be coprime.")

    decoded = ""
    mmi = _mmi(a)

    for letter in ciphered_text.replace(" ", ""):
        if letter.isdigit():
            decoded += letter
        else:
            decoded_letter_index = (mmi * (_letter_index(letter) - b)) % ALPHABET_LENGTH
            decoded += _letter_from_index(decoded_letter_index)
    return decoded
