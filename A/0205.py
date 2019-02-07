# Counter -based loop
cnt = 0
while cnt < 10:
    print(cnt)
    cnt += 1 # cnt = cnt + 1

# C#: for (var cnt = 0; cnt < 10; cnt += 1)
# C#: foreach (var val in strings)

nums = [12,10,5,13]
for val in nums:
    print(val)

for let in "Paul":
    print(let)

nums2 = [0,1,2,3,4,5,6,7,8,9]
for num in nums2:
    print(num)

list(range(10))

for num in range(10):
    print(num)

# range start + end
for num in range(5,10):
    print(num)

# range start, end, step
for num in range(0,100,5):
    print(num)

for num in range(10,-1,-1):
    print(num)

for num in range(-1,10,-1):
    print(num)

for joe in range(1000):
    if joe % 3 == 0 and joe % 7 == 0:
        print(f'{joe} is divisible by 3 and 7')

# Sequence Unpacking
first = "a"
second = "b"
third = "c"

vals = ("a","b","c")

first = vals[0]
second = vals[1]
third = vals[2]

first, second, third = vals

name = "Paul"
fl, sl = name # BAD : Have to have the same number of variables as elements

fl, sl, *rest = name

vals = [12,15,9,21,6,11]
first, *mids, last = vals


dict = {
    'bob': 10,
    'sally': 20,
    'bingo': 30
}
for key in dict:
    print(f'{key} is {dict[key]} years old')

# dict.items() is sequence of (key,value) pairs (tuples)
for name, age in dict.items():
    print(f'{name} is {age} years old')


# Parallel Iteration (ZIPPING)
Names = ['Pa','Go','Lm','Xy']
HW1 = [10,9,8,6]
HW2 = [5,9,7,10]
HW3 = [7,8,6,10]

list(zip(Names, HW1))

for name, hw1grade in zip(Names, HW1):
    print(f'{name} got a {hw1grade} on homework 1')

for name, hw1grade, hw2grade, hw3grade in zip(Names, HW1, HW2, HW3):
    averg = (hw1grade + hw2grade + hw3grade) / 3
    print(f'{name} has a {averg:.2} average')

vals = [10,11,12,100,13]
for v in sorted(vals):
    print(v)

for v in reversed(sorted(vals)):
    print(v)

m = '''
1) print hello
2) print world
3) exit
'''
while True:
    print(m)
    inp = input('Select: ')
    if inp == '3':
        break

