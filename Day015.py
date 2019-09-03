x = [ 1,2,3,4,5,6]
print(len(x))

#Add Items using Append() method
x.append(7)
print(x)

#o add an item at the specified index, use the insert() method.
x.insert(2,2.5)
print(x)


#Remove Item

#using remove() method
x.remove(2.5)
print(x)
#using pop() method
x.pop()  #by defualt witout spicfece index it will pop last item in the list
print(x)
x.pop(1) #will pop spcfiec item in the list by index
print(x)


#The clear() method empties the list.
x.clear()
print(x)



#Copy a List
#There are ways to make a copy, one way is to use the built-in List method copy().
x = [1,2,3,4,5]
y = x.copy()
print(y)

#Another way to make a copy is to use the built-in method list()
x = [1,2,3,4,5]
y = list(x)
print(y)




# use the list() constructor to make a new list.
newlist = list(("apple" ,'orange','banana'))
print(newlist)
