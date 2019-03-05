# Abstraction!!!!

# Functions : encapsulations of logic
 
prod = 1
for x in range(1, 5):   # 1..4
    print(str(x) + ' * ' + str(prod))
    prod = prod * x
    print(' = ' + str(prod))
print('4! = ' + str(prod))

 
prod = 1
fact = 5
for x in range(1, fact + 1):   # 1..4
    print(str(x) + ' * ' + str(prod))
    prod = prod * x
    print(' = ' + str(prod))
print(str(fact) + '! = ' + str(prod))
# FUNCTIONS!!!
# Function Definition

def showfactorial5():
    prod = 1
    fact = 5
    for x in range(1, fact + 1):   # 1..4
        print(str(x) + ' * ' + str(prod))
        prod = prod * x
        print(' = ' + str(prod))
    print(str(fact) + '! = ' + str(prod))

showfactorial5()

def showfactorial4():
    prod = 1
    fact = 4
    for x in range(1, fact + 1):   # 1..4
        print(str(x) + ' * ' + str(prod))
        prod = prod * x
        print(' = ' + str(prod))
    print(str(fact) + '! = ' + str(prod))

showfactorial4()


def showfactorial(fact):
    prod = 1
    for x in range(1, fact + 1):   # 1..fact
        print(str(x) + ' * ' + str(prod))
        prod = prod * x
        print(' = ' + str(prod))
    print(str(fact) + '! = ' + str(prod))

showfactorial4()
showfactorial(4)
showfactorial(8)

# REAL FUNCTIONS

name = input('enter your name: ')

import math

root = math.sqrt(4)


# flashback: public double root(double val) { ... }

def getfactorial(val):
    prod = 1
    for x in range(1, val + 1):   # 1..val
        prod = prod * x
    return prod

# call it
getfactorial(6)

x = getfactorial(7)

print('7! is ' + str(x))

# prob of rolling two 6's
# pretend this is 6! / 4!

f6 = getfactorial(6)
f4 = getfactorial(4)
p = f6/f4

print(p)

p = getfactorial(6) / getfactorial(4)
print(p)

def yorkstupidprob(v1, v2):
    p = getfactorial(v1) / getfactorial(v2)
    return p

print(yorkstupidprob(6,4))
print(yorkstupidprob(7,5))


# THIS BLOWS UP
print(yorkstupidprob(7))

def yorkstupidprob(v1, v2=1):
    p = getfactorial(v1) / getfactorial(v2)
    return p


print(yorkstupidprob(7,5))
print(yorkstupidprob(7))
