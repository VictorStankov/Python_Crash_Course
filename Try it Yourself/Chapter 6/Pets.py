sid = {'type': 'dog', 'owner': 'mira'}
barkley = {'type': 'dog', 'owner': 'yan'}
penka = {'type': 'cat', 'owner': 'slavi'}

pets = [sid, barkley, penka]

for pet in pets:
    print(f"\nName: {pet}" +
          "\nType: " + str(pet['type']) +
          "\nOwner: " + str(pet['owner']))