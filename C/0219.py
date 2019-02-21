# File I/O
# File Stream

# open a file stream
#fi = open('stuff.txt')
#fi = open('..\\stuff.txt')
fi = open('z:\\aist2120\\stuff.txt')

txt = fi.read(20)
print(txt)

fi.close()

# Read line at a time
fi = open('z:\\aist2120\\stuff.txt')

txt = fi.readline()
print(txt)

fi.close()


# one way streams
fi = open('z:\\aist2120\\stuff.txt')

txt = fi.read(200000)
print(txt)

txt = fi.read(200000)
print(txt)

fi.close()


# read the whole thing (in chunks)
fi = open('z:\\aist2120\\stuff.txt')

chunk = fi.read(10)
# while len(chunk) > 0:
# while chunk != '':
# while chunk.isalphanum(): ???
while chunk: # chunk is truthy if it has characters
    print(chunk)
    chunk = fi.read(10)

print('done')
fi.close()


# read a LINE at a time
fi = open('z:\\aist2120\\stuff.txt')

line = fi.readline()
while line: # line is truthy if it has characters
    print(line.strip())
    line = fi.readline()

print('done')
fi.close()


# SHORTCUT way of iterating over a file
fi = open('z:\\aist2120\\stuff.txt')

for line in fi:
    print(line.strip())

print('done')
fi.close()


# FILES HAVE MODES
# 'r' : READ (DEFAULT)
# 'w' : WRITE, create or overwrite a file
# 'a' : APPEND, create or append to a file

# write a new file

fi = open('output.txt', 'w')
fi.write('here is line 1\n')
fi.write('here is line 2\n')
fi.close()

