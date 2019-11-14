#Python RegEx 2
#The findall() function returns a list containing all matches.
import re
txt = "the rain in spain"
x = re.findall("ai",txt)
print(x)

txt = "the rain in spain"
x = re.findall("pro",txt)
print(x)
if (x):
    print("yes we have match")
else:
    print("no match")

#The search() function searches the string for a match, and returns a Match object if there is a match.
x = re.search("\s",txt)
print(x.start())

#The split() function returns a list where the string has been split at each match:
x = re.split("\s",txt)
print(x)
