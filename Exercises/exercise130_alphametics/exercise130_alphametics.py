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
    solution = {letter: None for letter in set(''.join(result).join(addends))}
    digits = list(reversed(list(range(10))))
    letter_digits = {letter: {"available digits": digits[:], "used digits": [], "backtrack": False}
                     for letter in letters}
    carry = [0] * max_len
    backtracked = False

    testing_counter = 0 # TODO: delete
    testing_counter_limit = 10 # TODO: delete

    operation_index = 0
    letter_index = 0
    while operation_index < max_len:
        print(f"A | oi: {operation_index} {operations[operation_index]}")
        operation_sum = 0
        if not backtracked:
            letter_index = 0
        backtracked = False
        while letter_index < len(operations[operation_index]):
            letter = operations[operation_index]["operation"][letter_index]
            print(f"A1 | oi: {operation_index} | li: {letter_index} {letter}")
            if solution[letter] is None: # Assign next digit
                print(f"A1A | oi: {operation_index} | li: {letter_index} {letter} {solution[letter]}")
                if len(letter_digits[letter]["available digits"]): # Add next digit to solution
                    print(f"A1A1 | {letter} ad: {letter_digits[letter]["available digits"]}")
                    digit = letter_digits[letter]["available digits"].pop()
                    letter_digits[letter]["used digits"].append(digit)
                    print(f"A1A1 | d: {digit} | lud: {letter_digits[letter]["used digits"]}")
                    for l in letters:
                        if l != letter:
                            # print(f"A1A1A | l: {l} | letter: {letter} | ad: {letter_digits[l]["available digits"]}")
                            if solution[letter] is not None:
                                # print(f"A1A1A1 | l: {l} | letter: {letter} | sl: {solution[letter]}")
                                letter_digits[l]["available digits"].append(solution[letter])
                                # print(letter_digits[l]["available digits"])
                                letter_digits[l]["available digits"].sort()
                            letter_digits[l]["available digits"].remove(digit)
                        # print(f"A1A1B | l: {l} | letter: {letter} | ad: {letter_digits[l]["available digits"]}")
                    print("A1A2")
                    solution[letter] = digit
                    operation_sum += solution[letter]
                else: # Backtrack
                    print("A1B1")
                    letter_digits[letter]["available digits"] = letter_digits[letter]["used digits"]
                    letter_digits[letter]["available digits"].append(solution[letter])
                    letter_digits[letter]["available digits"].sort()
                    letter_digits[letter]["used digits"] = []
                    solution[letter] = None
                    letter_index -= 2
                    print("A1B2")
                    if letter_index < 0: # Backtrack to previous operation
                        print("A1B2A")
                        letter_index = addend_amount
                        operation_index -= 1
                    print("A1B3")
            print("A2")
            letter_index += 1
            # print(f"li: {letter_index} | l: {letter} | s: {solution}")
            # testing_counter+=1 # TODO: Delete
            # if testing_counter > testing_counter_limit: # TODO: Delete
            #     return False # TODO: Delete
            print("A3")

        print("B")
        carry[operation_index+1] = operation_sum % 10
        operation_result = operation_sum // 10

        print(f"C | c: {carry} | opr: {operation_result}")
        if solution[operations[operation_index]["result"]] is None:
            print(f"C1 | {list(solution.values())}")
            if operation_result not in solution.values(): # Add operation result to solution
                print("C1A")
                letter_digits[letter]["available digits"].pop(operation_result)
                letter_digits[letter]["used digits"].append(operation_result)
                print("C1B")
                for l in letters:
                    print("C1B1")
                    letter_digits[l]["available digits"].remove(operation_result)
                print("C1C")
                solution[operations[operation_index]["result"]] = operation_result
                operation_index += 1
                print("C1D")
            else: # TODO: Backtrack letter
                print("C2A")
                for l in letters:
                    if l != letter:
                        letter_digits[l]["available digits"].append(solution[letter])
                        letter_digits[l]["available digits"].sort()
                        letter_digits[l]["available digits"].reverse()
                solution[letter] = None
                    
                # letter_digits[letter]["available digits"] = letter_digits[letter]["used digits"]
                # letter_digits[letter]["used digits"] = []
                # letter_index -= 2
                letter_index -= 1
                backtracked = True
                print("C2B")
            print("C2")
        elif solution[operations[operation_index]["letter"]] != operation_result: # TODO: Backtrack op
            print("D1")
            operation_index -= 1
            letter_index = addend_amount
        else:
            print("E1")
            operation_index += 1
        print("F")
        print(f"oi: {operation_index}")
        testing_counter+=1 # TODO: Delete
        if testing_counter > testing_counter_limit: # TODO: Delete
            return False # TODO: Delete
    print("G")
    return dict(solution)

######################### TESTING AREA #########################

mypuzzle = "SEND + MORE == MONEY"
print(solve(mypuzzle))
# myaddends = ["SEND", "MORE"]
# myresult = "MONEY"
# my_max_len = max(max(len(myaddend) for myaddend in myaddends), len(myresult))
# print(my_max_len)
# myletters = set(''.join(myresult).join(myaddends))
# print({letter:list(range(10)) for letter in set("QWERTY")})
# print(_extract_operations(["SEND", "MORE"], "MONEY"))
# print(reversed(list(range(10))))
# print({letter: None for letter in set(''.join(myresult).join(myaddends))})
