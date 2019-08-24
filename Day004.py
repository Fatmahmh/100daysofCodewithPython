x = 1  #int
y = 2.8  #float
z = 1j  #complex
print(type(x))
print(type(y))
print(type(z))

#  int
x = 1
y = 398476997897685743094
z = -8465846
print(type(x))
print(type(y))
print(type(z))

#  float
x = 1.5
y = 1.0
z = -35.65
print(type(x))
print(type(y))
print(type(z))

#  float
x = 35e4
y = 12E3
z = -87.6e100
print(type(x))
print(type(y))
print(type(z))

#  complex
x = 3+4j
y = 4j
z = -5j
print(type(x))
print(type(y))
print(type(z))


#  Type Conversion
x = 1   #int
y = 2.8  #float
z = 1j  #complex

#  convert from int to float
a = float(x)
print(a)
print(type(a))
#  convert frm float to int
b = int(y)
print(b)
print(type(b))
#  convert from int to complex
c = complex(x)
print(c)
print(type(c))

#random module
import random
print(random.randrange(1,10))
print(random.randrange(1,10))
print(random.randrange(1,10))
print(random.randrange(1,10))