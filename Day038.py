#Python Arrays 2
#Looping Array Elements
car = ['ford','bmw','toyota']
print(car)

for x in car:
    print(x)

#You can use the append() method to add an element to an array.
print(car)
car.append('honda')
print(car)

#You can use the pop() method to remove an element from the array.
car.pop(1)
print(car)


#You can also use the remove() method to remove an element from the array
car.remove('honda')
print(car)
