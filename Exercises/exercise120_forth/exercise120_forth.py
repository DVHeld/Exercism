"""Forth exercise"""

class StackUnderflowError(Exception):
    """Exception raised when Stack is not full.
       message: explanation of the error.
    """

    def __init__(self, message):

        self.message = message

def evaluate(input_data):
    """Returns the result of the Forth input statements.
 
    :param list[str] input_data: The list of statements to process.
    :raises TypeError: Raised when the input is not a list.
    :raises TypeError: Raised when the statements are not strings.
    :raises ValueError: Raised when the operation is not permitted.
    :raises ValueError: Raised when the operation is not defined.
    :raises StackUnderflowError: Raised when there are less operands available than those required
                                 for the operation.
    :raises ZeroDivisionError: Raised when there is a division by zero.
    :return list[int]: The result of the processed statements.
    """

    def _isnumber(word):

        return word.isdigit() or word.startswith("-") and word[1:].isdigit()

    if not isinstance(input_data, list):
        raise TypeError("Input must be a list.")

    result = []
    word_dict = {
        "+": "+",
        "-": "-",
        "*": "*",
        "/": "/",
        "dup": "dup",
        "drop": "drop",
        "swap": "swap",
        "over": "over",
        ":": ":",
        ";": ";"
    }

    for statement in input_data:
        if not isinstance(statement, str):
            raise TypeError("Statements must be strings.")
        statement = statement.casefold()
        if statement[0] == ":":
            statement_iterator = iter(statement.split())
            next(statement_iterator)
            word = next(statement_iterator)
            if _isnumber(word):
                raise ValueError("illegal operation")
            meaning = ""
            next_element = next(statement_iterator)
            while next_element != ";":
                if not _isnumber(next_element):
                    next_element = word_dict[next_element]
                meaning += next_element + " "
                next_element = next(statement_iterator)
            word_dict[word] = meaning[:-1]
        else:
            for word, meaning in word_dict.items():
                statement = " ".join([meaning if statement_word == word else statement_word
                                      for statement_word in statement.split()])
            for element in statement.split():
                if not _isnumber(element):
                    try:
                        element = word_dict[element]
                    except Exception as exc:
                        raise ValueError("undefined operation") from exc
                if _isnumber(element):
                    result.append(int(element))
                elif element in ["+", "-", "*", "/", "over", "swap"]:
                    if len(result) < 2:
                        raise StackUnderflowError("Insufficient number of items in stack")
                    operand_2 , operand_1 = result.pop(), result.pop()
                    if element == "+":
                        result.append(operand_1 + operand_2)
                    elif element == "-":
                        result.append(operand_1 - operand_2)
                    elif element == "*":
                        result.append(operand_1 * operand_2)
                    elif element == "/":
                        if operand_2 == 0:
                            raise ZeroDivisionError("divide by zero")
                        result.append(operand_1 // operand_2)
                    elif element == "swap":
                        result.extend((operand_2, operand_1))
                    elif element == "over":
                        result.extend((operand_1, operand_2, operand_1))
                elif element in ["dup", "drop"]:
                    if len(result) < 1:
                        raise StackUnderflowError("Insufficient number of items in stack")
                    operand = result.pop()
                    if element == "dup":
                        result.extend((operand, operand))
    return result
