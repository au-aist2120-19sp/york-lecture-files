#FILE I/O
# AKA (STREAM !/O)

# FILE OPENING:::
# GET FILE OBJECT BY open() function
#fi = open('bs.txt')
#fi = open('..\\bs.txt')
fi = open('z:\\aist2120\\bs.txt')

li = fi.readline()
print(li)

fi.close()


# READ CHARS
fi = open('z:\\aist2120\\bs.txt')

wholedangthang = fi.read()
print(wholedangthang)

fi.close()

# read a chunk 'o chars
fi = open('z:\\aist2120\\bs.txt')

chunk = fi.read(1000000)
print(chunk)

fi.close()

# reads are SEQUENTIAL
fi = open('z:\\aist2120\\bs.txt')

chunk1 = fi.read(1000)
print("CHUNK1: " + chunk1)

chunk2 = fi.read(1000)
print("CHUNK2: " + chunk2)

fi.close()

# READ TO END
fi = open('z:\\aist2120\\bs.txt')

cnt = 1
ch = fi.read(1)
while ch:
    print(str(cnt) + ": " + ch)
    cnt += 1
    ch = fi.read(1)
print('fin')

fi.close()


# READ TO END (LINE VERSION)
fi = open('z:\\aist2120\\bs.txt')

cnt = 1
li = fi.readline()
while li:
    print(str(cnt) + ": " + li)
    cnt += 1
    li = fi.readline()
print('fin')

fi.close()


# READ TO END (MORE BETTERER VERSION)
fi = open('z:\\aist2120\\bs.txt')

cnt = 1
for li in fi:
    print(str(cnt) + ": " + li)
    cnt += 1
print('fin')

fi.close()


# MODES
# open(name, mode)
# mode defaults to 'r' : READ
# 'w' : WRITE (if file exists, replace it / if not, create it)
# 'a' : APPEND (if file exists, append to it)
# There's also some read+write modes...don't go there.

log = open('log.txt','a')

log.write('''I'm doing great by writing a line\n''')
# do stuff
log.write('''I did more great stuff\n''')

log.close()

# "Standard" streams
# * 1. input: stdin
# * 2. output: stdout (really just print())
# 3. error: stderr

# piping

# switch over to a new file