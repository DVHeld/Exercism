"""Word Search exercise"""

from operator import add, mul

class Point:
    """A point in the puzzle."""

    def __init__(self, x, y):

        self.x = x
        self.y = y

    def __eq__(self, other):

        return self.x == other.x and self.y == other.y

    def __str__(self):

        return f"({self.x}, {self.y})"

    def __repr__(self):

        return f"Point({self.x}, {self.y})"

class WordSearch:
    """A word search puzzle. Stores the puzzle and searches for any given word."""

    def __init__(self, puzzle):

        if not isinstance(puzzle, (list, tuple)):
            raise TypeError("The puzzle must be a list or tuple.")
        for row in puzzle:
            if not isinstance(row, str):
                raise TypeError("The puzzle's rows must be strings.")
        self.puzzle = puzzle

    def search(self, word):
        """Searches the provided word in the puzzle.
 
        :param str word: The word to be searched in the puzzle.
        :raises TypeError: Raised if the word is not a string.
        :return None, tuple: Returns None if there is no match, or a tuple of the point where the
        word starts and the one where it ends.
        """

        if not isinstance(word, str):
            raise TypeError("Word must be a string.")
        for row_no, row in enumerate(self.puzzle):
            for col_no, char in enumerate(row):
                if char == word[0]:
                    result = self._lookup(word, (row_no, col_no))
                    if result:
                        return (Point(col_no, row_no), result)
        return None

    def _lookup(self, word, origin):

        directions = ((-1,-1), (-1, 0), (-1, 1),
                      ( 0,-1),          ( 0, 1),
                      ( 1,-1), ( 1, 0), ( 1, 1))
        for direction in directions:
            next_direction = tuple(map(add, origin, direction))
            if -1 in next_direction or \
               next_direction[0] >= len(self.puzzle) or \
               next_direction[1] >= len(self.puzzle[0]):
                continue
            if self.puzzle[next_direction[0]][next_direction[1]] == word[1]:
                for offset, letter in enumerate(word[2:]):
                    next_index = tuple(map(add, origin, map(mul, direction, (offset+2,)*2)))
                    if -1 in next_index or \
                       next_index[0] >= len(self.puzzle) or \
                       next_index[1] >= len(self.puzzle[0]):
                        break
                    next_letter = self.puzzle[next_index[0]][next_index[1]]
                    if next_letter != letter:
                        break
                    if offset == len(word)-3 and next_letter == letter:
                        return Point(next_index[1], next_index[0])
        return False
