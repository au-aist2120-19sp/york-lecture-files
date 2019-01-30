book = {
    'abdul': {
        'name': 'Abdul',
        'phone': '867-5309',
        'email': 'ab@email.me'
    },
    'ariana': {
        'name': 'Ariana',
        'phone': '555-1212',
        'email': 'ar@email.me'
    }
}

contempl = '''
Name:      {name}
Email:     {email}
Phone:     {phone}
'''

name = input('enter name: ').lower()
if name in book:
    print(contempl.format_map(book[name]))
#elif name not in book:
else:
    print('not found')
