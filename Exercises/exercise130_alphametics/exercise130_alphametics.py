"""Alphametics exercise"""

from string import ascii_uppercase

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
    operations = [{"operation": "", "letter": letter} for letter in reversed(result)]
    for addend in addends:
        for index, letter in enumerate(reversed(addend)):
            operations[index]["operation"] += letter
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
    max_len = len(result)
    letters = set(''.join(result).join(addends))
    solution = {letter: None for letter in set(''.join(result).join(addends))}
    digits = list(reversed(list(range(10))))
    letter_digits = {letter: {"available": digits, "used": None, "backtrack": False}
                     for letter in letters}
    carry = [0] * max_len

    operation_index = 0
    while operation_index < max_len:
        operation_sum = 0
        letter_index = 0
        while letter_index < len(operations[operation_index]):
            letter = operations[operation_index]["operation"][letter_index]
            if solution[letter] is None: # Assign next digit
                if len(letter_digits[letter]["available digits"]): # Add next digit to solution
                    digit = letter_digits[letter]["available digits"].pop()
                    letter_digits[letter]["used digits"].append(digit)
                    for l in letters:
                        letter_digits[l]["available digits"].append(solution[letter]).sort()
                        letter_digits[l]["available digits"].remove(digit)
                    solution[letter] = digit
                    operation_sum += solution[letter]
                else: # Backtrack
                    letter_digits[letter]["available digits"] = letter_digits[letter]["used digits"]
                    letter_digits[letter]["available digits"].append(solution[letter]).sort()
                    letter_digits[letter]["used digits"] = []
                    solution[letter] = None
                    letter_index -= 2 # TODO: What if letter index < 0? Backtrack to previous operation
            letter_index += 1

        carry[operation_index+1] = operation_sum % 10
        operation_result = operation_sum // 10

        if solution[operations[operation_index]["letter"]] is None:
            if operation_result not in solution.values(): # Add operation result to solution
                letter_digits[letter]["available digits"].pop(operation_result)
                letter_digits[letter]["used digits"].append(operation_result)
                for l in letters:
                    letter_digits[l]["available"].remove(operation_result)
                solution[operations[operation_index]["letter"]] = operation_result
                operation_index += 1
            else: # TODO: Backtrack letter
                letter_index -= 1
        elif solution[operations[operation_index]["letter"]] != operation_result: # TODO: Backtrack operation?
            pass
        else:
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
