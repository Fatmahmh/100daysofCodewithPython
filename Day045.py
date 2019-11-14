#Python Iterators
tuple = ("apple","bannana",'cherry')
myit=iter(tuple)
print(next(myit))
print(next(myit))
print(next(myit))

#Even strings are iterable objects, and can return an iterator.
mystr= 'bannana'
myitr1 = iter(mystr)
print(next(myitr1))
print(next(myitr1))
print(next(myitr1))
print(next(myitr1))
print(next(myitr1))
print(next(myitr1))

#Looping Through an Iterator
'''The for loop actually creates an iterator object and executes the next() method for each loop.'''
for x in tuple:
    print(x)

for x in mystr:
    print(x)
'''To create an object/class as an iterator you have to implement the methods __iter__() and __next__() to your object.
the __iter__() method acts similar to __inint__() , you can do operations (initializing etc.), but must always return the iterator object itself.
The __next__() method also allows you to do operations, and must return the next item in the sequence '''
class mynumbers:
     def __iter__(self):
         self.a=1
         return self

     def __next__(self):
        if self.a <= 20:
             x = self.a
             self.a += 1
             return x
        else:
             raise StopIteration

myclass = mynumbers()
myitr = iter(myclass)

print(next(myitr))
print(next(myitr))
print(next(myitr))
print(next(myitr))
print(next(myitr))

for x in myitr:
    print(x)
