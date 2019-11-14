#Python Lambda 2
'''The power of lambda is better shown when you use them as an anonymous function inside another function.'''

def my_function(n):
    return lambda a : a*n

mydoubler = my_function(2)
print(mydoubler(11))

mytripler = my_function(3)
print(mytripler(11))


