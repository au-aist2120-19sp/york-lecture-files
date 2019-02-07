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
    elif inp == '1':
        print('hello')
    elif inp == '2':
        print('world')
    else:
        print('You are an absolute moron')


some = 0
for n in range(1,5):
    print(f'{some} + {n} = {some + n}')
    some += n
print(some)


prod = 1
for n in range(2,6):
    print(f'{prod} * {n} = {prod * n}')
    prod *= n  # prod = prod * n
print(prod)



some = 0
while True:
    inp = input('Enter a number to add (press enter to stop): ').strip()
    if inp == '': # not inp   /  len(inp) == 0
        break
    else:
        num = int(inp)
        some += num
        print(f'Current subtotal is {some}')
print(f'Your final total is {some}')

for n in range(20):
    if n == 10:
        print('yeah, I am at 10')
        break
    else:
        print(n)
else:
    print('I never hit 10')

from math import sqrt as booger
for n in range(26,37):
    root = booger(n)
    if root == int(root):
        print(f'{root:.0f} is a whole number')
        break
else:
    print('no whole number roots!')


ls = []
for c in 'hello world':
    if c != 'l':
        ls.append(c)
print(ls)
print(''.join(ls))


ls = []
for c in "what's up?":
    if c not in 'tsp':
        ls.append(c)
print(ls)
print(''.join(ls))

ls = [c for c in "what's up?" if c not in 'tsp']
print(ls)

#[expr for var in seq (if expr)]

[True for x in range(5)]
[0 for x in range(5)]
['bob' for x in range(10)]
[x for x in range(5)]

[x*x for x in range(1,11)]

[x*x for x in range(1,11) if x%2 != 0] # odd squares

[(x,y) for x in range(1,4) for y in range(1,4)]

# File I/O

f = open('simpletable.html')
print(f.read())
f.close()

f = open('simpletable.html')
print('line:' + f.readline().replace('<','BOOGER!'))
f.close()

'hello world'.index('hello')