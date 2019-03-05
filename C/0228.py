# CLASS DEFINITIONS

class person:
    # define attributes
    name = 'Anonymous'
    yob = 1900
    phone = '555-1212'

    def get_yob(self):   #accessor
        return self.yob

    def set_yob(self, newyob):  #mutator
        self.yob = newyob

    def print(self):
        print(f"Name:  {self.name}")
        print(f"YOB:   {self.yob}")
        print(f"Phone: {self.phone}")


class student(person):
    pass

a = int() # create an instance of an integer with default values
print(a)

p = person() # create an instance of a person with default values
#print(p)
print(p.name) # ACCESS attributes

q = person()
print(q.name)

p.name = "Paul"
print(p.name)
print(q.name)


p.yob = 2001   #BAAAAAD
p.yob = 'bob'  # doh!!!
p.set_yob(2002) # GOOOOOOOODDDDD

print('pyob =',p.get_yob())
print('qyob =',q.get_yob())


p.print()
q.print()

p = q
p.print()
q.print()

print("CHANGE")

q.set_yob(-4000)
p.print()
q.print()


r = student()
r.set_yob(2005)

print(dir(r))
