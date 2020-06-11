cities = {
    'sofia': {
        'country': 'bulgaria',
        'pop': 1286383,
        'fact': "It's the capital",
        },
    'plovdiv': {
        'country': 'bulgaria',
        'pop': 368983,
        'fact': "Danev lives there"
        },
    'pernik': {
        'country': 'bulgaria',
        'pop': 78342,
        'fact': "They have no water",
        },
    }

for city, info in cities.items():
    country = info['country']
    pop = info['pop']
    fact = info['fact']

    print("\nCity: " + str(city).title())
    print("Country: " + country.title() +
          "\nPopulation: " + str(pop) +
          "\nFact: " + fact)
