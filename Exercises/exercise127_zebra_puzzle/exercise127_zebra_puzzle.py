"""Zebra Puzzle exercise"""

BLUE, GREEN, IVORY, RED, YELLOW = range(5)
COLORS = ("Blue", "Green", "Ivory", "Red", "Yellow")
ENG, JAP, NOR, SPA, UKR = range(5)
NATIONALITIES = ("Englishman", "Japanese", "Norwegian", "Spaniard", "Ukrainian")
CHESS, DANCE, FOOT, PAINT, READ = range(5)
HOBBIES = ("Chess", "Dancing", "Football", "Painting", "Reading")
DOG, FOX, HORSE, SNAIL, ZEBRA = range(5)
PETS = ("Dog", "Fox", "Horse", "Snail", "Zebra")
COFFEE, MILK, ORANGE_JUICE, TEA, WATER = range(5)
BEVERAGES = ("Coffee", "Milk", "Orange juice", "Tea", "Water")
COLOR, NATIONALITY, HOBBY, PET, BEVERAGE = range(5)
ATTRIBUTES = ("Color", "Nationality", "Hobby", "Pet", "Beverage")

def _check_constraints(houses):
    if len(houses) > 0 and houses[0][NATIONALITY] != NOR:
        return False
    if len(houses) > 2 and houses[2][BEVERAGE] != MILK:
        return False
    for house_no, house in enumerate(houses):
        if house[COLOR] == YELLOW and house[HOBBY] != PAINT:
            return False
        if house[COLOR] == GREEN and house[BEVERAGE] != COFFEE:
            return False
        if house[NATIONALITY] == ENG and house[COLOR] != RED:
            return False
        if house[NATIONALITY] == SPA and house[PET] != DOG:
            return False
        if house[NATIONALITY] == UKR and house[BEVERAGE] != TEA:
            return False
        if house[NATIONALITY] == JAP and house[HOBBY] != CHESS:
            return False
        if house[HOBBY] == FOOT and house[BEVERAGE] != ORANGE_JUICE:
            return False
        if house[HOBBY] == DANCE and house[PET] != SNAIL:
            return False
        if house[HOBBY] == READ:
            if (house_no < len(houses) - 1 and houses[house_no + 1][PET] != FOX) and \
               (house_no > 0 and houses[house_no - 1][PET] != FOX):
                return False
        if house[NATIONALITY] == NOR:
            if (house_no < len(houses) - 1 and houses[house_no + 1][COLOR] != BLUE) or \
               (house_no > 0 and houses[house_no - 1][COLOR] != BLUE):
                return False
        if house[HOBBY] == PAINT:
            if (house_no < len(houses) - 1 and houses[house_no + 1][PET] != HORSE) or \
               (house_no > 0 and houses[house_no - 1][PET] != HORSE):
                return False
        if len(houses) > 1:
            if houses[house_no][COLOR] == GREEN and houses[house_no - 1][COLOR] != IVORY:
                return False
    return True

def _solve(houses=[],
           colors=None,
           nationalities=None,
           hobbies=None,
           pets=None,
           beverages=None):

    if len(houses) == 5:
        return houses
    if colors is None:
        colors = set(range(5))
        nationalities = set(range(5))
        hobbies = set(range(5))
        pets = set(range(5))
        beverages = set(range(5))
    for color in colors:
        for nationality in nationalities:
            for hobby in hobbies:
                for pet in pets:
                    for beverage in beverages:
                        house = (color, nationality, hobby, pet, beverage)
                        combination = houses + [house]
                        if _check_constraints(combination):
                            result = _solve(
                                combination,
                                colors - {color},
                                nationalities - {nationality},
                                hobbies - {hobby},
                                pets - {pet},
                                beverages - {beverage}
                            )
                            if result:
                                return result
    return False

SOLUTION = _solve()

def drinks_water():
    """Returns the nationality of the person that drinks water.
 
    :return str: The nationality.
    """

    if not SOLUTION:
        return "No solution found"
    for house in SOLUTION:
        if house[BEVERAGE] == WATER:
            return NATIONALITIES[house[NATIONALITY]]

def owns_zebra():
    """Return the nationality of the person that owns the zebra.
 
    :return str: The nationality
    """

    if not SOLUTION:
        return "No solution found"
    for house in SOLUTION:
        if house[PET] == ZEBRA:
            return NATIONALITIES[house[NATIONALITY]]
