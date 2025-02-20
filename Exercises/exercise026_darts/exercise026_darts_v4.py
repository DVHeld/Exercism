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
    This implementation utilizes an arbitrarily extensible and
    automatically sorted dictionary. For this to work, the name of the
    zones' names must start by a number in ascending order, starting from
    the innermost zone.
    """
    zones = {
        "1_inner": {"radius": 1, "score": 10},
        "2_middle": {"radius": 5, "score": 5},
        "3_outer": {"radius": 10, "score": 1}
    }
    zones = dict(sorted(zones.items()))
    coordinate = x**2 + y**2
    for zone in zones.values():
        if coordinate <= zone["radius"]**2:
            return zone["score"]
    return 0
