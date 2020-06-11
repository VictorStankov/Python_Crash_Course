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


class IceCreamStand(Restaurant):
    def __init__(self, name, cuisine):
        super().__init__(name, cuisine)
        self.flavours = ['vanilla', 'chocolate', 'strawberry']

    def show_flavours(self):
        for flavour in self.flavours:
            print(flavour)


restaurant_0 = IceCreamStand('Ratas', 'rats')
restaurant_0.show_flavours()
