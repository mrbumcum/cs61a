"""Generalization"""

from math import pi, sqrt

def area(r, shape_constant):
    """Returns the area of a shape based on the shape constant.

    For example:
    >>> area_square(4)
    16
    >>> area_circle(1)
    3.141592653589793
    >>> area_hexagon(2)
    10.392304845413264
    """
    assert r > 0, 'A length must be positive'
    return r * r * shape_constant

def area_square(r):
    return area(r, 1)

def area_circle(r):
    return area(r, pi)

def area_hexagon(r):
    return area(r, 3 * sqrt(3) / 2)


"""Generalization for Summation"""

def summation(n, term):
    """
    Sum the first N terms of a sequence.

    >>> summation(5, cube)
    225
    """
    total, k = 0, 1
    while k <= n:
        total, k = total + term(k), k + 1
    return total

def identity(k):
    return k

def cube(k):
    return k ** 3

def sum_naturals(n):
    """Sum the first N natural numbers.

    >>> sum_naturals(5)
    15
    """
    return summation(n, identity)

def sum_cubes(n):
    """Sum the first N cubes.

    >>> sum_cubes(5)
    225
    """
    return summation(n, cube)
