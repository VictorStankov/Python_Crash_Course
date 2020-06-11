squares=[]
#for value in range(1,11):
   # square=value**2
   # squares.append(square)
#print(squares)

for value in range(1,11):
    squares.append(value**2) #better (omitting the use of a variable)
print(squares)

squares=[]
squares=[value**2 for value in range(1,11)] #list comprehension
print(squares)