"""Change exercise"""

def find_fewest_coins(coins, target):
    """Makes change to the target amount with the smallest amout of coins available.
 
    :param list[float] coins: The list of availeble coin values.
    :param float target: The target amount to make change to.
    :raises ValueError: Raised when there's no coin input.
    :raises TypeError: Raised when the coin input is not a list.
    :raises TypeError: Raised when the coin values are not integers or floats.
    :raises ValueError: Raised when coin values are zero or negative.
    :raises ValueError: Raised when there's no target input.
    :raises TypeError: Raised when the target is not an integer or a float.
    :raises ValueError: Raised when the target is negative.
    :raises ValueError: Raised when there's no possible combination of coins to make the required
                        change.
    :return list[float]: The list of coins to make the required change.
    """

    if not coins:
        raise ValueError("No coin input.")
    if not isinstance(coins, list):
        raise TypeError("Coins must be in a list.")
    for coin in coins:
        if not isinstance(coin, int) and not isinstance(coin, float):
            raise TypeError("Coins must be integers or floats.")
        if coin <= 0:
            raise ValueError("Coins must have a positive value.")
    if target is None:
        raise ValueError("No target input.")
    if not isinstance(target, int) and not isinstance(target, float):
        raise TypeError("Target must be an integer or a float.")
    if target < 0:
        raise ValueError("target can't be negative")

    if not target:
        return []
    change_sets = [[0, []]]
    values = []
    while change_sets:
        change_temp = change_sets + []
        for change in change_temp:
            for coin in coins:
                if change[0] + coin in values:
                    continue
                if change[0] + coin <= target:
                    current = [change[0] + 0, change[1] + []]
                    current[0] = current[0] + coin
                    current[1].append(coin)
                    if current[0] == target:
                        return sorted(current[1])
                    change_sets.append(current)
                    values.append(current[0])
                else:
                    break
            change_sets.remove(change)
    raise ValueError("can't make target with given coins")
