"""Yacht exercise"""

YACHT = 1
ONES = 2
TWOS = 3
THREES = 4
FOURS = 5
FIVES = 6
SIXES = 7
FULL_HOUSE = 8
FOUR_OF_A_KIND = 9
LITTLE_STRAIGHT = 10
BIG_STRAIGHT = 11
CHOICE = 12

def score(dice, category):
    """Calculates the score.
 
    :param list[int] dice: The dice numbers.
    :param int category: The selected scoring category.
    :raises ValueError: Raised when there are missing inputs.
    :raises TypeError: Raised when the dice input is not a list.
    :raises TypeError: Raised when there are dice that are not integers.
    :raises ValueError: Raised when there are dice numbers out of the 1-6 range.
    :raises ValueError: Raised when the dice amount is different than 5.
    :return int: The score.
    """

    if dice is None or category is None:
        raise ValueError("Missing input.")
    if not isinstance(dice, list):
        raise TypeError("Dice must be a list.")
    for d in dice:
        if not isinstance(d, int):
            raise TypeError("All dice must be integers.")
        if 1 > d > 6:
            raise ValueError("Dice value out of range.")
    if len(dice) != 5:
        raise ValueError("There must be 5 dice.")

    if category == YACHT and dice.count(dice[0]) == 5:
        return 50
    if category == SIXES:
        return dice.count(6)*6
    if category == FIVES:
        return dice.count(5)*5
    if category == FOURS:
        return dice.count(4)*4
    if category == THREES:
        return dice.count(3)*3
    if category == TWOS:
        return dice.count(2)*2
    if category == ONES:
        return dice.count(1)*1
    if category == CHOICE:
        return sum(dice)
    dice = sorted(dice)
    if category == BIG_STRAIGHT and dice == [2,3,4,5,6]:
        return 30
    if category == LITTLE_STRAIGHT and dice == [1,2,3,4,5]:
        return 30
    if category == FOUR_OF_A_KIND:
        if dice.count(dice[0]) >= 4:
            return dice[0] * 4
        if dice.count(dice[-1]) >= 4:
            return dice[-1] * 4
    if category == FULL_HOUSE and \
                   ((dice.count(dice[0]) == 2 and dice.count(dice[-1]) == 3) or
                    (dice.count(dice[0]) == 3 and dice.count(dice[-1]) == 2)):
        return sum(dice)
    return 0
