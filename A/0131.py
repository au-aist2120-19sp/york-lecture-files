# if ????:  ???? is condition but also a boolean expression
# if :
# elif :
# else :

# ==, !=, <, >, <=, >=
# (not) in, is (not)

'a' == 'A'
ord('a')
ord('A')

names = ["Abc", "abc", "Bcd", "ZZZ"]
print(names)
names.sort()
print(names)

# ord('abc') ERROR

(1,3,-100) > (1,2,100)


a = (1,2,3)
b = a
a is b  # True

a = [1,2,3]
b = a
a is b  # True
a[1] = 5  # [1,5,3]
a is b  # True
print(b)

a = [1,2,3]
b = a[:]
a is b  # False
a == b  # True
a[1] = 5  # [1,5,3]
a is b # False
print(b)

1 in a
1 not in a
1 == 2
1 != 2
not (1 in a)

passwd = '12345abc'
if ('#' in passwd) == False:
    print('NOT Cool')
print('done')

passwd = '12345abc'
if not '#' in passwd:
    print('NOT Cool')
print('done')

if True:
    print('huh?')
else:
    print('nah')
print('done')

if not passwd.startswith('a'):
    print('you rock')
print('done')


age = 55
if age >= 21:
    if age <= 65:
        print('you can work')
    else:
        print('go home')
else:
    print('go home')
print('done')

if age >= 21 and age <= 65:
    print('you can work')
else:
    print('go home')
print('done')

age = 70
if (age >= 10 and age <= 20) or (age > 65):
    print('you get a discount')
else:
    print('no soup for you!')
print('done')


if 21 <= age <= 65:
    print('you can work')
else:
    print('go home')
print('done')


# C# a && b   a || b  !(a || b)


if '':
    print("You're empty")
else:
    print("you're full")
print('done')

if ():
    print('empty')
else:
    print('full')
print('done')


name = input('enter name:')
if name:
    print('hello ' + name)
else:
    print('you are nobody')
print('done')

'' or 'goober'
'booger' or 'goober'

name = input('Enter your name: ') or 'anonymous'
# BETTER
name = input('Enter your name: ').strip() or 'anonymous'


cnt = 0
while cnt < 10:
    print(f'line {cnt}')
    cnt += 2
print('done')

name = input('you name? ')
while not name:
    name = input('no really your name? ')
print('done')

