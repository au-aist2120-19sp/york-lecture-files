# FUNCTIONS

def sayhi(name):
    print(f"Hello there, {name}")

# CALL IT

sayhi("Paul")
sayhi()

# Default parameter value

def sayhi2(name="Anonymous"):
    print(f"Hello there, {name}")

# CALL IT

sayhi2("Paul")
sayhi2()


# REAL functions return values

def addnums(num1, num2):
    s = num1 + num2
    return s

val = addnums(4,5)
print(val)
print(val + 2)

# MORE ON RETURN

def sayhi3(name="Anonymous"):
    print(f"Hello there, {name}")
    return

# CALL IT

sayhi3("Paul")
sayhi3()


def showaddnums(num1, num2):
    if num1 > 0 and num2 > 0:
        s = num1 + num2
        print(s)
    else:
        print('ONLY POSITIVES YOU DOWNER')

showaddnums(4,5)
showaddnums(-1,5)

def showaddnum2(num1, num2):
    if num1 <= 0:
        print('num1 has to be positive')
        return
    if num2 <= 0:
        print('num2 has to be positive')
        return

    # WHEW, NO ERRORS
    s = num1 + num2
    print(s)


showaddnum2(4,5)
showaddnum2(-1,5)
showaddnum2(4,-5)

# parameter collection

def add2nums(num1, num2):
    s = num1 + num2
    return s

def add3nums(num1, num2, num3):
    s = num1 + num2 + num3
    return s

def add4nums(num1, num2, num3, num4):
    s = num1 + num2 + num3 + num4
    return s

val = add2nums(4,5)
print(val)
print(val + 2)

def addxnums(*nums):
    # print(nums)
    # print(len(nums))
    s = 0
    for v in nums:
        s += v
    return s

addxnums(1)
addxnums(2,2)
addxnums(4,8,12,22,50)
addxnums()


def add4nums(num1, num2, num3, num4):
    s = num1 + num2 + num3 + num4
    return s

print(add4nums(4,6,8,10))
print(add4nums(6,8,num4=11,num3=5))

# NAMED PARAMETERS

def show4nums(num1=10, num2=20, num3=30, num4=40):
    print(f'num1 is {num1}')
    print(f'num2 is {num2}')
    print(f'num3 is {num3}')
    print(f'num4 is {num4}')

show4nums(5,10,15,20)
show4nums()
show4nums(num4=39)


# RETURNING MULTIPLE VALUES

def getpos():
    lat = 47.123
    long = 12.719
    # NOOOO return lat + long
    # NOPE return lat && long
    return (lat,long)

pos = getpos()
print(pos)
print('my longitude is ' + str(pos[1]))

pos = getpos()
la = pos[0]
lo = pos[1]
print('my longitude is ' + str(lo))


la,lo = getpos()   # AUTO UNPACK the TUPLE
print('my longitude is ' + str(lo))

