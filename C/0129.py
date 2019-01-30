students = ['paul', 'george', 'ringo', 'john']
grades = [100,90,50,70]

idx = students.index('ringo')
print(grades[idx])

# declare
stugrades = {
    'paul': 100,
    'george': 90,
    'ringo': 50,
    'john': 70
}

# read / access
print(stugrades['ringo'])

# add
stugrades['pete'] = 105

# modify / update
stugrades['pete'] = 100

# delete
del stugrades['george']
del stugrades['john']
del stugrades['george'], stugrades['john'] # one liner

list(stugrades.keys())
list(stugrades) # synonymous
list(stugrades.values())

print('paul' in stugrades)
print(100 in stugrades)
print(100 in stugrades.values())


# CHESS BOARD

board = {
    'a1': 'R+', 'b1': 'N+', 'c1': 'B+', 'd1': 'K+',
    'a2': '', 'b2': '', 'c2': '', 'd2': '',
    'a3': '', 'b3': '', 'c3': '', 'd3': '',
    'a4': 'R-', 'b4': 'N-', 'c4': 'B-', 'd4': 'Q+',
}
board['b2']

# move b1 to b2
board['b2'] = board['b1']
board['b1'] = ''


# --------------------
# | K* | ...

btempl = '''
+----+----+----+----+
|{a1:^4}|{b1:^4}|{c1:^4}|{d1:^4}|
+----+----+----+----+
|{a2:^4}|{b2:^4}|{c2:^4}|{d2:^4}|
+----+----+----+----+
|{a3:^4}|{b3:^4}|{c3:^4}|{d3:^4}|
+----+----+----+----+
|{a4:^4}|{b4:^4}|{c4:^4}|{d4:^4}|
+----+----+----+----+
'''
print(btempl.format_map(board))

# move b4 to b3
board['b3'] = board['b4']
board['b4'] = ''
print(btempl.format_map(board))


# C# had if (expr) { ..... }
val = 3
if val == 3:
    print('val is equal to 3')
    print('yeah!!!')
elif val == 4:
    print('val is equal to 4')
    print('yeah!!!')
else:
    print('val is NOT equal to 3 or 4')
    print('booooooo!')
print('DONE!!')

# boolean operators
# ==, !=, >, <, >=, <=, in, not in, is, is not

