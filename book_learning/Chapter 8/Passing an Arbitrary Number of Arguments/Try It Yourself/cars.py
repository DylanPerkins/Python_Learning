# Try it Yourself | 8-12

### Task: Write a function that stores information about a car in a dictionary.
# The function should always receive a manufacturer and a model name.
# It should then accept an arbitrary number of keyword arguments.
# Call the function with the required information and two other name-value pairs,
# such as a color or an optional feature. Your function should work for a call like this one:
# car = make_car('subaru', 'outback', color='blue', tow_package=True)
# Print the dictionary that’s returned to make sure all the information was stored correctly.
###


def make_car(manufacturer, model, **car_info):
    """Stores information about a car in a dictionary"""
    car = {}

    car["manufacturer"] = manufacturer
    car["model"] = model

    for key, value in car_info.items():
        car[key] = value

    return car


car = make_car("subaru", "outback", color="blue", premium_package=True)

print(car)
