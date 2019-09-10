#Make a copy of a dictionary with the copy() method.
thisdict = {
    "brand" : 'ford',
    "model": "mustang",
    "year" : 1996
}
mydict = thisdict.copy()
print(mydict)

#Another way to make a copy is to use the built-in method dict()
mydict2 = dict(thisdict)
print(mydict2)

#Nested Dictionaries
'''A dictionary can also contain many dictionaries, this is called nested dictionaries.'''
myfamily = {
   "child1" : {
       "name" :'Layan',
       "year" : 2004
    },
    "child2" : {
        "name" :'Nizoko',
        "year" : 2001
    },
    "child3" :{
        "name" : "Tanjirou",
        "year" : 1998
    }
}
print(myfamily)


#if you want to nest three dictionaries that already exists as dictionaries.
'''Create three dictionaries, then create one dictionary that will contain the other three
dictionaries.'''
child1 = {
       "name" :'Layan',
       "year" : 2004
    }
child2 = {
        "name" :'Nizoko',
        "year" : 2001
    }
child3 = {
        "name" : "Tanjirou",
        "year" : 1998
    }

myfamilywith3dict = {
    "child1" : child1 ,
"child2" : child2 ,
"child3" : child3
}
print(myfamilywith3dict)

#It is possible to use the dict() constructor to make a new dictionary.
mynewdict = dict(brand='ford', color="red", year=1997)
print(mynewdict)