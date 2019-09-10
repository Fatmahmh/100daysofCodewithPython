thisset = {}
print(thisset)

#Create a Set.
thisset = {'apple', 'cherry', ' banana'}
print(thisset)



#//
thisset = {'apple',1,2,1,5}
print(thisset)
for x in thisset:
    print(x)

print("apple" in thisset)

#Add an item to a set, using the add() method.
thisset.add("orange")
print(thisset)
thisset.update(['cherry','banana'])
print(thisset)



