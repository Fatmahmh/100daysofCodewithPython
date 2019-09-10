#Create a Tuple.
thistuple = ('apple ','bannana' , 'orange')
print(thistuple)

#empty tuple in Python
thistuple = ()
print(thistuple)

#tuple with one element

'''إذا كان ال tuple يحتوي على عنصر واحد فقط،
يجب عليك وضع فاصلة , بعد القيمة كما في المثال
نتيجة تشغيل الكود
نتيجة تشغيل الكود
حتى يتم التفريق بين tuple و المتغير العادي في بايثون.
'''

thistuple = (3, )
print(thistuple)

#The data inside a tuple can be of one or more data types.
thistuple = ('ahmed',2 , 1.2 ,'python')
print(thistuple)


#You can access tuple items by referring to the index number, inside square brackets [].
print(thistuple[2])

#Once a tuple is created, tuples are unchangeable

#You can loop through the tuple items by using a for loop.

tuple1 = ('apple ', 'bannana', 'orange')
for n in tuple1:
    print(n)

    #You cannot remove items in a tuple.//but you can delete the tuple completely.
    del thistuple
    #print(thistuple)


#//
    thistuple = ('apple ', 'bannana', 'orange','cherry')
    print(thistuple[0:2])
