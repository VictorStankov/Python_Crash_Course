motorcycles=['honda','yamaha','suzuki']
print(motorcycles)
motorcycles[0]='ducati' #changing stuff
print(motorcycles)
motorcycles[0]='honda'
motorcycles.append('ducati') #appending stuff
print(motorcycles)
motorcycles=['honda','yamaha','suzuki']
motorcycles.insert(0, 'ducati') #insterting stuff
print(motorcycles)
del motorcycles[0] #deleting stuff
print(motorcycles)
last_owned=motorcycles.pop() #popping stuff
print("The last motorcycle I owned was a "+last_owned.title()+".")
first_owned=motorcycles.pop(0) #popping specific stuff
print("The first motorcycle I owned was a "+first_owned.title()+".")
print(motorcycles) #popped stuff is gone
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print (motorcycles)
too_expensive='ducati'
motorcycles.remove(too_expensive) #removing stuff
print (motorcycles)
print ("\nA "+too_expensive.title()+" is too expensive for me.")