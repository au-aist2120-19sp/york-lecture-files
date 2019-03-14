'''
OBJECT-ORIENTATION
* Classes vs. Objects
* Instance
* State / Attributes / Properties
* Function (selfless) vs Methods (have self)
* Self (self.color or self.bounce() )
* Methods can access or mutate (acccessors or mutators)
* Inheritance
'''

'''
FUNCTIONS
declaration
def funcname([parm1[, parm2, ...]]):
    CODE BLOCK (contents of the function)
e.g,:
def hello():
def sayhi(name):
def converse(name1, name2):
oh by the way

def dolotsofstuff(*names): 
    names[1] >> 'paul'

dolotsofstuff('john','paul','george','ringo')

functions can:
a) DO STUFF (OTHERS might say subroutine or procedure but python likes "function")
OR
b) DO STUFF AND RETURN AN ANSWER/VALUE/RESULT

return?  How does it relate??
For type A), IT CAN return, and is just like "break" in that it exits early
For type B), IT MUST return a SINGLE value

return 1
return bob
return (5, 9) # COOL, can return a tuple

For type b, functions are evaluated and you need to assign the value to a variable (or use it)

g = getstuff()

t = gettwothings()   # returns (5,9)
t[1] >> 9

SEQUENCE UNPACKING

val1, val2 = gettwothings()   # returns (5,9)
val2 >> 9

BE PREPARED TO EVALUATE FUNCTIONS

def part(strng):
    return strng[2:]

what is the return value if I call part('hello')? _______
"llo"

def choice(age):
    if age < 21:
        <LFKDS:LFKJ:SL

'''

'''
FILE I/O (STREAM I/O)

strm = open(name, mode) # gives a stream reader
# modes!!! ESP: 'r','w','a'
txt = strm.read([bytes]) # returns big ol' string
txt = strm.readline()    # reads ONE line
lines = strm.readlines() # list (sequence) of lines
for line in lines:

STRM IS ALSO ITERABLE

for line in strm:   # just in time iteration...more efficient

# stream disposal (manual)
strm.close()
del strm

# stream disposal (automatic)
with open('b.txt','r') as strm:
    DO STUFF WITH strm

DONE (DIDN'T HAVE CLOSE OR DISPOSE)

'''

'''
EXCEPTION HANDLING
This is REactive error handling

try:     (1) Normal potenially error prone code
except:  (1..N) Only run if (perhaps a specific type of) error occurs
         ONLY one except block will ever run
else:    (1 (optional)) RUNS ONLY if NO EXCEPTION OCCURS
finally: (1 (optional)) ALWAYS runs whether or not there is an error

Multiple "except" options:

except:   ** CATCHES ANY and ALL EXCEPTIONS
except _____: ** Catching a specific exception CLASS
except ValueError:
except Exception: ** CATCHES ANY and ALL EXCEPTIONS
except _____ as _____: ** Catching and maybe USING and INSTACE of that CLASS
except Exception as ex: ** CATCHES ANY and ALL EXCEPTIONS

ValueError
ZeroDivisionError
IndexError
'''