import json

filename = 'f_number.json'
with open(filename) as f_obj:
    number = json.load(f_obj)
    print(f"I know your favourite number is {number}.")