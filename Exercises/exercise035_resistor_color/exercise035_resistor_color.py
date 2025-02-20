"""Resistor Color exercise"""

COLOR_RESISTANCES = {
    "black" : 0,
    "brown" : 1,
    "red"   : 2,
    "orange": 3,
    "yellow": 4,
    "green" : 5,
    "blue"  : 6,
    "violet": 7,
    "grey"  : 8,
    "white" : 9
    }

def color_code(color):
    """The resistance represented by the passed color.
 
    :param str color: The color.
    :return int: The resistance.
    """

    return COLOR_RESISTANCES[color]

def colors():
    """A list of the colors ordered by resistance, from lower to higher.
 
    :return list: The ordered color list.
    """

    return sorted(COLOR_RESISTANCES, key=COLOR_RESISTANCES.get)
