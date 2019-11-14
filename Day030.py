#Python Loops3 For Loop
'''The range() Function To loop through a set of code a specified number of times, we can use the range() function,
The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.'''

for x in range(6):
    print(x)

'''The range() function defaults to 0 t is possible to specify the starting value by adding a parameter: range(2, 6), which means values from 2 to 6
(but not including 6)'''
for x in range(2,6):
    print(x)

'''The range() function defaults to increment the sequence by 1, however it is possible to specify the increment value by adding a third parameter: range(2, 30, 3)'''
for x in range(2,30,3):
    print(x)

#Else in For Loop The else keyword in a for loop specifies a block of code to be executed when   loop is finished
#Print all numbers from 0 to 5, and print a message when the loop has ended
for x in range(2,6):
    print(x)
else:
    print("finally finished")


'''Nested Loops
A nested loop is a loop inside a loop.
The "inner loop" will be executed one time for each iteration of the "outer loop'''

#print each adjective for every fruit.

adj = ['red','big','testy']
fruites = ['apple','cherry','bannana']

for x in adj:
    for y in fruites:
        print(x,y)
