'''
Object-Orientation
* Class vs. Object
* Instance
* State / Attributes / Properies
* Mutators
* self (self.SOMETHING -- current object (C# "this"))
* function vs. method (methods access/mutate self)
* Inheritance (parent class / sub class : class hierarchy)
'''

'''
functions
declaration: def name([param1[, param2, ...]]):
    FOLLOWED BY A CODE BLOCK
eg:
def sayhi():
def sayyourname(name):
def haveconversation(name1, name2):

functions CAN EITHER
1) DO STUFF (procedures / subroutines)
CAN USE "return"
OR
2) DO STUFF AND GIVE ME A RESULT
MUST USE "return [value]"

e.g.,
return 1
return var1
return (val1, val2)

BE PREPARED to "evaluate" functions

def part(strng):
    return strng[2:-1]

part("hello")

def decide(age):
    if age:>>>>>

def repeat(times):
    for i in range(times):

SEQUENCE UNPACKING

def pack():
    return (3,5)

v1,v2 = pack()
'''

'''
FILE I/O (STREAM I/O)
strm = open(name, mode)
KNOW THE MODES
RETURN?? stream-reader
strm.read([bytes])
strm.readline() -> one line at a time
strm.readlines() -> whole sucker as a big arsed list
ITERATION OF A STREAM
for line in strm:
    print(line[2:5])

STREAMS SHOULD BE CLOSED
strm.close()

with open(name,mode) as strm:
    # AUTO CLOSE strm at end

'''

'''
EXCEPTION HANDLING
main blocks:
    try:     (1) TO DO SOMETHING
    except:  (1...N) RESPOND TO SPECIFIC (OR GENERIC) EXCPETIONS
             (BUT ONLY ONE IS EVERY ACTUALLY EXECUTED IF AN EXCEPTION OCCURS)
    finally: (1) NO MATTER WHAT DO THIS
    else:    (1) IF AND ONLY IF NO EXCEPTION OCCURRED

except [[EXCEPTION_CLASS] as variable]:
except ValueError:
except ZeroDivisionError:
except IndexError:
except Exception [as var]:  * CATCHES EVERYTHING
except:  * CATCHES EVERYTHING
'''

grade = 0
grade = int(input("enter grade: "))
print(grade)


e = "p.y@a.com"
fn = "paul"
ln = "york"
d = "a.com"
name = ln + ", " + fn

print(f"{e:25}{name:20}{d:15}")











