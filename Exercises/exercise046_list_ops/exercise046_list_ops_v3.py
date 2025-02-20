"""List Ops exercise"""

def append(list1, list2):
    """Appends two lists of equal length.
 
    :param list[] list1: A list.
    :param list[] list2: Another list.
    :return list[]: The new combined list.
    """

    new_list = []
    if list1 and list2:
        new_list = [list1[0], *append(list1[1:], list2[:-1]), list2[-1]]
    elif list1:
        new_list = [list1[0], *append(list1[1:], [])]
    elif list2:
        new_list = [*append([], list2[:-1]), list2[-1]]
    return new_list

def concat(lists):
    """Concatenates the lists contained within the given list.
 
    :param list[list[]] lists: A list of lists.
    :return list[]: The resulting list.
    """

    concat_lists = []
    if lists:
        concat_lists = [*lists[0], *concat(lists[1:])]
    return concat_lists

def filter(function, list):
    """Filters the given list using the given filtering function.
 
    :param lambda function: A function that evaluates a value into True or False.
    :param list[int] list: A list of numbers.
    :return list: The filtered list.
    """

    flist = []
    if list:
        if function(list[0]):
            flist = [list[0], *filter(function, list[1:])]
        else:
            flist = [*filter(function, list[1:])]
    return flist

def length(list):
    """Counts the amount of items contained in the given list.
 
    :param list[] list: The list.
    :return int: The amount of items.
    """

    list_length = 0
    if list:
        list_length = 1 + length(list[1:])
    return list_length

def map(function, list):
    """Applies the given function to each element on the given list.
 
    :param lambda function: The function.
    :param list[int] list: The list of numbers.
    :return list[int]: The resulting list.
    """

    mlist = []
    if list:
        mlist = [function(list[0]), *map(function, list[1:])]
    return mlist

def foldl(function, list, initial):
    """Implements the fold left function.
 
    :param lambda function: The folding function.
    :param list[int] list: The element list.
    :param int initial: The initial accumulator.
    :return int: The folded result.
    """

    if list:
        return foldl(function, list[1:], function(initial, list[0]))
    return initial

def foldr(function, list, initial):
    """Implements the fold right function.
 
    :param lambda function: The folding function.
    :param list[int] list: The element list.
    :param int initial: The initial accumulator.
    :return int: The folded result.
    """

    if list:
        return foldr(function, list[:-1], function(initial, list[-1]))
    return initial

def reverse(list):
    """Reverses the given list.
 
    :param list[] list: The list.
    :return list[]: The reversed list.
    """

    rlist = []
    if list:
        rlist = [list[-1], *reverse(list[:-1])]
    return rlist
