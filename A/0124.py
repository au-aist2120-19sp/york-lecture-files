s1 = 'hello wor;d'

s1.format()

s2 = 'hello {}'
s2.format('world')
s2.format(5)

s3 = "{}, {}, and {}"
s3.format('huey', 'dewey', 'louey')

s4 = 'Hello {0}, my name is {1}. It\'s really nice to meet you {0}'
s4.format('James', 'Tamesha')
s4.format('Billy', 'Leslie')

val1 = 12
val2 = -0.5

s5 = '{val1} is greater than {val2}'
s5.format(val1=val1, val2=val2)

print(f'{val1} is greater than {val2}')

sresult = f'{val1} is greater than {val2}'

val3 = 1/3

f'{val1} is greater than {val2} and {val3}'
f'{val1:f} is greater than {val2:f} and {val3:f}'
f'{val1:.2f} is greater than {val2:.2f} and {val3:.2f}'

print(f'{val1}\n{val2}\n{val3}')
print(f'{val1:12f}\n{val2:12f}\n{val3:12f}')
print(f'{val1:12.2f}\n{val2:12.2f}\n{val3:12.2f}')
val3 = 2/3

s11 = 'Max Temp'
s12 = 'Min Size'
s13 = 'Who Cares What this IS'

print(f'{s11}{val1:12.2f}\n{s12}{val2:12.2f}\n{s13}{val3:12.2f}')
print(f'{s11:15}{val1:12.2f}\n{s12:15}{val2:12.2f}\n{s13:15}{val3:12.2f}')
print(f'{s11:15}{val1:12.2f}\n{s12:15}{val2:12.2f}\n{s13[:15]:15}{val3:12.2f}')
print(f'{s11:30}{val1:12.2f}\n{s12:30}{val2:12.2f}\n{s13:30}{val3:12.2f}')


pct1 = 3/4
f'{pct1:%}'
f'{pct1:.0%}'


val5 = 123091802381092830128
f'{val5}'
f'{val5:,}'
f'{val5:30,.2f}'

title = 'MY AWESOME REPORT'
print(f'{title:80}')
print(f'{title:^80}')
print(f'{title:>80}')

print(f'{title:*^80}')
title.lower()

uid = 'paul'
comp = 'Paul'
comp == uid
comp.lower() == uid

title.find('MY')
title.find('E')
title.find('Z')
title.find('my')


h = list('hello')
''.join(h)
'.'.join(h)

h[2] = 5
h

sent = 'Now is the time for all good folk to come to the aid of their professor'
sent.split()

longnum = '1,234,567,890,123'
longnum.split(',')

sent.replace('is', 'was')
sent.replace('to', '2')


l = ['a','b','c']
l[1]

stu = ['bo','lu']
grade = [100,95]

grades = {'bo':100, 'lu':95}
grades['lu']

list(grades.keys())
list(grades.values())
list(grades)
