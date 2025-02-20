"""Pangram exercise"""

def is_pangram(sentence):
    """Checks if the sentence is a pangram.

    Checks if the sentence contains every letter in the alphabet at
    least once. Returns True if it does, False otherwise.

    :param str sentence: The sentence.
    :return bool: True if it's a pangram, False otherwise.
    """

    alphabet = "qwertyuiopasdfghjklzxcvbnm"
    sentence = sentence.lower()
    for letter in alphabet:
        if letter not in sentence:
            return False
    return True

# print(is_pangram("The quick brown fox jumps over the lazy dog."))
# print(is_pangram("Hello World"))
