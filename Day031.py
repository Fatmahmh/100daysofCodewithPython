#Python Functions
#A function is a block of code which only runs when it is called. You can pass data, known as parameters, into a function. A function can return data as a result


#In Python a function is defined using the def keyword

def my_function():
    print("hello from a function")

my_function()

#Parameters are specified after the function name, inside the parentheses. You can add as many parameters as you want, just separate them with a comma.
def my_function(fname):
    print(fname+" refsnes")

my_function("Email")
my_function("Tobias")
my_function("Linus")

#If we call the function without parameter, it uses the default value.
def my_function(countery='taif'):
    print('i am from '+ countery)
my_function("India")
my_function("Brazil")
my_function()