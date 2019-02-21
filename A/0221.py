# ABSTRACTION



sum = 0
max = 10
for n in range(1, max + 1):
    print(str(n) + ' + ' + str(sum))
    sum = sum + n
    print(str(sum))

print(sum)


def showsum10():
    sum = 0
    max = 10
    for n in range(1, max + 1):
        print(str(n) + ' + ' + str(sum))
        sum = sum + n
        print(str(sum))

    print(sum)

# CALL A FUNCTION
showsum10()

def showsum9():
    sum = 0
    max = 9
    for n in range(1, max + 1):
        print(str(n) + ' + ' + str(sum))
        sum = sum + n
        print(str(sum))

    print(sum)

# CALL IT
showsum9()


#!!!!! PARAMETERS !!!!
# variables that are passed IN to functions

def showsum(maxie):
    sum = 0
    for n in range(1, maxie + 1):
        print(str(n) + ' + ' + str(sum))
        sum = sum + n
        print(str(sum))
    print(sum)

# CALL IT
showsum(10)
showsum(9)
showsum(3)

# Make a REAL Function
# Return a value

def getsum(maxie):
    sum = 0
    for n in range(1, maxie + 1):
        sum = sum + n
    return sum  # GIVE IT BACK (AKA RETURN IT)


# CALL / CONSUME IT
s = getsum(10)

# ADD summation of 10 to the summation of 3
# store that as stupidsum

s10 = getsum(10)
s3 = getsum(3)
stupidsum = s10 + s3
print(stupidsum)

stupidsum = getsum(10) + getsum(3)
print(stupidsum)


def stupid(n1, n2):
    stupidsum = getsum(n1) + getsum(n2)
    return stupidsum

print(stupid(10,3))

# FYI, this is a "wrapper" function
def stupid2(n1=3, n2=5):
    return stupid(n1,n2)


stupid2()       # 3 & 5
stupid2(7)      # 7 & 5
stupid2(5,6)    # 5 & 6

