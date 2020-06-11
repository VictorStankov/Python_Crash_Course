prompt = ("Enter a pizza topping: ")
prompt += "\nType 'quit' if you want to exit. "

condition = True
while condition:
    toppings = input(prompt)
    if toppings == 'quit':
        break
    else:
        print("Adding " + toppings + " to the pizza.")
