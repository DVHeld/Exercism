"""Square Root exercise"""

def square_root(number):
    """Calculates the integer square root of a positive integer number.
 
    :param int number: The radicand.
    :return int: The square root.
    """

    answer = 1
    while number != answer**2:
        answer += 1
    return answer
