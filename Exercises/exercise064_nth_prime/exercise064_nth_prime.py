"""Nth Prime exercise"""

def prime(number,/):
    """The prime number with the given ordinality.
 
    This function utilizes trial division.
 
    :param int number: The ordinality of the prime number.
    :raises ValueError: Raised if there's no input.
    :raises TypeError: Raised if the input is not a positive integer.
    :raises ValueError: Raised if the given ordinality is zero. 
    :return int: The prime number.
    """

    if number is None:
        raise ValueError("no input given")
    if not isinstance(number, int) or number < 0:
        raise TypeError("input is not a positive integer")
    if not number:
        raise ValueError('there is no zeroth prime')

    counter = 1
    current = 1
    factor = 2
    divisors = 0
    while counter <= number:
        current += 1
        for factor in range(2,int((current)**(1/2))+1):
            if current % (factor) == 0:
                divisors += 1
        if divisors == 0:
            counter += 1
        divisors = 0
    return current
