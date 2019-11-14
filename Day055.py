#Python JSON
"""JSON is a syntax for storing and exchanging data--
Python has a built-in package called json, which can be used to work with JSON data.
"""
#Convert from JSON to Python:
import json

x = '{"name":"john","age":25 , "city":"new york"}'
#pars x
y = json.loads(x)

#the result is python dict
print(y["age"])

#Convert from Python to JSON
'''If you have a Python object, you can convert it into a JSON string by using the json.dumps() method.'''

#python object dict
x = {"name":"john" , "age": 30 , "city":"new work"}
#convert into json
y  = json.dumps(x)
#the result is python string
print(y)


#Convert Python objects into JSON strings, and print the values:
print(json.dumps("hello"))
print(json.dumps(24))
print(json.dumps(False))

#When you convert from Python to JSON, Python objects are converted into the JSON (JavaScript) equivalent:
import json
x = {
    "name" : "john" ,
    "age": 25,
    "marreid": True,
    "divorced": False,
    "children": ("anni","bille"),
    "pets": None,
    "cars": [
        {"model":"BMW 230","mpg":26.5},
        {"model":"ford edge","mpg":24.1}
    ]
}

print(json.dumps(x))