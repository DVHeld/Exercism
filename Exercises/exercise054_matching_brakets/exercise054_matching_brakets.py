"""Matching Brackets exercise"""

def is_paired(input_string):
    """Checks if the bracket string is correctly paires.
 
    :param str brackets: The bracket string.
    :return bool: True if the brackets are correctly paired, False otherwise.
    """

    brackets = ""
    filtered = filter(lambda char: char in "[]{}()", input_string)
    for bracket in filtered:
        print(f"bracket: {bracket}")
        brackets += bracket
        print(f"brackets: {brackets}")
    bracket_pairs = {")": "(", "]": "[", "}": "{"}
    bracket_stack = ""
    for bracket in brackets:
        if bracket in "({[":
            bracket_stack += bracket
        elif not bracket_stack or bracket_pairs[bracket] != bracket_stack[-1]:
            return False
        else:
            bracket_stack = bracket_stack[:-1]
    return not bool(bracket_stack)
