"""Roman Numerals exercise"""

def roman(number, /):
    """Transforms a number to roman numerals.
 
    The number must be between 1 and 3999.
 
    :raises ValueError: Raised if there's no input.
    :raises TypeError: Raised if the input is not an integer.
    :raises ValueError: Raised if the input is out of the allowable range.
    :return str: The roman number.
    """

    I, V, X, L, C, D, M = 1, 5, 10, 50, 100, 500, 1000

    if number is None:
        raise ValueError("No input.")
    if not isinstance(number, int):
        raise TypeError("The input must be a positive integer between 1 and 3999.")
    if 0 > number >= 4000:
        raise ValueError("Only numbers from 1 to 3999 can be represented as roman numerals.")

    translated = ""
    while number - M >= 0:
        translated += "M"
        number -= M
    if number + C-M >= 0:
        translated += "CM"
        number += C-M
    if number - D >= 0:
        translated += "D"
        number -= D
    if number + C-D >= 0:
        translated += "CD"
        number += C-D
    while number - C >= 0:
        translated += "C"
        number -= C
    if number + X-C >= 0:
        translated += "XC"
        number += X-C
    if number - L >= 0:
        translated += "L"
        number -= L
    if number + X-L >= 0:
        translated += "XL"
        number += X-L
    while number - X >= 0:
        translated += "X"
        number -= X
    if number + I-X >= 0:
        translated += "IX"
        number += I-X
    if number - V >= 0:
        translated += "V"
        number -= V
    if number + I-V >= 0:
        translated += "IV"
        number += I-V
    while number - I >= 0:
        translated += "I"
        number -= I
    return translated
