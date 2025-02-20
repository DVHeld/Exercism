"""Palindrome Products exercise"""

def is_palindrome(number):
    """Checks if the number is a palindrome."""

    return str(number) == str(number)[::-1]

def largest(min_factor, max_factor):
    """Given a range of numbers, find the largest palindromes which
       are products of two numbers within that range.
 
    :param min_factor: int with a default value of 0
    :param max_factor: int
    :return: tuple of (palindrome, iterable).
             Iterable should contain both factors of the palindrome in an arbitrary order.
    """

    if min_factor > max_factor:
        raise ValueError("min must be <= max")

    result = (None, [])
    min_factor -= 1
    max_palindrome = 0
    for factor_a in range(max_factor, min_factor, -1):
        for factor_b in range(factor_a, min_factor, -1):
            product = factor_a * factor_b
            if product < max_palindrome:
                break
            if is_palindrome(product):
                if product > max_palindrome:
                    result = (product, [tuple(sorted((factor_a, factor_b)))])
                    max_palindrome = product
                else:
                    result[1].append(tuple(sorted((factor_a, factor_b))))
    return result

def smallest(min_factor, max_factor):
    """Given a range of numbers, find the smallest palindromes which
    are products of two numbers within that range.

    :param min_factor: int with a default value of 0
    :param max_factor: int
    :return: tuple of (palindrome, iterable).
    Iterable should contain both factors of the palindrome in an arbitrary order.
    """

    if min_factor > max_factor:
        raise ValueError("min must be <= max")

    result = (None, [])
    max_factor += 1
    min_palindrome = max_factor**2
    for factor_a in range(min_factor, max_factor):
        for factor_b in range(factor_a, max_factor):
            product = factor_a * factor_b
            if product > min_palindrome:
                break
            if is_palindrome(product):
                if product < min_palindrome:
                    result = (product, [tuple(sorted((factor_a, factor_b)))])
                    min_palindrome = product
                else:
                    result[1].append(tuple(sorted((factor_a, factor_b))))
    return result
