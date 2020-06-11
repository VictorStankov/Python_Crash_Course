def describe_pet(pet_name, animal_type='dog'):  # default value
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")


describe_pet('hamster', 'harry')  # not defined, prone to errors
describe_pet(animal_type='hamster', pet_name='harry')  #defined, working as intended
describe_pet(animal_type='dog', pet_name='willie')
describe_pet(pet_name='willie', animal_type='dog')
describe_pet('willie')  # using default value
