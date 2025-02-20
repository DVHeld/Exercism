"""Wordy exercise"""

import re

def answer(question):
    """Answers the basic algebraic question.
 
    This function receives a question in the following form:
        "What is ## +((plus|minus|multiplied by|divided by) ##)
    It then calculates the given operations. If the syntax is incorrect, it
    raises a "syntax error". If the operation is unsupported or the question
    is malformed in other ways, it raises an "unknown operation" error.
 
    :param str question: The question to be calculated.
    :raises ValueError: "unknown operation" - Question malformed or unknown
    operation.
    :raises ValueError: "syntax error" - Question incorrectly formatted.
    :return float: The result of the asked question.
    """

    matches_pattern_1 = re.match(\
        r"(What is) -?\d+( (plus|minus|multiplied by|divided by) -?\d+)*\?", question)
    matches_pattern_2 = re.match(\
        r"(What is)( -?\d+)*(( (plus|minus|multiplied by|divided by))*( -?\d+)*)*\?", question)
    if matches_pattern_1:
        parsed_question = question\
                          .replace("?", "")\
                          .replace("What is ", "")\
                          .replace(" by", "")\
                          .split(" ")
        parsed_numbers = parsed_question[::2]
        for index, number in enumerate(parsed_numbers):
            parsed_numbers[index] = int(number)
        parsed_operations = parsed_question[1::2]
        result = parsed_numbers[0]
        for index, operation in enumerate(parsed_operations):
            if operation == "plus":
                result += parsed_numbers[index + 1]
            elif operation == "minus":
                result -= parsed_numbers[index + 1]
            elif operation == "multiplied":
                result = result * parsed_numbers[index + 1]
            elif operation == "divided":
                result = result / parsed_numbers[index + 1]
            else: raise ValueError("unknown operation")
        return result
    if matches_pattern_2:
        raise ValueError("syntax error")
    raise ValueError("unknown operation")
