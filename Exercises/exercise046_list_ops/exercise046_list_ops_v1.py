"""List Ops exercise"""

def append(list1, list2):
    """Adds the second list to the end of the first.
 
    :param list[] list1: The first list.
    :param list[] list2: The second list.
    :return list[]: The appended lists.
    """

    list2[:0] = list1
    return list2

def concat(lists):
    """Concatenates the lists contained within the given list.
 
    :param list[list[]] lists: A list of lists.
    :return list[]: The resulting list.
    """

    concat_lists = []
    for item in lists:
        concat_lists = append(concat_lists, item)
    return concat_lists

def filter(function, list):
    """Filters the given list using the given filtering function.
 
    :param lambda function: A function that evaluates a value into True or False.
    :param list[int] list: A list of numbers.
    :return list: The filtered list.
    """

    flist = []
    for item in list:
        if function(item):
            flist = append(flist, [item])
    return flist

def length(list):
    """Counts the amount of items contained in the given list.
 
    :param list[] list: The list.
    :return int: The amount of items.
    """

    counter = 0
    for item in list:
        counter += 1
    return counter

def map(function, list):
    """Applies the given function to each element on the given list.
 
    :param lambda function: The function.
    :param list[int] list: The list of numbers.
    :return list[int]: The resulting list.
    """

    mlist = []
    for item in list:
        mlist = append(mlist, [function(item)])
    return mlist

def foldl(function, list, initial):
    """Implements the fold left function.
 
    :param lambda function: The folding function.
    :param list[int] list1: The element list.
    :param int initial: The initial accumulator.
    :return int: The folded result.
    """

    if list:
        result = function(initial, list[0])
        for index in range(1,length(list)):
            result = function(result, list[index])
        return result
    return initial

def foldr(function, list, initial):
    """Implements the fold right function.
 
    :param lambda function: The folding function.
    :param list[int] list1: The element list.
    :param int initial: The initial accumulator.
    :return int: The folded result.
    """

    if list:
        list_length = length(list)-1
        result = function(initial, list[list_length])
        for index in range(list_length):
            result = function(result, list[list_length-index-1])
        return result
    return initial

def reverse(list):
    """Reverses the given list.
 
    :param list[] list1: The list.
    :return list[]: The reversed list.
    """

    rlist = []
    for item in list:
        rlist = append([item], rlist)
    return rlist
