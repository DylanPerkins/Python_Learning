# Section: Default Values
# A default value is a value that is assigned to a parameter in the function definition.
# If an argument for a parameter is provided in the function call, Python uses the argument value instead of the default.
def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('loki') # Uses the default value for animal_type

describe_pet(pet_name='luna', animal_type='cat') # Superseeds the default value for animal_type