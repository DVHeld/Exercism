"""Series exercise"""

from re import match

def slices(series, length,/):
    """Creates a list of slices of the given length from the given series of digits.
 
    :param str series: The digit series.
    :param int length: The slice length.
    :return [str]: The list of slices.
    """

    if not isinstance(series, str) or match(r".*\D+.*", series):
        raise TypeError("input series must be a string of integers")
    if not isinstance(length, int):
        raise TypeError("input length must be an integer")
    if not length:
        raise ValueError("slice length cannot be zero")
    if length < 0:
        raise ValueError("slice length cannot be negative")
    if not series:
        raise ValueError("series cannot be empty")
    if length > len(series):
        raise ValueError("slice length cannot be greater than series length")

    def _slices(series, length):
        return [series[:length], *_slices(series[1:], length)] if len(series) >= length else []

    return _slices(series, length)
