"""Perfect Numbers exercise"""

def classify(number):
    """ A perfect number equals the sum of its positive divisors.
 
    :param number: int a positive integer.
    :return: str the classification of the input integer.
    """

    if number < 1 or type(number) != int:
        raise ValueError("Classification is only possible for positive integers.")
    counter = 1
    result = 0
    while counter < number:
        if number % counter == 0:
            result += counter
        counter += 1
    if result == number:
        return "perfect"
    if result < number:
        return "deficient"
    return "abundant"
