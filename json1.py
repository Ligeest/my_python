import json

filename = "nb.json"
with open(filename) as f_obj:
    print(json.load(f_obj))