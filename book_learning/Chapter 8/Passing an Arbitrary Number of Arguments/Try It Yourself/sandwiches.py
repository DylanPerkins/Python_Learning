# Try it Yourself | 8-12

# Task:
# Write a function that accepts a list of items a person wants on a sandwich.
# The function should have one parameter that collects as many items as the
# function call provides, and it should print a summary of the sandwich
# that's being ordered. Call the function three times, using a different
# number of arguments each time.


def build_a_sandwich(*ingredients):
    """Prints out what's going on your sandwich"""
    print("Creating your sandwich with the following ingredients: ")
    for ingredient in ingredients:
        print(f"- {ingredient}")
    print("\n")


build_a_sandwich("lettuce")
build_a_sandwich("steak", "lettuce", "peppers")
build_a_sandwich("hamburger", "ketchup", "cheese", "pickles")
