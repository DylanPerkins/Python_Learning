# Section: Passing an Arbitrary Number of Arguments

# Python allows a function to collect an arbitrary number of arguments from the
# calling statement.

def make_pizza(*toppings):
    """Print the list of toppings that have been requested."""
    print(toppings)

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

# The asterisk in the parameter name *toppings tells Python to make an empty
# tuple called toppings and pack whatever values it receives into this tuple.