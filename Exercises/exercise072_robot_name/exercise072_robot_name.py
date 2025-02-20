"""Robot Name exercise"""

from random import randrange

class Robot:
    """A robot"""

    _assigned_names = []
    __alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def __init__(self):
        while True:
            self.name = f"{self.__alpha[randrange(0,26)]}{self.__alpha[randrange(0,26)]}"+\
                        f"{randrange(0,9)}{randrange(0,9)}{randrange(0,9)}"
            if not self.name in self._assigned_names:
                self._assigned_names.append(self.name)
                break

    def reset(self):
        self.__init__()
