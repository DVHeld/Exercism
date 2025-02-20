"""Luhn exercise"""

class Luhn:
    """Stores a card number and verifies if it's valid."""

    def __init__(self, card_num):
        self.card_num = card_num.replace(" ","")

    def valid(self):
        """Validates the card number.

        :return bool: True if the card is valid, False otherwise.
        """

        if not self.card_num.isnumeric():
            return False
        checksum = 0
        for index, number in enumerate(reversed(self.card_num)):
            temp = int(number)*(1+index%2)
            checksum += temp-9 if temp > 9 else temp
        return False if checksum%10 or self.card_num == "0" else True
