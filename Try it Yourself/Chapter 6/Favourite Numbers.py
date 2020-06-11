favourite_numbers = {'john': 3, 'ivan': 5, 'pete': 8, 'andrew':10, 'frank': 65}
print(favourite_numbers['john'])
print(favourite_numbers['ivan'])
print(favourite_numbers['pete'])
print(favourite_numbers['andrew'])
print(favourite_numbers['frank'])

favourite_numbers = {'john': [3, 4],
                     'ivan': [5, 6],
                     'pete': [8, 9],
                     'andrew': [10, 11],
                     'frank': [65, 66],
                     }

for person, number in favourite_numbers.items():
    print(person.title() + "'s favourite numbers are:" + str(number) + ".")
