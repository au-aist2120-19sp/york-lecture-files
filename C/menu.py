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
