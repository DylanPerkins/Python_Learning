# Section: A List in a Dictionary

# Store info about a pizza being ordered
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese']
}

# Summarize the order
print(f"You order a {pizza['crust']}-crust pizza "
    "with the following toppings:")

# Lists out the values in the key 'toppings'
for topping in pizza['toppings']:
    print(f"\t{topping}")