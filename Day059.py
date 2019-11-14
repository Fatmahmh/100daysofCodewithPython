#Python RegEx 3
#The sub() function replaces the matches with the text of your choice:
import re
txt = "the rain in spain"
x = re.sub("\s","9",txt)
print(x)


#You can control the number of replacements by specifying the count parameter
x = re.sub("\s","9",txt , 2)
print(x)

#A Match Object is as object containing information about the search and the result
x = re.search("ai",txt)
print(x)

#The Match object has properties and methods used to retrieve information about the search, and the result.
x = re.search(r"\bS\w+",txt)
print(x.string)