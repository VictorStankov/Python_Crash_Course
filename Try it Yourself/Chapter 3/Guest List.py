people=['Slavi','Niki','Ivan']
invitation=', you have been invited to an event.'
print("Dear "+people[0]+invitation)
print("Dear "+people[1]+invitation)
print("Dear "+people[2]+invitation)
#Slavi can't make
people.remove('Slavi')
people.append('Rosen')
print("Dear "+people[0]+invitation)
print("Dear "+people[1]+invitation)
print("Dear "+people[2]+invitation)