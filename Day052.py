#Python Datetime

'''Python Dates - A date in Python is not a data type of its own, but we can import a module named datetime to work with dates as date objects.
'''

import datetime

x = datetime.datetime.now()
print(x)
print(x.year)
#The datetime() class also takes parameters for time and timezone (hour, minute, second, microsecond, tzone), but they are optional, and has a default value of 0, (None for timezone).

#Create a date object
x = datetime.datetime(2020,5,17)
print(x)

#The strftime() Method
print(x.strftime("%B"))

