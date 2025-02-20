"""Triangle exercise"""

def equilateral(sides):
    """Determines if the triangle is equilateral.
 
    :param sides: tuple - The length of the sides.
 
    :return: bool - True if it's an equilateral triangle, False otherwise.
 
    This function receives a tuple containing the length of the sides of the
    triangle, and checks if it's an equilateral triangle. It returns True if
    it is, False otherwise, including if it's not a triangle.
    """

    a, b, c = sides
    return a==b and b==c and a!=0

def isosceles(sides):
    """Determines if the triangle is isosceles.
 
    :param sides: tuple - The length of the sides.
 
    :return: bool - True if it's an isosceles triangle, False otherwise.
 
    This function receives a tuple containing the length of the sides of the
    triangle, and checks if it's an isosceles triangle. It returns True if
    it is, False otherwise, including if it's not a triangle.
    """

    a, b, c = sides
    return not ((a==0) or (b==0) or (c==0) or (a+b<=c) or (a+c<=b) or (b+c<=a))\
           and ((a==b) or (b==c) or (a==c))

def scalene(sides):
    """Determines if the triangle is scalene.
 
    :param sides: tuple - The length of the sides.
 
    :return: bool - True if it's an scalene triangle, False otherwise.
 
    This function receives a tuple containing the length of the sides of the
    triangle, and checks if it's an scalene triangle. It returns True if
    it is, False otherwise, including if it's not a triangle.
    """

    a, b, c = sides
    return not ((a==0) or (b==0) or (c==0) or (a+b<=c) or (a+c<=b) or (b+c<=a))\
           and ((a!=b) and (b!=c) and (a!=c))
