#Dictionary

#Empty dictionary.
thisdict = {}
thisdict = {
    "brand" : 'ford',
    "model": "mustang",
    "year" : 1996
}

print(thisdict)
print(thisdict["model"])

#Get the value of the  key.
print(thisdict.get('model'))

#You can change the value of a specific item by referring to its key name.
thisdict["year"] = 2019
print(thisdict)

#Loop Through a Dictionary
#print keys
for n in thisdict:
    print(n)

    #print values
for n in thisdict:
        print(thisdict[n])

print(thisdict.values())
print(thisdict.keys())

#the items() function.
print(thisdict.items())

#Loop through both keys and values, by using the items() function
for x,y in thisdict.items():
    print(x,y)




