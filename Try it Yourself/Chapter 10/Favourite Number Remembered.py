import json

filename = 'f_number.json'
try:
    with open(filename) as f_obj:
        number = json.load(f_obj)
except FileNotFoundError:
    with open(filename, 'w') as f_obj:
        number = input("Please enter your favourite number: ")
        json.dump(number, f_obj)
else:
    print(f"I know your favourite number is {number}.")
