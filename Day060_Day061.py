import json
#Q1
tuple = ("Sunday","monday","Tuesday","Wednesday","Thursday","Friday","Saturday")
print(json.dumps(tuple))

import re
#Q2
txt = "data is the new oil"
x = re.search(".*data.*",txt)
print(x)
