"""Darts exercise"""

def score(x, y):
    """Determines the score of the shot.
 
    :param x: float - The x coordinate where the dart landed.
    :param y: float - The y coordinate where the dart landed.
 
    :return: int - The score.
 
    This function determines the score of a shot landing in the provided
    coordinates. If the dart lands within the inner circle, the score is
    10, if it lands within the middle ring the score is 5, if it lands
    within the outer ring the score is 1 and the score is 0 otherwise.
    """

    if x**2 + y**2 <= 1:
        return 10
    if x**2 + y**2 <= 5**2:
        return 5
    if x**2 + y**2 <= 10**2:
        return 1
    return 0
