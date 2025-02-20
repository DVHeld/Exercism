"""Sum of Multiples exercise"""

def sum_of_multiples(limit, multiples):
    """Returns the amount of energy to be restored at the end of a level.
 
    :param int limit: The level that was completed.
    :param list[int] multiples: The value of the magical items collected.
    :return int: The amount of energy.
    """

    values_set = set()
    for item in multiples:
        level = limit - 1
        while level:
            if item and level % item == 0:
                values_set.add(level)
            level -= 1
    return sum(values_set)
