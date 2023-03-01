players =  ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
# Slices the list and prints the first three items raw

players =  ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[1:4])
# Slices the list and prints the second item to the fourth item raw

players =  ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[:4])
# Slices the list and prints the first four items raw

players =  ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[2:])
# Slices the list and prints from the third item to the end of the list raw

players =  ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[-3:])
# Slices the list and prints the last three items of the list raw

players =  ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:5:2])
# Slices the list and prints the first item, skips the next item, and prints the 3rd, and so on. Then prints the list raw.





players =  ['charles', 'martina', 'michael', 'florence', 'eli']
print("Here are the first three players on my team:")
for player in players[:3]:
	print(player.title())
# Loops through the list only for the first three items.

