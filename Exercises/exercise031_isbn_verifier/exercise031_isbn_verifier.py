"""ISBN Verifier exercise"""

def is_valid(isbn):
    """Validates a ISBN code.
 
    :param str isbn: The ISBN code to validate.
    :return bool: True if it's a valid ISBN code, False otherwise.
    """

    isbn = isbn.replace("-","").lower()
    if not len(isbn) == 10 or\
       not isbn[:-1].isdigit() or\
       not (isbn[-1].isdigit() or isbn[-1] == "x"):
        return False
    validator = 0
    for digit in range(10):
        if digit == 9 and isbn[digit] == "x":
            validator += 10 * (10-digit)
        else:
            validator += int(isbn[digit]) * (10-digit)
    return True if validator % 11 == 0 else False
