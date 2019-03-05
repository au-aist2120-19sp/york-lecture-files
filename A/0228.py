# PYTHON supports custom Classes

# int() & string() & list() etc. are classes
# a class is a "complex" data type

class person:
    name = 'Anonymous'
    password = ''

    def sayhi(self):
        print('hi')
        print('my name is', self.name)

    def set_name(self,newname):
        self.name = newname

    def set_password(self, newpass, confpass):
        if newpass == confpass:
            self.password = newpass + 'booger' # boogie hash
            print('password changed')
        else:
            print('passwords do not match')

    def check_password(self,checkpass):
        checkpass = checkpass + 'booger' # hash my checkpass
        if checkpass == self.password:
            print('passes match')
        else:
            print('intruder alert!!')


# NOT IN THE CLASS DEFINITION

paul = person() # CREATE AN INSTANCE
david = person() # CREATE AN INSTANCE
#print(paul)
print(paul.name)
print(david.name)

# person.sayhi()

paul.name = "Paul"
david.name = "David"

paul.sayhi()
david.sayhi()

david.set_password('pass','pass')
print(david.password)
print(paul.password)
david.check_password('word')

# DON'T DO THIS
def hi(pers):
    print('hi my name is ', pers.name)

hi(paul)
hi("paul")
