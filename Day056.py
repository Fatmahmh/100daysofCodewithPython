#Python JSON 2
#The json.dumps() method has parameters to make it easier to read the result:
#Use the indent parameter to define the numbers of indents
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

print(json.dumps(x, indent=4 ,separators=(".","="),sort_keys=True ))
#Use the sort_keys parameter to specify if the result should be sorted or not:
