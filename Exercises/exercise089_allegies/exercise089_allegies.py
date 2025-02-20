"""Allergies exercise"""

class Allergies:
    """A person's allergies."""

    all_allergies = ["cats", "pollen", "chocolate", "tomatoes", "strawberries", "shellfish",
                     "peanuts", "eggs"]

    def __init__(self, score):

        if not isinstance(score, int):
            raise TypeError("Score must be an integer.")
        if score < 0:
            raise ValueError("Score must not be negative.")

        score = str(bin(score))[2:].zfill(8)[-8:]
        self.allergy_list = []

        for index, item in enumerate(score):
            if item == "1":
                self.allergy_list.append(self.all_allergies[index])

    def allergic_to(self, item):
        """Confirms if the person is allergic to the given item.
 
        :param str item: The item to check.
        :raises TypeError: Raised if the item is not a string.
        :return bool: True if the person is allergic to the item, False otherwise.
        """

        if not isinstance(item, str):
            raise TypeError("Item must be a string.")

        return item in self.allergy_list

    @property
    def lst(self):
        """A list of the person's allergies.
 
        :return list[str]: The list of allergies.
        """

        return self.allergy_list
