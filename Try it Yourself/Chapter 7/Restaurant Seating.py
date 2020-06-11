people = input("How many people are in your dinner group? ")
people = int(people)

if people > 8:
    print("I'm sorry but you will have to wait for a table.")
else:
    print("Your table is ready.")