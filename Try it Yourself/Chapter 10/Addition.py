number_0 = input("\nPlease enter the first number: ")
number_1 = input("Please enter the second number: ")
try:
    print(int(number_0) + int(number_1))
except ValueError:
    print("That's not a number, jackass.")
