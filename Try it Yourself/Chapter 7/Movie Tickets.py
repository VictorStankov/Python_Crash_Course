prompt = "Please enter your age, so we can tell you the price of the ticket: "

while True:
    age = input(prompt)
    age = int(age)
    if age <= 3:
        print("The ticket is free for you!")
    elif age <= 12:
        print("The ticket costs $10 for you.")
    else:
        print("The ticket costs $15 for you.")
