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
    solution = dict(sorted({letter: None for letter in set(''.join(result).join(addends))}.items()))
    digits = list(reversed(list(range(10))))
    letter_digits = {letter: {"available digits": digits[:], "used digits": [], "backtrack": False}
                     for letter in letters}
    carry = [0] * max_len
    backtracked = False

    testing_counter = 0 # TODO: delete
    testing_counter_limit = 200 # TODO: delete

    operation_index = 0
    letter_index = 0
    while operation_index < max_len:
        # print(f"A | oi: {operation_index} {operations[operation_index]}")
        if not backtracked:
            letter_index = 0
        backtracked = False
        # print(f"{testing_counter:0{len(str(testing_counter_limit))}} A | {solution}")
        while letter_index < len(operations[operation_index]):
            letter = operations[operation_index]["operation"][letter_index]
            # print(f"A1 | oi: {operation_index} | li: {letter_index} {letter}")
            if solution[letter] is None: # Assign next digit
                # print(f"A1A | oi: {operation_index} | li: {letter_index} {letter} {solution[letter]}")
                if len(letter_digits[letter]["available digits"]): # Add next digit to solution
                    # print(f"A1A1 | {letter} ad: {letter_digits[letter]["available digits"]}")
                    digit = letter_digits[letter]["available digits"].pop()
                    letter_digits[letter]["used digits"].append(digit)
                    # print(f"A1A1 | d: {digit} | lud: {letter_digits[letter]["used digits"]}")
                    for l in letters:
                        if l != letter:
                            # print(f"A1A1A | l: {l} | letter: {letter} | ad: {letter_digits[l]["available digits"]}")
                            if solution[letter] is not None: # and solution[letter] in letter_digits[l]["available digits"]:
                                # print(f"A1A1A1 | l: {l} | letter: {letter} | sl: {solution[letter]}")
                                letter_digits[l]["available digits"].append(solution[letter])
                                # print(letter_digits[l]["available digits"])
                                letter_digits[l]["available digits"].sort()
                            if digit in letter_digits[l]["available digits"]:
                                letter_digits[l]["available digits"].remove(digit)
                        # print(f"A1A1B | l: {l} | letter: {letter} | ad: {letter_digits[l]["available digits"]}")
                    # print("A1A2")
                    solution[letter] = digit
                    # operation_sum += solution[letter]
                else: # Backtrack
                    # print(f"A1B1 | {letter_digits[letter]["available digits"]} = {letter_digits[letter]["used digits"]}")
                    letter_digits[letter]["available digits"] = letter_digits[letter]["used digits"]
                    # print(f"A1B1 | {letter_digits[letter]["used digits"]} = {[]}")
                    letter_digits[letter]["used digits"] = []
                    # print(f"A1B1 | {letter_digits[letter]["available digits"]}.append({solution[letter]})")
                    # letter_digits[letter]["available digits"].append(solution[letter])
                    # print(f"A1B1 | {letter_digits[letter]["available digits"]}.sort()")
                    letter_digits[letter]["available digits"].sort()
                    # print(f"A1B1 | {letter_digits[letter]["available digits"]}.reverse()")
                    letter_digits[letter]["available digits"].reverse()
                    # print(f"A1B1 | {solution[letter]} = {None}")
                    # solution[letter] = None
                    # print(f"A1B1 | {letter_index} -= {2}")
                    letter_index -= 1
                    pl = operations[operation_index]["operation"][letter_index]
                    # print(f"A1B2 | {pl} {letter_digits[pl]["available digits"]}")
                    # letter_digits[pl]["used digits"].append(solution[pl])
                    # letter_digits[pl]["available digits"].append(solution[pl])
                    for l in letters:
                        if l != pl:
                            letter_digits[l]["available digits"].append(solution[pl])
                            letter_digits[l]["available digits"].sort()
                            letter_digits[l]["available digits"].reverse()
                        # print(f"A1B2A | {l} - {letter_digits[l]["available digits"]}")
                    solution[pl] = None
                        
                    # letter_digits[letter]["available digits"] = letter_digits[letter]["used digits"]
                    # letter_digits[letter]["used digits"] = []
                    # letter_index -= 2
                    letter_index -= 1
                    backtracked = True
                    # print("A1B3")
            # print(f"A2 | {letter_index} += {1}")
            letter_index += 1
            if letter_index < 0: # Backtrack to previous operation
                # print("A1B2A")
                letter_index = addend_amount
                operation_index -= 1
            # print(f"li: {letter_index} | l: {letter} | s: {solution}")
            # testing_counter+=1 # TODO: Delete
            # if testing_counter > testing_counter_limit: # TODO: Delete
            #     return False # TODO: Delete
            # print("A3")

        print(f"{testing_counter:0{len(str(testing_counter_limit))}} B | {solution}")
        # print("B")
        operation_sum = 0
        for l in operations[operation_index]["operation"]:
            operation_sum += solution[l]
        carry[operation_index+1] = operation_sum // 10
        operation_result = operation_sum % 10

        print(f"C | op: {operations[operation_index]["operation"]} = {operations[operation_index]["result"]} | os: {operation_sum} | c: {carry} | opr: {operation_result} | {solution[operations[operation_index]["result"]]} is None?")
        if solution[operations[operation_index]["result"]] is None:
            print(f"C1 | {operation_result} not in {list(solution.values())}?")
            if operation_result not in solution.values() and \
               operation_result in letter_digits[letter]["available digits"]: # Add operation result to solution
                # print("C1A")
                letter_digits[letter]["available digits"].remove(operation_result)
                letter_digits[letter]["used digits"].append(operation_result)
                # print("C1B")
                for l in letters:
                    # print(f"C1B1 | {letter_digits[l]["available digits"]}.remove({operation_result})")
                    if operation_result in letter_digits[l]["available digits"]:
                        letter_digits[l]["available digits"].remove(operation_result)
                # print("C1C")
                solution[operations[operation_index]["result"]] = operation_result
                operation_index += 1
                # print("C1D")
            else: # TODO: Backtrack letter
                # print("C2A")
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
                # print("C2B")
            # print("C2")
        elif solution[operations[operation_index]["result"]] != operation_result: # TODO: Backtrack
            # print("D1")
            operation_index -= 1
            letter_index = addend_amount
        else:
            # print("E1")
            operation_index += 1
        # print("F")
        # print(f"oi: {operation_index}")
        testing_counter+=1 # TODO: Delete
        if testing_counter > testing_counter_limit: # TODO: Delete
            return False # TODO: Delete

    # print("G")
    return dict(solution)

######################### TESTING AREA #########################

mypuzzle = "SEND + MORE == MONEY"
print(solve(mypuzzle))
# myaddends = ["SEND", "MORE"]
# myresult = "MONEY"
# print(_extract_operations(["SEND", "MORE"], "MONEY"))
