students = ['john','paul','george','ringo']
grades = [100,60,80,15]
'ringo' in students         # True or False
students.index('ringo')     # 3

idx = students.index('ringo') # 3
print(grades[idx])

stugrades = {
    'john': 100,
    'paul': 60,
    'george': 80,
    'ringo': 15
}
print(stugrades['ringo'])

stugrades['bobby'] = 105   # add
stugrades['bobby'] = 100   # change

del stugrades['bobby']

jack = 5
n = input('enter name: ')
# CAN'T GET "jack" variable value
# COULD GET stugrades[n] to get a value

battle = { ('a', 7) = 'BS' }
print(battle[('a', 7)]) # BS

'john' in stugrades       # True
100 in stugrades          # False
100 in stugrades.values() # True

# ADDRESS BOOK

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

abd = book['abdul']
print(abd['phone'])
print(book['abdul']['phone'])
print(book['abdul']['address']['city'])  # if it had a complex address


print(book['abdul'])

contempl = '''
Name:      {name}
Email:     {email}
Phone:     {phone}
'''
print(contempl.format_map(book['abdul']))



board = {
    'a1': 'R+', 'b1': 'B+', 'c1': 'N+','d1': 'K+',
    'a2': '',
    'b2': '',
    'c2': '',
    'd2': '',
    'a3': '',
    'b3': '',
    'c3': '',
    'd3': '',
    'a4': 'R-',
    'b4': 'B-',
    'c4': 'N-',
    'd4': 'Q-'
}