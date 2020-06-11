rivers = {'nile': 'egypt',
          'iskar': 'bulgaria',
          'amazon river': 'brazil',
          }

for river, country in rivers.items():
    print("The " + river.title() + " runs through " + country.title() + ".")
