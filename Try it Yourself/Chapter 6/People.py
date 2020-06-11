slavi = {'first_name': 'Svetoslav', 'last_name': 'Ivanov', 'age': 13, 'city': 'Druzhba'}
niki = {'first_name': 'Nikolai', 'last_name': 'Lalev', 'age': 17, 'city': 'Sofia'}
victor = {'first_name': 'Victor', 'last_name': 'Stankov', 'age': 19, 'city': 'Sofia'}

people = []
people.append(slavi)
people.append(niki)

for person in people:
    print("\nFirst name: " + str(person['first_name']) +
          "\nLast name: " + str(person['last_name']) +
          "\nAge: " + str(person['age']) +
          "\nCity: " + str(person['city']))
