#Python Scope
'''A variable created inside a function belongs to the local scope of that function, and can only be used inside that function.'''

def myfunc():
    x = 5
    print(x)
myfunc()

#Function Inside Function
def myfunc():
    x = 5
    def myinsidfunc():
        print(x)
    myinsidfunc()

myfunc()

#Global Scope
'''A variable created in the main body of the Python code is a global variable and belongs to the global scope'''
x = 300
def myfunc():
     print(x)

myfunc()
print(x)

