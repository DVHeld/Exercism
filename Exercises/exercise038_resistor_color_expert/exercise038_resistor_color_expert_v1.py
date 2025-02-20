"""Resistor Color Expert exercise"""

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
   10: [" gigaohms", 9],
   11: [" gigaohms", 9],
   12: [" teraohms", 9],
   13: [" teraohms", 9],
   14: [" teraohms", 9]
}

TOLERANCES = {
    "grey"  : " ±0.05%",
    "violet": " ±0.1%",
    "blue"  : " ±0.25%",
    "green" : " ±0.5%",
    "brown" : " ±1%",
    "red"   : " ±2%",
    "gold"  : " ±5%",
    "silver": " ±10%"
}

def resistor_label(colors):
    """The the resistance based on the colors in the given colors list.
 
    :param list[str] colors: The color list.
    :return int: The resistance.
    """

    color_amount = len(colors)
    if color_amount <= 2:
        resistance = 0
        for index in range(color_amount):
            resistance += 10 ** (color_amount - index) * COLOR_RESISTANCES[colors[index]]
        return f"{resistance:g} ohms"
    if color_amount == 3:
        value = 10 ** COLOR_RESISTANCES[colors[2]] *\
               (10 * COLOR_RESISTANCES[colors[0]] + COLOR_RESISTANCES[colors[1]])
        order_of_magnitude = len(str(value))-1
        resistance = value//10**SUFFIXES[order_of_magnitude][1]
        return f"{resistance:g}{SUFFIXES[order_of_magnitude][0]}"
    if color_amount >= 4:
        tolerance = TOLERANCES[colors.pop()]
        multiplier = COLOR_RESISTANCES[colors.pop()] - 1
        color_amount -= 2
        resistance = 0
        for index in range(color_amount):
            resistance += 10 ** (color_amount - index) * COLOR_RESISTANCES[colors[index]]
        resistance = round(10 ** multiplier * resistance)
        order_of_magnitude = len(str(resistance))-1
        resistance = resistance/10**SUFFIXES[order_of_magnitude][1]
        return f"{resistance:g}{SUFFIXES[order_of_magnitude][0]}{tolerance}"
