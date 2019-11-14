#Python Classes and Objects 2
class person :
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def greeting(self):
        print("hello, my name is :" + self.name)

p1 = person("layan",12)
p1.greeting()

#Modify Object Properties
p1.age = 21
print(p1.age)

#You can delete properties on objects by using the del keyword.
#del p1.age
print(p1.age)


#You can delete objects by using the del keyword
#del p1
print(p1)
