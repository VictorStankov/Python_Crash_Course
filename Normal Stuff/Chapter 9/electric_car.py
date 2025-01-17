# class Car:
#     """A simple attempt to represent a car."""
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0
#         self.fuel = 50
#
#     def get_descriptive_name(self):
#         long_name = str(self.year) + ' ' + self.make + ' ' + self.model
#         return long_name.title()
#
#     def read_odometer(self):
#         print("This car has " + str(self.odometer_reading) + " miles on it.")
#
#     def update_odometer(self, mileage):
#         if mileage >= self.odometer_reading:
#             self.odometer_reading = mileage
#         else:
#             print("You can't roll back an odometer!")
#
#     def increment_odometer(self, miles):
#         self.odometer_reading += miles
#
#     def fill_gas_tank(self, number):
#         self.fuel += number
#         print(f"Your car has now {str(self.fuel)} liters of fuel.")
from car import Car

class Battery:
    """A simple attempt to model a battery for an electric car."""
    def __init__(self, battery_size=70):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"This car has a {str(self.battery_size)}-kWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270

        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)


class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    def __init__(self, make, model, year):
        """Initialize attributes of the parent class."""
        super().__init__(make, model, year)
        self.battery_size = Battery()

    # def describe_battery(self):
    #     """Print a statement describing the battery size."""
    #     print(f"This car has a {str(self.battery_size)}-kWh battery.")

    def fill_gas_tank(self, number):
        """Electric cars don't have gas tanks."""
        print("This car doesn't need a gas tank!")


# my_tesla = ElectricCar('tesla', 'model s', 2016)
# my_car = Car('VW', 'golf', 1999)
# print(my_tesla.get_descriptive_name())
# my_tesla.battery_size.describe_battery()
# # my_car.fill_gas_tank(10)
# # my_tesla.fill_gas_tank(10)
# my_tesla.battery_size.get_range()
