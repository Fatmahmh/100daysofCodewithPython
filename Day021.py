#Get the Length of a Set
thisset = {'apple', 'cherry', 'banana'}
print(len(thisset))
#To remove an item in a set, use the remove(), or the discard() method.
thisset.remove('apple')
thisset.discard('cherry')


#pop() method
thisset = {'apple', 'cherry', 'banana'}
x = thisset.pop()
print(x)
print(thisset)

#clear() method empties the set.
thisset.clear()
print(thisset)

#The del keyword will delete the set completely.
#this will raise an error because the set no longer exists


del thisset
#the set() constructor to make a set
thisset = set((1,2,3,4,5))
print(thisset)



