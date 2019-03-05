# quick review
def sayhi(name='Anonymous'):
    print(f'Oh, hi there, {name}')

sayhi()
sayhi('Paul')


def doaddsuff(num1, num2):
    summie = num1 + num2
    return summie

summie = doaddsuff(2,2)
print(summie)
summie = doaddsuff(4,4)
print(summie)

# Let's talk about SCOPE

num1 = 12

def doaddmoresuff(num1, num2, num3):
    summie = num1 + num2 + num3
    return summie

print(summie)
summie = doaddmoresuff(4,4,4)
print(summie)


def showxpeople(x):
    if 1 <= x <= 10:
        for p in range(1, x+1):
            print(f'Person Number {p}')
    else:
        print('Yo idiot! Between 1 and 10!!!')

def showxpeople(x):
    if x < 1 or x > 10:
        print('Yo idiot! Between 1 and 10!!!')
        return
    for p in range(1, x+1):
        print(f'Person Number {p}')

showxpeople(5)
showxpeople(-5)


print(1,2,3,4,5)

print(1,2,3,4,5,sep='booger')

# Parameter Collector

def doaddstuff2(*nums):
    # print(nums)
    # print(len(nums))
    s = 0  # declare an accumulator
    for v in nums:
        s += v
    return s

print(doaddstuff2(3,4,5))

print(doaddstuff2(3,4,5,8,1,-1,12))


# Named Parameters

def doaddmoresuff3(num1=5, num2=10, num3=20):
    summie = num1 + num2 + num3
    return summie

doaddmoresuff(5,6,7)
print(doaddmoresuff3())
print(doaddmoresuff3(num3=25))
print(doaddmoresuff3(0,num3=25))

n3 = input("enter a third number: ")
print(doaddmoresuff3(num3=int(n3)))



def superdiv(num,den):
    wh = num // den
    re = num % den
    # NO wh + re
    # NO wh && re
    # COULD str(wh) + 'r' + str(re)
    # BEST (wh,re) SAME SAME AS (3,2)
    return (wh, re)

superdiv(13,2) # returns (6,1)
superdiv(13,5) # returns (3,2)

ans = superdiv(77,13)
print('the remainder is ' + str(ans[1]))

ans = superdiv(7497,146)
n = ans[0]
r = ans[1]
print('the remainder is ' + str(r))

n, r = superdiv(7497,146) # UNPACK (v1,v2) into n and r
print('the remainder is ' + str(r))
