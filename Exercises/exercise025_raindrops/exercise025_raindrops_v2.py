"""Raindrops exercise"""

def convert(number):
    """ Converts the number into the corresponding raindrop.
 
    :param number: int - The number.
    :return: str - The converted number.
 
    This function receives a number and converts it to a string according
    to the "raindrops" logic:
 
    If the number is divisible by 3, convert it to "Pling".
 
    If the number is divisible by 5, convert it to "Plang".
 
    If the number is divisible by 7, convert it to "Plong".
 
    If the number is divisible by more than one of the previous, convert it
    to the corresponding concatenation, in the previous order.
 
    If the number is not divisible by the previous, return the number
    itself as a string.
 
    This function uses an easily extendible dictionary-based algorithm.
    """

    raindrops = {3: "Pling", 5: "Plang", 7: "Plong"}
    result = ""
    not_divisible = True
    for factor, drop in raindrops.items():
        if number % factor == 0:
            result += drop
            not_divisible = False
    if not_divisible:
        return str(number)
    return result
