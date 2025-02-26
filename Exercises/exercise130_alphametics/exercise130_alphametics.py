"""Alphametics exercise"""

from string import ascii_uppercase
from collections import defaultdict

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

def _split(puzzle: str, /) -> tuple:
    addends, result = puzzle.replace(" ", "").split("==")
    addends = addends.split("+")
    return (addends, result)

def _extract_operations(addends: list, result: str, /) -> list:
    operations = [["", letter] for letter in reversed(result)]
    for addend in addends:
        for index, letter in enumerate(reversed(addend)):
            operations[index][0] += letter
    return operations

def solve(puzzle: str, /) -> dict:
    """Solves the provided alphametics puzzle.

    :param str puzzle: The puzzle.
    :return dict: The solution.
    """

    _validate(puzzle)

    addends, result = _split(puzzle)

    if max(len(addend) for addend in addends) > len(result):
        raise ValueError("The length of the result must be greater or equal to the length of the"+\
                         " addends.")

    operations = _extract_operations(addends, result)
    max_len = len(operations)
    max_len = max(max(len(addend) for addend in addends), len(result))
    # letters = set(''.join(result).join(addends))
    # solution = defaultdict(int)
    solution = {letter: None for letter in set(''.join(result).join(addends))}
    carry = [0] * max_len
    # letter_digits = {letter:list(reversed(list(range(10)))) for letter in letters}
    digits = list(reversed(list(range(10))))

    operation_index = 0
    while operation_index < max_len:
        letter_index = 0
        operation_sum = 0
        while letter_index < len(operations[operation_index]):
            letter = operations[operation_index][0][letter_index]
            if solution[letter] is None:
                solution[letter] = digits.pop()
                operation_sum += solution[letter]
            letter_index += 1

        carry[operation_index+1] = operation_sum % 10
        operation_result = operation_sum // 10

        if solution[operations[operation_index][1]] is None:
            if operation_result in digits:
                solution[operations[operation_index][1]] = operation_result
            else:
                # TODO: Backtrack
                pass
        elif solution[operations[operation_index][1]] != operation_result:
            # TODO: Backtrack
            pass
        operation_index += 1
    return dict(solution)

######################### TESTING AREA #########################

# mypuzzle = "SEND + MORE == MONEY"
# myaddends = ["SEND", "MORE"]
# myresult = "MONEY"
# my_max_len = max(max(len(myaddend) for myaddend in myaddends), len(myresult))
# print(my_max_len)
# myletters = set(''.join(myresult).join(myaddends))
# print({letter:list(range(10)) for letter in set("QWERTY")})
# print(_extract_operations(["SEND", "MORE"], "MONEY"))
# print(reversed(list(range(10))))
# print({letter: None for letter in set(''.join(myresult).join(myaddends))})
