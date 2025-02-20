"""Phone Number exercise"""

from re import findall, sub

class PhoneNumber:
    """A phone number."""

    def __init__(self, number):
        if findall(r"[a-zA-Z]", number):
            raise ValueError("letters not permitted")
        if findall(r"[^\d\(\)+\-\s.]", number):
            raise ValueError("punctuations not permitted")
        self.number = sub(r"\D", "", number)
        if len(self.number) < 10:
            raise ValueError("must not be fewer than 10 digits")
        if len(self.number) > 11:
            raise ValueError("must not be greater than 11 digits")
        if len(self.number) == 11 and self.number[0] != "1":
            raise ValueError("11 digits must start with 1")
        if self.number[-7] == "0":
            raise ValueError("exchange code cannot start with zero")
        if self.number[-7] == "1":
            raise ValueError("exchange code cannot start with one")
        if self.number[-10] == "0":
            raise ValueError("area code cannot start with zero")
        if self.number[-10] == "1":
            raise ValueError("area code cannot start with one")
        if len(self.number) == 11:
            self.number = self.number[1:]
        self.area_code = self.number[:3]
        self.exchange_code = self.number[3:6]
        self.subscriber_number = self.number[6:]

    def pretty(self):
        """Formats the phone number.
 
        It follows the standard format: ({area code})-{exchange code}-{subscriber number}
        
        :return str: The formatted phone number.
        """

        return f"({self.area_code})-{self.exchange_code}-{self.subscriber_number}"
