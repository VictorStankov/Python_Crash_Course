class Restaurant:
    """I have no idea"""
    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine
        self.number_served = 0

    def describe_restaurant(self):
        print(f"\nThe restaurant's name is {self.name.title()}.")
        print(f"The restaurant's cuisine is {self.cuisine.title()}.")
        print(f"The restaurant has served {str(self.number_served)} people.")

    def open_restaurant(self):
        print(f"The {self.name.title()} restaurant has been opened.")

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, number):
        self.number_served += number


restaurant_0 = Restaurant('aaaaa', 'asd')
restaurant_0.number_served = 15
restaurant_0.describe_restaurant()
restaurant_0.set_number_served(20)
restaurant_0.describe_restaurant()
restaurant_0.increment_number_served(5)
restaurant_0.describe_restaurant()
