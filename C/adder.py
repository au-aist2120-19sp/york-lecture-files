total = 0
while True:
    inp = input('Enter a number (press Enter to stop): ').strip()
    if inp == '': # len(inp) == 0  //  not inp
        break
    elif not inp.isnumeric():
        print('Enter a number, moron')
    else:
        num = int(inp)
        total += num
        print(f"You're subtotal so far is {total}")
print(f'The final total is: {total}')

