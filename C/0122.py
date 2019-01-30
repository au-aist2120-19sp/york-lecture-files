lnums = [1,2,3,4,5]

lnc = lnums[0:5]
lnc2 = lnums[0:10]
lnc3 = lnums[:3]
lnc4 = lnums[2:]

s = '42'
s2 = s * 2
s3 = s + s

lnc5 = lnums + [6,7]
print(lnc5)

lnc6 = lnums * 3
print(lnc6)

print('+' + '-' * 50 + '+')
print('|' + ' ' * 50 + '|')
print('|' + ' ' * 50 + '|')
print('|' + ' ' * 50 + '|')
print('+' + '-' * 50 + '+')

lstr = ['SC','AL','ar','ak','ga']

len(lnums) #5
max(lnums) #5
min(lnums) #1
max(lstr) #'ga' ? 'sc'

lnums + lstr

seq = list(range(20))

seq.reverse()

seq.sort()
seq.reverse()
print(seq)

seq.sort()
print(seq)

seq.sort(reverse=True)
print(seq)

lstr.append('ms')
print(lstr)
print(len(lstr))

lstr.insert(4, 'az')
print(lstr)

lstr.remove()