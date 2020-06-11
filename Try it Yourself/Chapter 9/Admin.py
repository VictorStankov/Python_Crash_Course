class User:
    def __init__(self, first_name, last_name, age, location, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.gender = gender

    def describe_user(self):
        print(f"\nThe following is the user's information:"
              f"\nFirst name: {self.first_name.title()}"
              f"\nLast name: {self.last_name.title()}"
              f"\nAge: {str(self.age)}"
              f"\nLocation: {self.location.title()}"
              f"\nGender: {self.gender.title()}")

    def greet_user(self):
        print(f"\nHello there, {self.first_name.title()} {self.last_name.title()}")


class Privileges:
    def __init__(self):
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        for privilege in self.privileges:
            print(privilege)


class Admin(User):
    def __init__(self, first_name, last_name, age, location, gender):
        super().__init__(first_name, last_name, age, location, gender)
        self.privileges = Privileges()



user_0 = User('victor', 'stankov', 19, 'bulgaria', 'male')
user_1 = Admin('esteban', 'garcia', 21, 'cave', 'black')
user_1.privileges.show_privileges()
