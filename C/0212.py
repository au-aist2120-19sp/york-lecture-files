# STREAM I/O
# File
# Network
# stdout (Console print)
# stdin (Console input)
# stderr 

f = open('simpletable.html')    

if f.readable():
    # text = f.read()
    # print(text)
    text = f.read(10)
    print(text)
    text = f.read(10)
    print(text)
    if f.seekable():
        f.seek(0)
    text = f.read(10)
    print(text)

f.close()



f = open('newfile.txt','r')
f.close()

f = open('newfile.txt','w')
f.close()

f = open('newfile.txt','w')
f.write('Hello')
f.close()

f = open('newfile.txt','w')
f.write('''Here is a
very long
string to demonstrate
something, I don't know what''')
f.close()

