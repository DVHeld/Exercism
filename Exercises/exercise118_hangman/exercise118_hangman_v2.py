"""Hangman exercise"""

# Game status categories
STATUS_WIN = 'win'
STATUS_LOSE = 'lose'
STATUS_ONGOING = 'ongoing'

class Hangman:
    """A hangman game."""

    def __init__(self, word, /, maximum_guesses = 9):

        self._remaining_guesses = maximum_guesses
        self._status = STATUS_ONGOING
        self._word = list(word.casefold())
        self._masked_word = ["_"] * len(word)

    def guess(self, char):

        if not char.isalpha():
            raise ValueError("Input must be a letter")
        if self._status != STATUS_ONGOING:
            raise ValueError("The game has already ended.")

        char = char.casefold()
        not_found = True
        for index, word_char in enumerate(self._word):
            if char == word_char:
                self._masked_word[index] = char
                self._word[index] = "_"
                not_found = False
        if not_found:
            self._remaining_guesses -= 1
        if "_" not in self._masked_word:
            self._status = STATUS_WIN
        elif self._remaining_guesses < 0:
            self._status = STATUS_LOSE

    def get_masked_word(self):

        return ''.join(self._masked_word)

    def get_status(self):

        return self._status

    @property
    def remaining_guesses(self):

        return self._remaining_guesses
