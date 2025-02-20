"""Flatten Array exercise"""

def flatten(iterable):
    """Flattens the given array, discarding nulls.
 
    :param list[] iterable: The array to be flattened.
    :return list[]: The flattened array.
    """

    if iterable or iterable == 0:
        flattened_array = []
        if isinstance(iterable, list):
            for element in iterable:
                result = flatten(element)
                if result or result == 0:
                    if isinstance(result, list):
                        flattened_array.extend(result)
                    else:
                        flattened_array.append(result)
            return flattened_array
        return iterable
    return []
