players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3]) #beginning:end
print(players[1:4])
print(players[:4])
print(players[2:])
print(players[-3:])
print("\nHere are the first three player on my team:")
for player in players[:3]:
    print player.title()