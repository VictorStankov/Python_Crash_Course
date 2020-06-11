people=['Slavi','Niki','Ivan']
invitation=', you have been invited to an event.'
message=", I've purchased a bigger table so we'll be able to invite 3 more people"
print("Dear "+people[0]+message)
print("Dear "+people[1]+message)
print("Dear "+people[2]+message)
people.insert(1,'Mariya')
people.insert(3,'Kocko')
people.append('Alex')
print("\nDear "+people[0]+invitation)
print("Dear "+people[1]+invitation)
print("Dear "+people[2]+invitation)
print("Dear "+people[3]+invitation)
print("Dear "+people[4]+invitation)
print("Dear "+people[5]+invitation)

#The table won't arrive

apology=", due to unforseen factors, the event has been called off."
left_out_guy=people.pop(0)
print("\nDear "+left_out_guy+apology)
left_out_guy=people.pop(0)
print("Dear "+left_out_guy+apology)
left_out_guy=people.pop(0)
print("Dear "+left_out_guy+apology)
left_out_guy=people.pop(0)
print("Dear "+left_out_guy+apology)
message_2=', due to unforseen factors, the others will not be able to come to the event.'
print("\nDear "+people[0]+message_2)
print("Dear "+people[1]+message_2)
print(len(people))