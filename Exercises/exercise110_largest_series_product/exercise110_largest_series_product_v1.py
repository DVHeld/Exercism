"""Largest Series Product exercise"""

def largest_product(series, size):
    """Returns the largest product of all the series' contiguous subsets of the given size.
 
    :param str series: A string containing the series of digits.
    :param int size: The size of the subset to get the product of.
    :raises ValueError: Raised when there's a missing input.
    :raises TypeError: Raised when the series is not a string.
    :raises TypeError: Raised when the size is not an integer.
    :raises ValueError: Raised when the size is smaller that the series' length.
    :raises ValueError: Raised when the size is negative.
    :raises ValueError: Raised when the string contains non-digits.
    :return int: The largest product.
    """

    if series is None or size is None:
        raise ValueError("Missing input.")
    if not isinstance(series, str):
        raise TypeError("Series must be a string.")
    if not isinstance(size, int):
        raise TypeError("Size must be an integer.")
    if size > len(series):
        raise ValueError("span must be smaller than string length")
    if size < 0:
        raise ValueError("span must not be negative")

    max_product = 0
    while len(series) >= size:
        product = 1
        for number in series[:size]:
            if number not in "0123456789":
                raise ValueError("digits input must only contain digits")
            product *= int(number)
        max_product = max(max_product, product)
        series = series[1:]
    return max_product
