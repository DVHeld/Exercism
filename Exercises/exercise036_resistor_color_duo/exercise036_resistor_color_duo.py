"""Resistor Color Duo exercise"""

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

def value(colors):
    """The sum of the resistances of first two colors in the given colors list.
 
    :param list[str] colors: The color list.
    :return int: The combined resistance.
    """
    return int(str(COLOR_RESISTANCES[colors[0]]) + str(COLOR_RESISTANCES[colors[1]]))
