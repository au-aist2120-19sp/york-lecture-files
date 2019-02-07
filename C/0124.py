s1 = 'hello world'
s1[0]
s1[:5]

print(s1)

val1 = 12

print('it is now ' + val1 + ' o\'clock')

print('it is now {} oclock'.format(val1))

val2 = 20

print('it is now {} oclock on January {}'.format(val1, val2))

print('{0} {1}'.format(val1, val2))
print('{1} {0}'.format(val1, val2))
print('{oclock} {date}'.format(oclock=11, date=22))
print('{date} {oclock} {date}'.format(oclock=11, date=22))

print(f'{val1} {val2}')

val3 = 13.2

f'{val3}'

print(f'{val1}\n{val3}')

print(f'{val1:f}\n{val3:f}')
print(f'{val1:.2f}\n{val3:.2f}')

m1 = 'January'
m2 = 'February'

print(f'{m1} {val1:.2f}\n{m2} {val3:.2f}')
print(f'{m1:20} {val1:.2f}\n{m2:20} {val3:.2f}')
print(f'{m1:20} {val1:.2f}\n{m2:20} {val3:.2f}')

val3 = 1725.7

print(f'{m1:20} {val1:.2f}\n{m2:20} {val3:.2f}')
print(f'{m1:20} {val1:10.2f}\n{m2:20} {val3:10.2f}')
f'{val3:10.2f}'

m2 = 'Icantbelievethisisamonth'

print(f'{m1:20} {val1:10.2f}\n{m2:20} {val3:10.2f}')

print(f'{m1:20} {val1:10.2f}\n{m2[0:20]:20} {val3:10.2f}')
print(f'{m1[:20]:20} {val1:10.2f}\n{m2[0:20]:20} {val3:10.2f}')

title = 'Year End Report'

print(f'{title:80}')
print(f'{title:^80}')
print(f'{title:>80}')

print('-' * 80)


val5 = 3/4

print(f'{val5}')
print(f'{val5:.0%}')

uid = 'paul'

print(uid == inp.lower())

s1.find('l')
s1.find('ll')
s1.find('ld')
s1.find('BOOGER')
'll' in s1
s1.count('l')
s1.replace('l','w')

s1.find('h') == 0
s1[0] == 'h'

ls = 'Now is the time for Dr. York to shut up'
words = ls.split()
print(words)
backatya = ' '.join(words)
print(backatya)

backatya = '-'.join(words)
print(backatya)

ch = ['h','e','l']
st = ''.join(ch)
print(st)


### DICTS


grades = {'david': 100, 'paul': 72}
grades['john'] = 60
grades['john'] = 80



