"""Word Count exercise"""

from re import findall

def count_words(sentence):
    """Gives the count for each word in the provided text.
 
    :param str sentence: The sentence to count the words of.
    :raises TypeError: Raised if the input is not a string.
    :raises ValueError: Raised if the input is an empty string.
    :return dict{str:int}: A dictionary containing the different words and the number of their
                           occurrence.
    """

    if not isinstance(sentence, str):
        raise TypeError("Input must be a string.")
    if not sentence:
        raise ValueError("String must not be empty.")

    words = findall(r"[a-z\d]+(?:'*[a-z\d]+)*", sentence.casefold())
    wordcount = {}
    for word in set(words):
        wordcount[word] = words.count(word)
    return wordcount
