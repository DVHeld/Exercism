"""Roman Numerals exercise"""

def roman(number, /):
    """Transforms a number to roman numerals.
 
    The number must be between 1 and 3999.
 
    :raises ValueError: Raised if there's no input.
    :raises TypeError: Raised if the input is not an integer.
    :raises ValueError: Raised if the input is out of the allowable range.
    :return str: The roman number.
    """

    if number is None:
        raise ValueError("No input.")
    if not isinstance(number, int):
        raise TypeError("The input must be a positive integer between 1 and 3999.")
    if 0 > number >= 4000:
        raise ValueError("Only numbers from 1 to 3999 can be represented as roman numerals.")

    numerals  = [("M", 1000), ("D", 500), ("C", 100), ("L", 50), ("X", 10), ("V", 5), ("I", 1)]
    translated, index, check = "", 0, 0
    while number:
        unit = number//numerals[index][1]
        if unit == 4:
            translated = (translated[:-1] if check else translated) +\
                         numerals[index][0] + numerals[index-1-check][0]
        else:
            translated += unit * numerals[index][0]
            check = unit%2
        number -= unit * numerals[index][1]
        index += 1
    return translated
