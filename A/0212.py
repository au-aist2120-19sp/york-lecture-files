# TYPES OF STREAMS
# File Stream
#    seekable
#    readable
#    writable
# stdout (OUTPUT STREAM)
# stdin (INPUT STREAM)
# stderr (ERROR OUTPUT STREAM)

f = open('simpletable.html')

if f.readable():
    contents = f.read(10)
    print(contents)
    contents = f.read(10)
    print(contents)
    if f.seekable():
        f.seek(0)
    contents = f.read(10)
    print(contents)
   

f.close()

f = open('newfile.txt','r')
f.close()

f = open('newfile.txt','w')
print(f.readable())
if f.writable():
    f.write('hello')
f.close()

f = open('newfile.txt','w')
print(f.readable())
if f.writable():
    f.write('''This is a long
multiline string.
isn't it grand?''')
f.close()
