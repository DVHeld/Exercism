"""Alphametics exercise"""

from string import ascii_uppercase
from collections import defaultdict

def _split(puzzle: str, /) -> tuple:
    addends, result = puzzle.replace(" ", "").split("==")
    addends = addends.split("+")
    return (addends, result)

def _validate(puzzle: any, /) -> None:
    if not puzzle:
        raise ValueError("Missing input.")
    if not isinstance(puzzle, str):
        raise TypeError("Input must be a string.")
    if len(set(puzzle.replace(" ", "").replace("+", "").replace("=" , ""))) > 10:
        raise ValueError("Too many different letters. Maximum is 10.")
    for char in puzzle:
        if char not in ascii_uppercase + "= +":
            raise ValueError(f"Invalid character in puzzle: '{char}'")

def solve(puzzle: str, /) -> dict:
    """Solves the provided alphametics puzzle.

    :param str puzzle: The puzzle.
    :return dict: The solution.
    """

    _validate(puzzle)

    addends, result = _split(puzzle)
    solution = defaultdict(int)
    max_len = max(max(len(addends)), len(solution))
    remainders = [0] * max_len
    letters = set(''.join(result).join(addends))
    letter_digits = {letter:list(range(10)) for letter in letters}

    column = max_len
    while column > 0:
        row = 0
        while row > len(addends):
            row += 1
        column -= 1
    return solution

######################### TESTING AREA #########################

# mypuzzle = "SEND + MORE == MONEY"
# myaddends = ["SEND", "MORE"]
# myresult = "MONEY"
# myletters = set(''.join(myresult).join(myaddends))
# print({letter:list(range(10)) for letter in set("QWERTY")})
