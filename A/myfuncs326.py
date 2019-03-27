from math import sqrt

def pythag(a, b):
    '''
    sq(a) + sq(b) = sq(c)

    Assuming legs A & B of a right triangle
    return the length of the hypoteneuse of
    that triangle.

    E.g.,

    >>> pythag(3,4)
    5.0

    >>> pythag(6,8)
    10.0
    '''
    sqc = a**2 + b**2
    c = sqrt(sqc)
    return c

# MOST OF THE TIME
# modules have NO main code

# from pprint import pprint as pp
# pp(dir())
# print(__name__)
if __name__ == "__main__":
    # this should return 5
    # pythag(3,4)
    help(pythag)
    import doctest
    doctest.testmod()
