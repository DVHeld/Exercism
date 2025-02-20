"""Collatz Conjecture exercise"""

def steps(number):
    """Determines the amount of steps in a Collatz Conjecture test.
 
    :param number: int - The starting number.
    :return: int - The amount of steps needed to reach 1.
 
    This function tests the Collatz Conjecture for the given number
    and returns the number of steps needed to reach 1. It will return an
    error if the given number is not a positive integer.
    """

    if number < 1:
        raise ValueError("Only positive integers are allowed")
    if type(number) != int:
        raise TypeError("Only positive integers are allowed")

    counter = 0

    while number > 1:
        if number % 2 == 0:
            number = number/2
        else:
            number = 3 * number + 1
        counter += 1
    return counter
