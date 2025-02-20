"""All Your Base exercise"""

def rebase(input_base, digits, output_base):
    """Changes a number from one base to another.
 
    The number must be given as a list of its digits in base 10,
    ie. a hexadecimal C must be input as 12.
 
    :param int input_base: The input number's base.
    :param list[int] digits: The input digits in base 10.
    :param int output_base: The desired output base.
    :raises ValueError: Raised when the input base is less than 2.
    :raises ValueError: Raised when the output base is less than 2.
    :raises ValueError: Raised when a digit is less than 0 or greater than the input base.
    :return list[int]: The list of digits in base 10 of the number in the target base.
    """

    if input_base < 2:
        raise ValueError("input base must be >= 2")
    if output_base < 2:
        raise ValueError("output base must be >= 2")

    input_number = 0
    digits.reverse()
    for magnitude, digit in enumerate(digits):
        if digit >= input_base or digit < 0:
            raise ValueError("all digits must satisfy 0 <= d < input base")
        input_number += digit * (input_base**magnitude)
    output_digits = []
    while True:
        output_digits.append(input_number%output_base)
        input_number = input_number//output_base
        if not input_number:
            break
    output_digits.reverse()
    return output_digits
