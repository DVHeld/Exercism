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
    translated = ""
    while number:
        for index, numeral in enumerate(numerals):
            if number >= numeral[1]:
                translated += numeral[0]
                number -= numeral[1]
                break
            if number >= numeral[1] - numerals[index+2-index%2][1]:
                translated += numerals[index+2-index%2][0] + numeral[0]
                number -=  numeral[1] - numerals[index+2-index%2][1]
                break
            if index == 1:
                numerals = numerals[2:]
                break
    return translated
