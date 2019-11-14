#Python Inheritance
class person :
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname
    def printname(self):
        print(self.fname, self.lname)

x = person("fatma",  "maid")
x.printname()

#Create a Child Class
'''Use the pass keyword when you do not want to add any other properties or methods to the class.'''
class student(person):
    def __init__(self, fname, lname):
        person.__init__(self, fname, lname)



y = student('layan','fares')
y.printname()
