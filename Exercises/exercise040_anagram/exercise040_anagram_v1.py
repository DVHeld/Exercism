"""Anagram exercise"""

def find_anagrams(word, candidates):
    """Finds the anagrams of the given word.
 
    This function takes the given word and compares it to the provided
    candidates. If the candidate is an anagram of the word, it is added
    to a list. This list is then returned.
 
    :param str word: The word to check against.
    :param list[str] candidates: The list of candidate words.
    :return list[str]: The resulting list of anagrams.
    """

    anagrams = []
    for candidate in candidates:
        matched = True
        if (len(candidate) != len(word)) or (candidate.lower() == word.lower()):
            continue
        for letter in word:
            if word.lower().count(letter.lower()) != candidate.lower().count(letter.lower()):
                matched = False
                break
        if matched:
            anagrams.append(candidate)
    return anagrams
