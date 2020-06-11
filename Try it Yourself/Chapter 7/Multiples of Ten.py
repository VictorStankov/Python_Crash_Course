number = input("Please give me a number and I'll tell you if it's devisable by 10: ")
number = int(number)

if number % 10 == 0:
    print("The number " + str(number) + " is a multiple of ten.")
else: print("The number " + str(number) + " is not a multiple of ten.")