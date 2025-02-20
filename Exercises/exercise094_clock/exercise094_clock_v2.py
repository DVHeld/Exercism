"""Clock exercise"""

class Clock:
    """A clock.
 
    Stores hour and minute. Can add, substract and compare.
    """

    def __init__(self, hour, minute):

        if hour is None or minute is None:
            raise ValueError("Missing input.")
        if not isinstance(hour, int) or not isinstance(minute, int):
            raise TypeError("Inputs must be integers.")

        self.hour = int((hour + minute / 60) % 24)
        self.minute = minute % 60

    def __repr__(self):

        return f"Clock({self.hour}, {self.minute})"

    def __str__(self):

        return f"{self.hour:02}:{self.minute:02}"

    def __eq__(self, other):

        if other is None:
            raise ValueError("Missing input.")
        if not isinstance(other, Clock):
            raise TypeError("Cannot compare wit non-Clock classes.")

        return self.__repr__() == other.__repr__()

    def __add__(self, minutes):

        if minutes is None:
            raise ValueError("Missing input.")
        if not isinstance(minutes, int):
            raise TypeError("Cannot add with non-integers.")

        self.__init__(self.hour, self.minute + minutes)
        return self.__str__()

    def __sub__(self, minutes):

        if minutes is None:
            raise ValueError("Missing input.")
        if not isinstance(minutes, int):
            raise TypeError("Cannot substract with non-integers.")

        self.__init__(self.hour, self.minute - minutes)
        return self.__str__()
