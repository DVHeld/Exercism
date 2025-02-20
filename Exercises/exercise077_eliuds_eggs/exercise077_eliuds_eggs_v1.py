"""Eliud's Eggs exercise"""

def egg_count(display_value):
    """Decodes the value and counts the eggs.
 
    :param int display_value: The value in the coop's display.
    :raises TypeError: Raised when the input is not an integer.
    :raises ValueError: Raised when the input is negative.
    :return int: The amount of eggs in the coop.
    """

    if not isinstance(display_value, int):
        raise TypeError("Input must be a positive integer.")
    if display_value < 0:
        raise ValueError("Input cannot be negative.")

    exponent = 0
    binary = []
    while display_value:
        binary.append(display_value%2)
        display_value //= 2
    return sum(binary)
