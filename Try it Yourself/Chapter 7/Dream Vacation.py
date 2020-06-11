prompt_0 = "If you want to quit type 'quit'"
prompt_0 += "\nWhat is your name? "
prompt_1 = "If you could visit one place in the world, where would you go? "
favourite_places = {}

flag = True
while flag:
    name = input(prompt_0)
    if name == 'quit':
        break
    place = input(prompt_1)
    favourite_places[name] = place
for person, response in favourite_places.items():
    print(str(person).title() + " would like to visit " + str(response).title() + ".")
