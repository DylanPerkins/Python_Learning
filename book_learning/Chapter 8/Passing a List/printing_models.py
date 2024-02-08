# Section: Modifing a List in a Function

# When you pass a list to a function, the function can modify the list. Any
# changes made to the list inside the function’s body are permanent


def print_models(unprinted_designs, completed_models):
    """
    Simulate printing each design, until none are left to print.
    Then, move each design to 'completed_models' after printing.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing Model: {current_design.title()}")
        completed_models.append(current_design.title())


def show_completed_models(completed_models):
    """Show all of the models that were printed"""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)


unprinted_designs = ["phone case", "robot pendant", "dodecahedron"]
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)
