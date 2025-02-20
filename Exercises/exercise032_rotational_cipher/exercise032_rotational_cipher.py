"""Rotational Cipher exercise"""

def rotate(text, key):
    """Encrypts the text using ROT{key}
 
    This function encrypts the given text using the Rotational/Caesar
    cipher with the given encryption key. It returns the encrypted text.
 
    :param str text: The text to be encrypted.
    :param int key: The encryption key.
    :return str: The encrypted text.
    """

    if not isinstance(key, int):
        raise TypeError("The key must be an integer")
    text = str(text)
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    encrypted_text = ""
    for letter in text:
        if letter in lower_case:
            encrypted_text += lower_case[(lower_case.index(letter) + key) % 26]
        elif letter in upper_case:
            encrypted_text += upper_case[(upper_case.index(letter) + key) % 26]
        else:
            encrypted_text += letter
    return encrypted_text
