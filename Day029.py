#Python Loops For Loop
'''A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).'''

#Print each fruit in a fruit list
fruites = ['bannana','apple','cherry']
for x in fruites:
    print(x)

#Even strings are iterable objects, they contain a sequence of characters.
#Loop through the letters in the word "banana"
for x in 'fatmah':
    print(x)
#With the break statement we can stop the loop before it has looped through all the items.
fruites = ['bannana','apple','cherry']
for x in fruites:
    if x=='apple':
        break
    print(x)

#With the continue statement we can stop the current iteration of the loop and continue with the next.
fruites = ['bannana','apple','cherry']
for x in fruites:
    if x=='apple':
        continue
    print(x)