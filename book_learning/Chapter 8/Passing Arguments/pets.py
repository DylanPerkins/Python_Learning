# Section: Positional Arguments + Multiple Function Calls

# This program demonstrates how to pass arguments to a function
def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('cat', 'luna')
describe_pet('dog', 'loki')

# Section: Keyword Arguments
# The order doesn't matter when you use keyword arguments
describe_pet(animal_type='cat', pet_name='luca')