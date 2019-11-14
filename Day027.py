'''Conditional Statements
Python If … Else'''

a = 5
b = 3
if a>b:
    print("a is greater than b")

'''Python relies on indentation (whitespace at the beginning of a line) to define scope in the code. Other programming languages often use curly brackets for this purpose.'''
#If statement, without indentation (will raise an error)
'''the elif keyword is pythons way of saying
if the previous conditions were not true, then try this condition'''
#Else The else keyword catches anything which isn't caught by the preceding conditions.

a = 5
b = 3
if a<b:
    print("b is greater than a")
elif a>b:
    print("a is greater than b")
else:
    print("a is equal to b")

#You can also have an else without the elif
a = 5
b = 3
if a<b:
    print("b is greater than a")
else:
    print("b is equal or not greater to a")


#Short Hand If
'''If you have only one statement to execute, you can put it on the same line as the if statement.'''
if a>b: print("a is greater than b")

#Short Hand If ... Else
'''If you have only one statement to execute, one for if, and one for else, you can put it all on the same line'''

#You can also have multiple else statements on the same line
print("a is greater than b") if a>b else  print("b is equal to a") if a==b else  print("b is not equal or not greater to a")

#The and keyword is a logical operator, and is used to combine conditional statements
if a<b and a==b:
    print("b is greater than and equal to a")
#The or keyword is a logical operator, and is used to combine conditional statements
if a<b or a==b:
    print("b is greater than or equal to a")

#Nested If-You can have if statements inside if statements, this is called nested if statements
if a<10:
    print("a is less than 10")
    if a<5:
        print("a is less than to 5")
    else:
        print("but not less than 5")

