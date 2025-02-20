"""Prime Factors exercise"""

def factors(value):
    """Generates the list of prime factors of the given integer value.
 
    :param int value: The value.
    :return list[int]: The list of prime factors.
    """

    if not isinstance(value, int) or not value or value == 1:
        return []
    number = 2
    while value % number != 0:
        number += 1
    return [number, *factors(value//number)]
