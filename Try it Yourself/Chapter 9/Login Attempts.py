class User:
    def __init__(self, first_name, last_name, age, location, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.gender = gender
        self.login_attempts = 0

    def describe_user(self):
        print(f"\nThe following is the user's information:"
              f"\nFirst name: {self.first_name.title()}"
              f"\nLast name: {self.last_name.title()}"
              f"\nAge: {str(self.age)}"
              f"\nLocation: {self.location.title()}"
              f"\nGender: {self.gender.title()}")

    def greet_user(self):
        print(f"\nHello there, {self.first_name.title()} {self.last_name.title()}")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


user_0 = User('victor', 'stankov', 19, 'bulgaria', 'male')
user_0.increment_login_attempts()
user_0.increment_login_attempts()
user_0.increment_login_attempts()
user_0.increment_login_attempts()
user_0.increment_login_attempts()
user_0.increment_login_attempts()
user_0.increment_login_attempts()
print(user_0.login_attempts)
user_0.reset_login_attempts()
print(user_0.login_attempts)
