import json

filename = 'f_number.json'
with open(filename,  'w') as f_obj:
    number = input("Please enter your favourite number: ")
    json.dump(number, f_obj)
