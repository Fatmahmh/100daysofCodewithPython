# Logical Operators
x = 5
print(x > 5 or x < 4)
print(x > 5 and x < 4)
print(not x < 4)


#Identity Operators
''' if they are actually the same object, with the same memory location.'''
x = 5
y = 5
z = x
print("           ")
print(x is z )
print(x is not z )
print(x is y)
print(x != z )
print(x == z )
print(z == y )



# Membership Operators
x = ['apple' , 'orange']
print('orange' in x)
print('orange'  not in x)
print('banana' in x)
print('banana' not in x)



#Bitwise Operators
