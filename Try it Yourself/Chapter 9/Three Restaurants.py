class Restaurant:
    """I have no idea"""
    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine

    def describe_restaurant(self):
        print(f"The restaurant's name is {self.name.title()}.")
        print(f"The restaurant's cuisine is {self.cuisine.title()}.")

    def open_restaurant(self):
        print(f"The {self.name.title()} restaurant has been opened.")


restaurant_0 = Restaurant('Ratas', 'rats')
restaurant_1 = Restaurant('idk man', 'beef')
restaurant_2 = Restaurant('AAAAAAAA', 'pork I guess')

restaurant_0.describe_restaurant()
print()
restaurant_1.describe_restaurant()
print()
restaurant_2.describe_restaurant()
