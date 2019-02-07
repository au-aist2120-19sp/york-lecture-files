some = 0
while True:
    inp = input('Enter a number to add (press enter to stop): ').strip()
    if inp == '': # not inp   /  len(inp) == 0
        break
    elif not inp.isnumeric():
        print('A NUMBER you doof')
    else:
        num = int(inp)
        some += num
        print(f'Current subtotal is {some}')
print(f'Your final total is {some}')

