# Section: Mixing Positional and Arbitrary Arguments

# Sometimes you'll want to accept several different kinds of arguments, but for
# some arguments you'll want to accept an arbitrary number of arguments. Python
# allows you to combine positional and arbitrary arguments, but the arbitrary
# argument must be the last parameter in the function definition. Python matches
# positional and keyword arguments first and then collects any remaining
# arguments in the final parameter.


def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")


make_pizza(16, "pepperoni")
make_pizza(12, "mushrooms", "green peppers", "extra cheese")
