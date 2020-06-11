favourite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

print("Sarah's favourite language is " +
      favourite_languages['sarah'].title() +
      ".")

for name, language in favourite_languages.items():
    print(name.title() + "'s favourite language is " + language.title() + '.')

friends = ['phil', 'sarah']
for name in favourite_languages:
    print(name.title())

    if name in friends:
        print("Hi " + name.title() +
              ", I see your favourite language is " +
              favourite_languages[name].title() + "!")

if 'erin' not in favourite_languages:
    print("Erin, please take our poll!")

for name in sorted(favourite_languages):
    print(name.title() + ", thank you for taking the poll.")

print("\nThe following languages have been mentioned:")
for language in favourite_languages.values():
    print(language.title())

print("\nThe following languages have been mentioned:")  # set for repeating stuff
for language in set(favourite_languages.values()):
    print(language.title())

favourite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
    }

for name, languages in favourite_languages.items():
    print("\n" + name.title() + "'s favourite languages are:")
    for language in languages:
        print("\t" + language.title())