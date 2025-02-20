"""Isogram exercise"""

def is_isogram(string):
    """Checks if the string is an isogram.

    This function checks if the string is an isogram. It doesn't count
    spaces nor isograms.

    :param str string: The string to check.
    :return bool: True if it's an isogram, False otherwise.
    """

    string = string.replace(" ", "").replace("-", "").lower()
    for letter in string:
        if string.count(letter) > 1:
            return False
    return True

# print(is_isogram("isogram"))
# print(is_isogram("isograms"))
# print(is_isogram("six-year-old"))
# print(is_isogram("downstream"))
# print(is_isogram("background"))
# print(is_isogram("lumberjacks"))
# print(is_isogram("Juan el sucio"))
