favourite_places = {'mira': ['paris', 'home', 'france'],
                    'slavi': ['druzhba', 'sofia', 'corsa'],
                    'victor': ['sofia', 'school', 'basement']
                    }
for person, place in favourite_places.items():
    print(person.title() + "'s favourite places are: " +
          str(place).title())
