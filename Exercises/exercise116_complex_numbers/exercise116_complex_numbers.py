"""Complex Numbers exercise"""

from math import exp, sin, cos, sqrt

class ComplexNumber:
    """A complex number. The first argument corresponds to the real part,
    the second argument corresponds to the imaginary part."""

    def __init__(self, real, imaginary, /):

        if not isinstance(real, (int, float)) or\
           not isinstance(imaginary, (int, float)):
            raise TypeError("Inputs must be integers or floats.")

        self.real = real
        self.imaginary = imaginary

    def __eq__(self, other, /):

        if not isinstance(other, (int, float, ComplexNumber)):
            raise TypeError("Operation not supported with input type.")

        if not isinstance(other, ComplexNumber):
            other = ComplexNumber(other, 0)
        return self.real == other.real and self.imaginary == other.imaginary

    def __add__(self, other, /):

        if not isinstance(other, (int, float, ComplexNumber)):
            raise TypeError("Operation not supported with input type.")

        if not isinstance(other, ComplexNumber):
            other = ComplexNumber(other, 0)
        return ComplexNumber(self.real + other.real, self.imaginary + other.imaginary)

    def __radd__(self, other, /):

        if not isinstance(other, (int, float, ComplexNumber)):
            raise TypeError("Operation not supported with input type.")

        return self + other

    def __mul__(self, other, /):

        if not isinstance(other, (int, float, ComplexNumber)):
            raise TypeError("Operation not supported with input type.")

        if not isinstance(other, ComplexNumber):
            other = ComplexNumber(other, 0)
        real = self.real * other.real - self.imaginary * other.imaginary
        imaginary = self.imaginary * other.real + self.real * other.imaginary
        return ComplexNumber(real, imaginary)

    def __rmul__(self, other, /):

        if not isinstance(other, (int, float, ComplexNumber)):
            raise TypeError("Operation not supported with input type.")

        return self * other

    def __sub__(self, other, /):

        if not isinstance(other, (int, float, ComplexNumber)):
            raise TypeError("Operation not supported with input type.")

        if not isinstance(other, ComplexNumber):
            other = ComplexNumber(other, 0)
        return ComplexNumber(self.real - other.real, self.imaginary - other.imaginary)

    def __rsub__(self, other, /):

        if not isinstance(other, (int, float, ComplexNumber)):
            raise TypeError("Operation not supported with input type.")

        return self*-1 + other

    def __truediv__(self, other, /):

        if not isinstance(other, (int, float, ComplexNumber)):
            raise TypeError("Operation not supported with input type.")

        if not isinstance(other, ComplexNumber):
            other = ComplexNumber(other, 0)
        real = (self.real * other.real + self.imaginary * other.imaginary)/\
               (other.real**2 + other.imaginary**2)
        imaginary = (self.imaginary * other.real - self.real * other.imaginary)/\
                    (other.real**2 + other.imaginary**2)
        return ComplexNumber(real, imaginary)

    def __rtruediv__(self, other, /):

        if not isinstance(other, (int, float, ComplexNumber)):
            raise TypeError("Operation not supported with input type.")

        if not isinstance(other, ComplexNumber):
            other = ComplexNumber(other, 0)
        return other / self

    def __abs__(self):

        return ComplexNumber(sqrt(self.real**2 + self.imaginary**2), 0)

    def __round__(self, decimals=0, /):

        if not isinstance(decimals, int):
            raise TypeError("Decimals input must be an integer.")

        return ComplexNumber(round(self.real, decimals), round(self.imaginary, decimals))

    def __str__(self):

        if self.real:
            real_string = str(self.real)
            if self.imaginary:
                real_string += " + "
        imaginary_string = f"{self.imaginary} i" if self.imaginary else ""
        return real_string + imaginary_string

    def __repr__(self):

        return f"ComplexNumber({self._real}, {self._imaginary})"

    def conjugate(self):
        """The complex number's conjugate."""

        return ComplexNumber(self.real, -self.imaginary)

    def reciprocal(self):
        """The complex number's reciprocal."""

        real = self.real/(self.real**2 + self.imaginary**2)
        imaginary = -self.imaginary/(self.real**2 + self.imaginary**2)
        return ComplexNumber(real, imaginary)

    def exp(self):
        """The complex number's exponential."""

        return ComplexNumber(exp(self.real) * cos(self.imaginary),\
                             exp(self.real) * sin(self.imaginary))

    @property
    def real(self):
        """The complex number's real part."""

        return self._real

    @real.setter
    def real(self, real, /):

        self._real = real

    @property
    def imaginary(self):
        """The complex number's imaginary part."""

        return self._imaginary

    @imaginary.setter
    def imaginary(self, imaginary, /):

        self._imaginary = imaginary
