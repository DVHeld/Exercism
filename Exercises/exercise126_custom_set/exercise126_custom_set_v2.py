"""Custom Set exercise"""

from collections.abc import Iterable

class CustomSet:
    """A custom implementation of a set."""

    def __init__(self, elements=None, /):
        self._elements = []
        if elements is not None:
            if isinstance(elements, Iterable):
                if not isinstance(elements, str):
                    for element in elements:
                        self.add(element)
            else:
                self.add(elements)

    def isempty(self):
        """True if the set is empty, False otherwise."""

        return len(self) == 0

    def __contains__(self, element, /):

        return element in self._elements

    def issubset(self, other_set, /):
        """Checks if this set is a subset of the provided one."""

        self._isset(other_set)
        for element in self:
            if element not in other_set:
                return False
        return True

    def isdisjoint(self, other_set, /):
        """Checks if the sets are disjoint."""

        self._isset(other_set)
        for element in other_set:
            if element in self:
                return False
        return True

    def __eq__(self, other_set, /):

        self._isset(other_set)
        for element in self:
            if element not in other_set:
                return False
        for element in other_set:
            if element not in self:
                return False
        return True

    def add(self, element, /):
        """Adds the given element to the set."""

        if not element in self:
            self._elements.append(element)

    def intersection(self, other_set, /):
        """Returns the intersection of the sets."""

        self._isset(other_set)
        return CustomSet([element for element in other_set if element in self])

    def __sub__(self, other_set, /):

        self._isset(other_set)
        return CustomSet([element for element in self if element not in other_set])

    def __add__(self, other_set, /):

        self._isset(other_set)
        return CustomSet(list(self) + list(other_set))

    def __len__(self):

        return len(self._elements)

    def __iter__(self):

        yield from self._elements

    def _isset(self, other):

        if not isinstance(other, (set, CustomSet)):
            raise TypeError("Input must be a set.")
        return True

    def __str__(self):

        return "(" + ", ".join(f"'{element}'" if isinstance(element, str)\
               else str(element) for element in self) + ")"

    def __repr__(self):

        return f"CustomSet{str(self)}"
