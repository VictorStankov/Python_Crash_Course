while True:
    number_0 = input("\nPlease enter the first number: ")
    if number_0 == 'q':
        break
    number_1 = input("Please enter the second number: ")
    if number_1 == 'q':
        break
    try:
        print(int(number_0) + int(number_1))
    except ValueError:
        print("That's not a number, jackass.")
