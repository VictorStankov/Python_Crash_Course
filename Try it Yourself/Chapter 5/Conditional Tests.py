car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

food = 'cake'
print('\nIs my favourite food cake?')
print(food == 'cake')
print('\nIs my favourite food potatoes?')
print(food == 'potatoes')

activity = 'Coding'
print('\nIs my favourite activity coding?')
print(activity.lower() == 'coding')
print('\nIs my favourite activity doing homework')
print(activity == 'doing homework')

number = 6
print(number < 7)
print(number > 7)
print(number < 7 or number > 7)
print(7 > number > 7)

no_entry = ['ivan', 'niki', 'alex']
name = 'ivan'
if name in no_entry:
    print('Hell to the no-no')
else:
    print("Welcome")
