pizzas = ['pepperoni', 'hamburg', 'sausage']
friend_pizzas = pizzas[:]

pizzas.append('cheese')
friend_pizzas.append('mushrooms')

print("My favorite pizzas are:")
for pizza in pizzas:
	print(pizza)

print("My friend's favorite pizzas are:")
for fpizza in friend_pizzas:
	print(fpizza)

# 'Try it yourself 4-11'