requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
    print("Hold the anchovies!")
# Created a variable with a value 'mushrooms'
# Made an if statement where if the value(s) in requested_topping ...
# ... Does not equal 'anchovies', then you print a statement.


requested_toppings = ['mushrooms', 'onions', 'pineapple']
print('mushrooms' in requested_toppings)
# Finds whether or not the value 'mushrooms' is in the list requested_toppings
print('pepperoni' in requested_toppings)
# Finds whether or not the value 'pepperoni' is in the list requested_toppings


# testing multiple conditions
requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese")

print("\nYour pizza has been finished being made!")