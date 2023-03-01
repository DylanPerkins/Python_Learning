# Section: Using if Statements with Lists
# Sub-section: Checking for Special Items

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry, we are out of green peppers right now.")
    else:
        print(f"Adding {requested_topping}")

print("\nFinished making your pizza!")

# Sub-section: Checking That a List Is Not Empty

requested_toppings2 = []

if requested_toppings2:
    for requested_topping in requested_toppings2:
        print(f"Adding {requested_topping}")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")

# Sub-section: Using Multiple Lists

available_toppings =  ['mushrooms', 'olives', 'green peppers',
 'pepperoni', 'pineapple', 'extra cheese']

requested_toppings3 = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings3:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}")
    else:
        print(f"Sorry, we don't have {requested_topping}.")

print("\nFinished making your pizza!")