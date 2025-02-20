"""Binary Search exercise"""

def find(search_list, value):
    """Finds the position of the song in the list.
 
    :param list[int] search_list: The song list.
    :param int value: The song to be found.
    :return int: The position of the song within the list.
    """

    indices = list(range(len(search_list)))
    middle_index = len(indices)//2
    while indices:
        if search_list[indices[middle_index]] == value:
            return indices[middle_index]
        if search_list[indices[middle_index]] > value:
            indices = indices[:middle_index]
        elif search_list[indices[middle_index]] < value:
            indices = indices[middle_index+1:]
        middle_index = len(indices)//2
    raise ValueError("value not in array")
