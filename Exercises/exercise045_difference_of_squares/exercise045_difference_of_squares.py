"""Difference of Squares exercise"""

def square_of_sum(number):
    """Returns the square of the sum of the first given numbers.
 
    :param int number: The maximum number in the sum.
    :return int: The result.
    """

    return sum(range(1,number+1))**2

def sum_of_squares(number):
    """Returns the sum of the squares of the first given numbers.
 
    :param int number: The maximum number in the sum.
    :return int: The result.
    """    

    return sum(n**2 for n in range(1, number+1))

def difference_of_squares(number):
    """The difference between the square of the sum and the sum of the squares.
 
    :param int number: The maximum number in the sums.
    :return int: The result.
    """

    return square_of_sum(number) - sum_of_squares(number)
