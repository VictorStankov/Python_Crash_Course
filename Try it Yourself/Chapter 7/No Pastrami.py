sandwich_orders = ['tuna', 'pastrami', 'cheese', 'bacon', 'pastrami', 'ham', 'vegetarian', 'pastrami']

print(sandwich_orders)

while True:
    for sandwich in sandwich_orders:
        if sandwich == 'pastrami':
            sandwich_orders.remove(sandwich)
    print(sandwich_orders)
    break