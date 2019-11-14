#Python Classes and Objects
class my_class:
    x=5
print(my_class)

#Create Object
p1 = my_class()
print(p1.x)

#The __init__() Function
class person :
    def __init__(self,name,age):
        self.name = name
        self.age = age

person1 = person('john',25)
print(person1.name)
print(person1.age)
