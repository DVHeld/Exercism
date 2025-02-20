"""Grains exercise"""

def square(number):
    """Returns the number of grains on the given square.
 
    :param square: int - The square's number.
 
    :return: int - The amount of grains.
 
    This function calculates the amount of grains on the given
    square of the checkerboard. It only accepts an integer
    between 1 and 64.
    """

    if not 1 <= number <= 64:
        raise ValueError("square must be between 1 and 64")
    if type(number) != int:
        raise TypeError("square number must be integer")
    return 2**(number-1)

def total():
    """Returns the total amount of grains on the checkerboard.
 
    :return: int - The amount of grains.
    """

    grains = 0
    for number in range(1, 65):
        grains += square(number)
    return grains
