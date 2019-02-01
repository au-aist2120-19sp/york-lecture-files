# boolean expression
#   EVALUATES to True or False

# res = True

# THESE TWO ARE EQUIVALENT

# if res == True:
# if res:

# Comparisons: <, >, <=, >=, ==, !=, in, not in, is, is not

"a" != "A"
ord('a') # 97
ord('A') # 65

'a' > 'A' # True

l = ['abc', 'abd', 'abZ', 'ZZZ']
l.sort()
print(l)

(1,2,3) < (1,3,2)
(1,2,10000) < (1,3,-10000000)
(1,10000,3) < (1,-10000000,3)
(1,2,3) < (1,2)
(1,2,3) < (1,3)
(2,) < (1,2,3,4,5,6)
'hi' < 'hippopotamus'

a = [1,2,3]
b = a
a[2] = 5
print(a)
print(b)

x = [1,2,3]
y = x[:] # x.copy()
x[2] = 5
print(x)
print(y)

a = [1,2,3]
b = a
a == b
a is b

x = [1,2,3]
y = x[:] # x.copy()
x == y
x is y

# is, is not, in, not in

'a' in 'abcde'
'c' in 'abcde'
'f' in 'abcde'

'f' not in 'abcde'

not True
not False
not not True

# BAD 3 not == 5
not 3 == 5
3 != 5
not 3 != 5 # opposite

not 'a' in 'abc'
not a is b

age = 22

if age >= 16:
    if age <= 21:
        print('go in')
    else:
        print('get out')
else:
    print('get out')

age = 20
if age >= 16 and age <= 21:
    print('go in')
else:
    print('get out')

# AND expr
#  T and T == T
#  F and T == F
#  T and F == F
#  F and F == F

# OR expr
#  T or T == T
#  F or T == T
#  T or F == T
#  F or F == F

# if age < 12 or age > 16:
# if age < 16 or age > 12:  NONSENSE
# if age < 12 and age > 50: NONSENSE

# NOT (negation) in C# is !   so if (!x>6)
# AND in C# is &&
# OR in C# is ||

if 16 <= age <= 21:
    print('go in')
else:
    print('get the Hell out')

name = input('enter name: ')
if len(name) == 0:
    print('you stink')

if name:
    print('you stink')

name = input('enter name: ') or 'anonymous'
# infinite loop
cnt = 0
while cnt < 10:
    print(cnt)

# counter-based loop
cnt = 0
while cnt < 10:
    print(cnt)
    #cnt = cnt + 1
    cnt += 1

# Good
name = input('enter name: ')
while not name:
    print('no really, I need your name')
    name = input('enter name: ')
print('hi ' + name)

# Better
name = input('enter name: ').strip()
while not name:
    print('no really, I need your name')
    name = input('enter name: ').strip()
print('hi ' + name)

`
