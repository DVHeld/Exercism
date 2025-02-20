"""Pig Latin exercise"""

import re

VOWELS = list("aeiou")
CONSONANTS = list("qwrtypsdfghjklzxcvbnm")
RULES = {
    "Rule 1": r"^("+"|".join(VOWELS + ["xr", "yt", "ay"])+")+",
    "Rule 2": r"^("+"|".join(CONSONANTS)+")+",
    "Rule 3": r"^("+"|".join(CONSONANTS)+")*(qu)",
    "Rule 4": r"^("+"|".join(CONSONANTS)+")+(y)"
    }

def process(word):
    """Receives a word and converts it to pig latin.
 
    :param str word: The word.
    :return str: The translated word.
    """

    processed_word = ""
    print(f"word: {word} - word[0]: {word[0]} - word[:2]: {word[:2]}")
    match_r1 = re.search(RULES["Rule 1"], word)
    match_r2 = re.search(RULES["Rule 2"], word)
    match_r3 = re.search(RULES["Rule 3"], word)
    match_r4 = re.search(RULES["Rule 4"], word)
    if match_r1:
        print("r1")
        processed_word = f"{word}ay"
    elif match_r3:
        print("r3")
        processed_word = word[match_r3.end(0):] + match_r3.group(0) + "ay"
    elif match_r4:
        print("r4")
        processed_word = word[match_r4.end(0)-1:] + match_r4.group(0)[:-1] + "ay"
    else:
        print("r2")
        processed_word = word[match_r2.end(0):] + match_r2.group(0) + "ay"
    return processed_word

def translate(text):
    """Translates the text to pig latin.
 
    :param str text: The text to be translated.
    :return str: The translated text.
    """

    if " " in text:
        words = text.split(" ")
        translation = ""
        for word in words:
            translation += process(word) + " "
        return translation.strip()
    return process(text)
