sandwich_orders = ['tuna', 'cheese', 'bacon', 'ham', 'vegetarian']
finished_sandwiches = []

while sandwich_orders:
    for sandwich in sandwich_orders:
        finished_sandwich = sandwich_orders.pop()
        print("Making a " + finished_sandwich + " sandwich.")
