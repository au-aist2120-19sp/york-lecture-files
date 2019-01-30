peeps = {
    'akim': {
        'name': 'Akim Smith',
        'phone': '555-1212',
        'email': 'akim@mail.me'
    },
    'neesha': {
        'name': 'Neesha Bilbo',
        'phone': '867-5309',
        'email': 'neesha@mail.me'
    }
}

ptempl = '''
Name:   {name}
Email:  {email}
Phone:  {phone}
'''

# name = 'neesha'
# name = input('gimme a name: ')
# print(ptempl.format_map(peeps[name.lower()]))
name = input('gimme a name: ').lower()

if name in peeps:
    print(ptempl.format_map(peeps[name]))
else:
    print('NOT FOUND!!!')
    


