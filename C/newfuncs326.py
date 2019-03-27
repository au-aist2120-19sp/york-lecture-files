from math import sqrt
def pythag(a,b):
    '''
    For any given legs of a right triangle, return the
    length of the hypotenuse (sp???).

    Uses Pythagorean Theory a2 + b2 = c2. Yada yada.

    E.g.,

    >>> pythag(3,4)
    5.0

    >>> pythag(6,8)
    10.0

    >>> pythag("three","four")
    BLOW UP!!!

    '''
    c2 = a**2 + b**2
    c = sqrt(c2)
    return c

# print(pythag(3,4)) # should be 5
# print('Paul wuz here')

# from pprint import pprint as pp
# pp(dir())
# print(__name__)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
