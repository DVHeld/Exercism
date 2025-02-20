"""Rational Numbers exercise"""

class Rational:
    """A rational number.
 
    Implements the operations of equality comparison, addition, substraction, multiplication,
    division, absolute value and exponentiation.
    """

    def __init__(self, numerator, denominator):

        if numerator is None or denominator is None:
            raise ValueError("Missing input.")
        if not isinstance(numerator, int) or not isinstance(denominator, int):
            raise TypeError("Inputs must be integers.")

        gcd = self._greatest_common_divisor(numerator, denominator)
        self.numerator = (-1 if denominator < 0 else 1) * numerator // gcd
        self.denominator = abs(denominator) // gcd

    def _greatest_common_divisor(self, number_a, number_b):

        number_a, number_b = abs(number_a), abs(number_b)
        number_1, number_2 = max(number_a, number_b), min(number_a, number_b)
        if not number_2:
            return number_1
        for divisor in range(number_2,1,-1):
            if number_1 % divisor == 0 == number_2 % divisor:
                return divisor
        return 1

    def __eq__(self, other):

        return self.numerator == other.numerator and self.denominator == other.denominator

    def __str__(self):

        return f'{self.numerator}/{self.denominator}'
    
    def __repr__(self):

        return f'Rational({self.numerator}, {self.denominator})'

    def __add__(self, other):

        numerator = self.numerator * other.denominator + self.denominator * other.numerator
        denominator = self.denominator * other.denominator
        return Rational (numerator, denominator)

    def __sub__(self, other):

        numerator = self.numerator * other.denominator - self.denominator * other.numerator
        denominator = self.denominator * other.denominator
        return Rational (numerator, denominator)

    def __mul__(self, other):

        numerator = self.numerator * other.numerator
        denominator = self.denominator * other.denominator
        return Rational (numerator, denominator)

    def __truediv__(self, other):

        numerator = self.numerator * other.denominator
        denominator = self.denominator * other.numerator
        return Rational (numerator, denominator)

    def __abs__(self):

        return Rational(abs(self.numerator), abs(self.denominator))

    def __pow__(self, power):

        if power >= 0:
            numerator = self.numerator**power
            denominator = self.denominator**power
        else:
            numerator = self.denominator**(-power)
            denominator = self.numerator**(-power)
        return Rational (numerator, denominator)

    def __rpow__(self, base):

        return (base**self.numerator)**(1/self.denominator)
