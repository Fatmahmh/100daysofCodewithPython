#Python Modules 2
#There are several built-in modules in Python, which you can import whenever you like.

import platform


x= platform.system()
print(x)
print(platform.python_version())


#There is a built-in function to list all the function names (or variable names) in a module. The dir() function.
#The dir() function can be used on all modules, also the ones you create yourself.

x = dir(platform)
print(x)

#You can choose to import only parts from a module, by using the from keyword.
from mymodule import person1
'''When importing using the from keyword, do not use the module name when referring to elements in the module.'''
