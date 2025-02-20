"""Pythagorean Triplet exercise"""

def triplets_with_sum(number,/):
    """Calculates the pythagorean triplets that sum the given number.
 
    :param int number: The number that the triplets must sum.
    :raises TypeError: Raised when the input is not an integer.
    :raises ValueError: Raised when the input is less than 1.
    :return list[list[int]]: The list of triplets.
    """

    if not isinstance(number, int):
        raise TypeError("Input must be an integer.")
    if number < 1:
        raise ValueError("Input must be greater than zero.")

    triplets = []
    for a in range(1, number//2):
        for b in range(a, (number-a)//2+1):
            c = number - a - b
            if a**2+b**2==c**2:
                triplets.append([a,b,c])
    return triplets
