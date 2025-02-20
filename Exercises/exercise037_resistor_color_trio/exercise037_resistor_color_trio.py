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

SUFFIXES = {
    0: [" ohms", 0],
    1: [" ohms", 0],
    2: [" ohms", 0],
    3: [" kiloohms", 3],
    4: [" kiloohms", 3],
    5: [" kiloohms", 3],
    6: [" megaohms", 6],
    7: [" megaohms", 6],
    8: [" megaohms", 6],
    9: [" gigaohms", 9],
   10: [" gigaohms", 9]
}

def label(colors):
    """The the resistance based on the three colors in the given colors list.
 
    :param list[str] colors: The color list.
    :return int: The combined resistance.
    """

    value = 10 ** COLOR_RESISTANCES[colors[2]] *\
           (10 * COLOR_RESISTANCES[colors[0]] + COLOR_RESISTANCES[colors[1]])
    order_of_magnitude = len(str(value))-1
    resistance = value/10**SUFFIXES[order_of_magnitude][1]
    return str(round(resistance)) + SUFFIXES[order_of_magnitude][0]
