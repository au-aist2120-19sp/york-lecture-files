menu = '''
1) Burger
2) Fries
3) Checkout
'''
while True:
    print(menu)
    choice = input('Enter choice: ')
    if choice == '3':
        break
    elif choice == '1':
        print('Mmm. Wouldn\'t you like some fries?')
    elif choice == '2':
        print('Okay, but what about a juicy burger?')
    else:
        print('Enter a valid choice, dear customer')
print('enjoy your meal')


menu = '''
1) Burger ($3)
2) Fries ($1)
3) Checkout
'''
subtotal = 0
while True:
    print(menu)
    choice = input('Enter choice: ')
    if choice == '3':
        break
    elif choice == '1':
        print('Mmm. Wouldn\'t you like some fries?')
        subtotal = subtotal + 3 # subtotal += 3
    elif choice == '2':
        print('Okay, but what about a juicy burger?')
        subtotal += 1
    else:
        print('Enter a valid choice, dear customer')
    print(f'You subtotal is {subtotal}')
print('enjoy your meal')
print(f'but first give me ${subtotal}')

# Summation
sun = 0
for n in range(1,6): #15
    print(f'{sun} + {n} = {sun + n}')
    sun += n
print(sun)


# Factorial
prod = 1
for n in range(1,6): #120
    print(f'{prod} x {n} = {prod * n}')
    prod *= n
print(prod)

tofind = 'o'
for c in "hello world":
    if c == tofind:
        print('yeah I found ' + tofind)
        break
else:
    print('boo I didn\'t find ' + tofind)


from math import sqrt as squirt
for n in range(26,37):
    sq = squirt(n)
    isq = int(sq)
    if sq == isq:
        print(f'yeah, {n} has an int root: {sq:.0f}')
        break
else:
    print('NOT FOUND')


str = "what's up?"
seq = []
for c in str:
    if c != "'":
        seq.append(c)
print(seq)
print(''.join(seq))

str = "what's up?"
seq = []
for c in str:
    if c not in 'tsp':
        seq.append(c)
print(seq)
print(''.join(seq))

# LIST COMPREHENSIONS
# [EXPR for x in SEQ (if EXPR2)]
seq = [c for c in str if c not in 'tsp']
print(seq)

[True for x in range(10)]
['default' for x in range(10)]
[x % 2 == True for x in range(10)]
