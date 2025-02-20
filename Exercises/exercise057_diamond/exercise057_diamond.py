"""Diamond exercise"""

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def rows(letter):
    """Creates a diamond kata reaching the given letter.
 
    :param str letter: The letter that the diamond reaches.
    :raises TypeError: Raised when the input is not a string.
    :raises ValueError: Raised when the input is mot an UPPERCASE letter.
    :raises ValueError: Raised when the input is more than one letter.
    :return list[str]: The diamond kata in the form of a list of strings.
    """

    if not isinstance(letter, str):
        raise TypeError("Input must be one UPPERCASE letter.")
    if letter not in ALPHABET:
        raise ValueError("Input must be one UPPERCASE letter.")
    if len(letter) != 1:
        raise ValueError("Input must be one UPPERCASE letter.")

    lines = []
    dimension = ALPHABET.index(letter)+1
    for row in range(2*dimension-1):
        lines.append("")
        if row < dimension:
            lines[row] += " " * (dimension-row-1)        +\
                          f"{ALPHABET[row]}"             +\
                          " " * (2*row-1)                +\
                          f"{ALPHABET[row]}" * bool(row) +\
                          " " * (dimension-row-1)
        else:
            lines[row] += " " * (row-dimension+1)          +\
                          f"{ALPHABET[2*dimension-row-2]}" +\
                          " " * (2*(2*dimension-row-1)-3)  +\
                          f"{ALPHABET[2*dimension-row-2]}" * bool(2*dimension-row-2) +\
                          " " * (row-dimension+1)
    return lines
