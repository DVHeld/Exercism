"""DND Character exercise"""

from random import randrange

class Character:
    """A D&D character.
 
    This class generates and stores the different stats of a D&D character.
    """

    def __init__(self):
        self.strength = self.ability()
        self.dexterity = self.ability()
        self.constitution = self.ability()
        self.intelligence = self.ability()
        self.wisdom = self.ability()
        self.charisma = self.ability()
        self.hitpoints = 10 + modifier(self.constitution)
    
    def ability(self):
        """Rolls an ability's points.
 
        :return int: The total ability points.
        """

        return sum(sorted([randrange(1, 7) for x in range(4)])[1:])

def modifier(value=0):
    """Calculates the constitution modifier on the basis of the character's constitution score.
 
    :param int value: The character's constitution score. Defaults to 0.
    :return int: The constitution modifier.
    """

    if not isinstance(value, int):
        raise TypeError("Input must be an integer.")

    return (value-10)//2
