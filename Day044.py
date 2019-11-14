#Python Inheritance 2---Use the super() Function
class person :
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname
    def printname(self):
        print(self.fname, self.lname)

class student(person):
    def __init__(self, fname, lname, year):
        super().__init__(self, fname, lname)
        self.graduationyear = year

    def welcome(self):
        print("welcome"+self.fname,self.lname+"to the class of"+self.graduationyear)

y = student("layan","fares",2019)
y.printname()
y.welcome()



