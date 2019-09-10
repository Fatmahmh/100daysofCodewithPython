thistuple = ('apple ', 'bannana', 'orange', 'cherry')
print(thistuple)
 #Check if Item Exists
if "orange" in thistuple:
      print('yes , apple in this tuple')


#repeat an item in a tuple, use the * operator.
thistuple = ('python' , )*3
print(thistuple)


#+ Operator in Tuple uesd To add 2 tuples or more into one tuple.
#example
x = (3,4,5,6)
x = x + (1,2,3)
print(x)

#determine how many items a tuple has, use the len() method
print(len(x))


#It is also possible to use the tuple() constructor to make a tuple.
#Using the tuple() method to make a tuple.

thistuple = tuple((1,2,3,4,5,6,4,4))
print(thistuple)
print(thistuple.count(4))
print(thistuple.index(1))


