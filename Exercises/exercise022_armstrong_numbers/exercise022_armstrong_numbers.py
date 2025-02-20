"""Armstrong Numbers exercise"""

def is_armstrong_number(number):
    """Determines if the given number is Armstrong.
 
    :param number: int - The number.
    :return: bool - True if it's an Armstrong number.
    """

    result = 0
    str_number = str(number)
    length = len(str_number)
    for digit in str_number:
        result += int(digit)**length
    return number == result
