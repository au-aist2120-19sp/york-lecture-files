# get a module
# import math
# from math import acos
# from math import sqrt as sq

# this is the __main__() function


import testmod
import testmod
testmod.puke()

# from testmod import puke
from testmod import *
testmod.puke()
testmod.cleanitup()

print('looks pretty ' + testmod.consistency)

print(abs(-5))
print(testmod.abs(-5))

# no matter how many times a module is imported, it is ONLY actually
# executed or read one time

# packages are just about file & folder structure
# __init__.py -- THIS IS OPTIONAL FOR PACKAGES

from pack import testpack
from pack.testpack import unicorns as uni

testpack.rainbows()
uni()


from lib2120.twod import point
p = point(1,1)
print(p.x)
