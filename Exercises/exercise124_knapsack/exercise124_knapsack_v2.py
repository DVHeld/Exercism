"""Knapsack exercise"""

from itertools import combinations as combs

def maximum_value(maximum_weight: int, items: list, /):
    """Calculates the maximum value that can be carried in a knapsack of the given capacity.
 
    :param int maximum_weight: The capacity of the knapsack.
    :param list[dict] items: A list of items as dictionaries containing their respective weights
                             and values.
    :raises ValueError: Raised when there is a missing input.
    :raises TypeError: Raised when the maximum weight is not an integer.
    :raises ValueError: Raised when the maximum weight is negative.
    :raises TypeError: Raised when the items are not in a list.
    :raises TypeError: Raised when the items are not dictionaries.
    :raises TypeError: Raised when the attributes are not integers.
    :raises ValueError: Raised when there are missing or malformed attributes.
    :return int: The maximum value that can be carried.
    """

    if maximum_weight is None or items is None:
        raise ValueError("Missing input.")
    if not isinstance(maximum_weight, int):
        raise TypeError("Maximum weight must be an integer.")
    if maximum_weight < 0:
        raise ValueError("Maximum weight cannot be negative.")
    if not isinstance(items, list):
        raise TypeError("Items must be in a list.")
    for item in items:
        if not isinstance(item, dict):
            raise TypeError("Items must be dictionaries.")
        try:
            if not isinstance(item["weight"], int) or not isinstance(item["value"], int):
                raise TypeError("Attributes must be integers.")
        except Exception as exc:
            raise ValueError("Missing or malformed attribute.") from exc

    max_value = 0
    for amount in range(len(items)):
        for combinations in combs(items,amount):
            if sum(item["weight"] for item in combinations) <= maximum_weight:
                max_value = max(sum(item["value"] for item in combinations), max_value)
    return max_value
