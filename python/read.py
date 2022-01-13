import json
from re import A

member = {}

with open('save.json') as json_file:
    member = json.load(json_file)
 
    # for reading nested data [0] represents
    # the index value of the list
    try:
        print(member["Hello"])
    except KeyError:
        print("Error: No result found.")