"""Sublist exercise"""

SUBLIST = 1
SUPERLIST = 2
EQUAL = 3
UNEQUAL = 4

def sublist(list_1, list_2):
    """Determines is the first list is a sublist or superlist of the second, or if they are equal
    or unequal.
 
    The lists are equal when all their elements match eachother. A list is a superlist when it
    contains the other. A list is a sublist when it is contained in the other. Otherwise, they
    are unequal.
 
    :param list[] list_1: The first list.
    :param list[] list_2: The second list.
    :raises TypeError: Raised if any of the arguments provided is not a list.
    :return int: The kind of list. 1 means sublist, 2 means superlist, 3 means equal and 4 means
                 unequal.
    """

    if not isinstance(list_1, list) or not isinstance(list_2, list):
        raise TypeError("Both inputs must be lists.")
    if list_1 == list_2:
        return EQUAL
    if not list_1:
        return SUBLIST
    if not list_2:
        return SUPERLIST
    str_1 = "".join(f"{str(x)}]" for x in list_1)
    str_2 = "".join(f"{str(x)}]" for x in list_2)
    if str_2 in str_1:
        return SUPERLIST
    return SUBLIST if str_1 in str_2 else UNEQUAL