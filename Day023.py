
thisdict = {
    "brand" : 'ford',
    "model": "mustang",
    "year" : 1996
}
#Check if Key Exists
if "model" in thisdict:
    print("yes model is one of the keys in this dict")
#To determine how many items (key-value pairs) a dictionary has, use the len() method.
print(len(thisdict))


#Add item
thisdict["color"] = "red"
print(thisdict.items())

#The pop() method removes the item with the specified key name.
thisdict.pop("model")
print(thisdict)

'''The popitem() method removes the last inserted item.
(in versions before 3.7, a random item is removed instead).'''
thisdict.popitem()
print(thisdict)


#The del keyword removes the item with the specified key name.
del thisdict["brand"]
print(thisdict)
#The del keyword can also delete the dictionary completely.
del thisdict #wiil remove the dict

#print(thisdict) // this will cause an error because "thisdict" no longer exists.

#The clear() keyword empties the dictionary.
thisdict = {
    "brand" : 'ford',
    "model": "mustang",
    "year" : 1996
}
thisdict.clear()
print(thisdict)

