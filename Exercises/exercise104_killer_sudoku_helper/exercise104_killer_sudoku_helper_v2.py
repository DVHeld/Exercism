"""Killer Sudoku Helper exercise"""

from itertools import combinations as combi

def combinations(target, size, exclude):
    """Generates the possible combinations for the Killer Sudoku cages.
 
    Given a target number a cage size and a list of excluded digits, this function generates
    valid combinations of digits for those parameters.
 
    :param int target: The target number the digits must sum to.
    :param int size: The amount of digits in a cage.
    :param list[int] exclude: The list of numbers excluded because they're already in use.
    :raises ValueError: Raised when there is no target input.
    :raises TypeError: Raised when the target is not an integer.
    :raises ValueError: Raised when the target is out of the valid range (1-45).
    :raises ValueError: Raised when there is no size input.
    :raises TypeError: Raised when the size is not an integer.
    :raises ValueError: Raised when the size is out of range (1-9).
    :raises ValueError: Raised when there's no exclude input.
    :raises TypeError: Raised when the exclude input is not a list.
    :raises TypeError: Raised when a digit in the exclude list is not an integer.
    :raises ValueError: Raised when a digit in the exclude list is out of range (1-9).
    :return list[list[int]]: The list of valid combinations.
    """

    if target is None:
        raise ValueError("No target input.") 
    if not isinstance(target, int):
        raise TypeError("Target must be an integer not greater than 45.")
    if 0 >= target > 45:
        raise ValueError("Target must be an integer not greater than 45.")
    if size is None:
        raise ValueError("No size input.") 
    if not isinstance(size, int):
        raise TypeError("Size must be a positive integer not greater than 9.")
    if 0 >= size > 9:
        raise ValueError("Size must be a positive integer not greater than 9.")
    if exclude is None:
        raise ValueError("No exclude input.")
    if not isinstance(exclude, list):
        raise TypeError("The excluded digits must be in a list.")
    for digit in exclude:
        if not isinstance(digit, int):
            raise TypeError("The excluded digits must be positive integers not greater than 9.")
        if 0 >= digit > 9:
            raise ValueError("The excluded digits must be positive integers not greater than 9.")

    return [list(combo) for combo in combi(
                (digit for digit in range(1, min(target, 9) + 1) if digit not in exclude), size)
                if sum(combo) == target]
