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
    operations = [{"operation": "", "result": letter} for letter in reversed(result)]
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
    addend_amount = len(addends)
    letters = set(''.join(result).join(addends))
    solution = dict(sorted({letter: None for letter in set(''.join(result).join(addends))}.items())) # TODO: remove sorting
    digits = list(reversed(list(range(10))))
    letter_digits = {letter: {"available digits": digits[:], "used digits": [], "backtrack": 0}
                     for letter in letters}
    carry = [0] * max_len
    backtracked = False

    testing_counter = 0 # TODO: delete
    testing_counter_limit = 30 # TODO: delete

    operation_index = 0
    letter_index = 0
    while operation_index < max_len:
        if not backtracked:
            letter_index = 0
        backtracked = False
        while letter_index < len(operations[operation_index]):
            letter = operations[operation_index]["operation"][letter_index]
            if solution[letter] is None: # Assign next digit
                if len(letter_digits[letter]["available digits"]): # Add next digit to solution
                    digit = letter_digits[letter]["available digits"].pop()
                    letter_digits[letter]["used digits"].append(digit)
                    for l in letters:
                        if l != letter:
                            if solution[letter] is not None: # and solution[letter] in letter_digits[l]["available digits"]:
                                letter_digits[l]["available digits"].append(solution[letter])
                                letter_digits[l]["available digits"].sort()
                            if digit in letter_digits[l]["available digits"]:
                                letter_digits[l]["available digits"].remove(digit)
                    solution[letter] = digit
                else: # Backtrack
                    letter_digits[letter]["available digits"] = letter_digits[letter]["used digits"]
                    letter_digits[letter]["used digits"] = []
                    letter_digits[letter]["available digits"].sort()
                    letter_digits[letter]["available digits"].reverse()
                    letter_index -= 1
                    pl = operations[operation_index]["operation"][letter_index]
                    for l in letters:
                        if l != pl:
                            letter_digits[l]["available digits"].append(solution[pl])
                            letter_digits[l]["available digits"].sort()
                            letter_digits[l]["available digits"].reverse()
                    solution[pl] = None
                        
                    letter_index -= 1
                    backtracked = True
            letter_index += 1
            if letter_index < 0: # Backtrack to previous operation
                letter_index = addend_amount
                operation_index -= 1

        operation_sum = 0
        for l in operations[operation_index]["operation"]:
            operation_sum += solution[l]
        carry[operation_index+1] = operation_sum // 10
        operation_result = operation_sum % 10

        print(f"{testing_counter:0{len(str(testing_counter_limit))}} | {solution} | {operations[operation_index]["operation"]} = {operations[operation_index]["result"]}")
        if solution[operations[operation_index]["result"]] is None:
            if operation_result not in solution.values() and \
               operation_result in letter_digits[letter]["available digits"]: # Add operation result to solution
                letter_digits[letter]["available digits"].remove(operation_result)
                letter_digits[letter]["used digits"].append(operation_result)
                for l in letters:
                    if operation_result in letter_digits[l]["available digits"]:
                        letter_digits[l]["available digits"].remove(operation_result)
                solution[operations[operation_index]["result"]] = operation_result
                operation_index += 1
            else: # Backtrack letter
                for l in letters:
                    if l != letter:
                        letter_digits[l]["available digits"].append(solution[letter])
                        letter_digits[l]["available digits"].sort()
                        letter_digits[l]["available digits"].reverse()
                solution[letter] = None
                letter_index -= 1
                backtracked = True
        elif solution[operations[operation_index]["result"]] != operation_result: # Backtrack letter
            for l in letters:
                if l != letter:
                    letter_digits[l]["available digits"].append(solution[letter])
                    letter_digits[l]["available digits"].sort()
                    letter_digits[l]["available digits"].reverse()
            solution[letter] = None
            letter_index -= 1
            backtracked = True
        else:
            operation_index += 1

        testing_counter+=1 # TODO: Delete
        if testing_counter > testing_counter_limit: # TODO: Delete
            return False # TODO: Delete

    return dict(solution)

######################### TESTING AREA #########################

mypuzzle = "SEND + MORE == MONEY"
print(solve(mypuzzle))
# myaddends = ["SEND", "MORE"]
# myresult = "MONEY"
# print(_extract_operations(["SEND", "MORE"], "MONEY"))
