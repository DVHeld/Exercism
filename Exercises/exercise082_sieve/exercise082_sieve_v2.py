"""Sieve exercise"""

def primes(limit):
    """Returns a list of the prime numbers from 2 to the specified limit.
 
    :param int limit: The maximum number to consider. Must be higher than 0.
    :raises TypeError: Raised if the input is not an integer.
    :raises ValueError: Raised if the input is less than 1.
    :return list[int]: The list of prime numbers.
    """

    if not isinstance(limit, int):
        raise TypeError("Input must be an integer.")
    if limit < 1:
        raise ValueError("Input must be greater than 0.")

    primes_list = list(range(2, limit+1))
    for number in primes_list:
        for i in range(number, int(limit*1/2)+1):
            if number*i in primes_list:
                primes_list.remove(number*i)
    return primes_list
