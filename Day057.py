#Python Regular Expressions RegEx
#RegEx Module
import re
txt = "the rain in spain"
x = re.search("^the.*spain$",txt)

if (x):
    print("yes we have match")
else:
    print("no match")
