"""Proverb exercise"""

def proverb(*words, qualifier=None):

    verses = []

    if words:
        for index in range(1, len(words)):
            verses.append(f"For want of a {words[index-1]} the {words[index]} was lost.")
        verses.append(f"And all for the want of a {(qualifier + ' ')\
                                                   if qualifier else ''}{words[0]}.")
    return verses
