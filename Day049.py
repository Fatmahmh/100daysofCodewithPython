#Python Scope 2
x=300
def myfunc():
    x=200
    print(x)
myfunc()
print(x)


def myfunc2():
    global y
    y = 300
    print(y)
myfunc2()
print(y)

