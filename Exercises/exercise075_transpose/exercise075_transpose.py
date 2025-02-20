"""Transpose exercise"""

def transpose(text):
    """Transposes the given taxt.
 
    Pads to the left with spaces.
 
    :param str text: The string to be transposed.
    :raises ValueError: Raised when there's no input given.
    :raises TypeError: Raised when the input is not a string.
    :return str: The transposed string.
    """

    if text is None:
        raise ValueError("Input must not be empty.")
    if not isinstance(text, str):
        raise TypeError("Input must be a string.")

    matrix = text.replace(" ", "_").split("\n")
    transposed_text = ""

    for col_no in range(max(len(x) for x in matrix)):
        for row in matrix:
            if col_no > len(row)-1:
                transposed_text += " "
            else:
                transposed_text += row[col_no]
        transposed_text = transposed_text.rstrip().replace("_", " ") + "\n"
    return transposed_text[:-1]
