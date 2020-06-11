favourite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

p_should_take = ['ivan', 'jen', 'ratilla', 'frank', 'josh', 'edward']

for person in p_should_take:
    if person in favourite_languages.keys():
        print(person.title() + ", thank you for taking the poll.")
    else:
        print(person.title() + ", please take our poll!")
