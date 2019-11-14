#Python Functions 2
'''You can send any data types of parameter to a function'''


def my_function(food):
    for x in food :
        print(x)

fruites = [ 'apple','bannana' , 'cherry']
my_function(fruites)

#Return Values
def my_function(x):
    return 5*x

print(my_function(11))
print(my_function(12))

'''Keyword Arguments
You can also send arguments with the key = value syntax.
This way the order of the arguments does not matter.'''

def myfunction(child1,child2,child3):
    print('the oungest child is'+ child3)
myfunction(child3='nizoko',child2='raghad',child1='didi')

'''Arbitrary Arguments
If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.'''
#in this way it will accept any number of argument when it called
def myfunction(*kids):
    print('the youngest child' +kids[2])
myfunction('Email','car','tanjiro')

#Recursion
def Recursion(k):
    if (k>0):
        result = k + Recursion(k-1)
        print(result)
    else:
        result = 0
        return result
print('Recursion example result')
Recursion(6)




