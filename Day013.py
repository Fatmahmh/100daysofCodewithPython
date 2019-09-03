#Lists
s = []
print(s)

x = [1,2,3,4,5]
print(x)

theLists = ["banana" , 'orange' , "apple"]
print(theLists)


theLists = [1, 2, 3 ,"banana" , 'orange' , "apple"]
print(theLists)
print(theLists[0])
print(theLists[2])
print(theLists[-1])
print(theLists[-3])

#Loop Through a List
for n in theLists:
    print(n)

#Change Item Value
theLists[0]= 10
print(theLists)

#del keyword
del theLists[0]
print(theLists)
del theLists
