### Try it Yourself: 9-1

# Task:  Make a class called Restaurant. The __init__() method for
# Restaurant should store two attributes: a restaurant_name and a cuisine_type.
# Make a method called describe_restaurant() that prints these two pieces of
# information, and a method called open_restaurant() that prints a message
# indicating that the restaurant is open. Make an instance called restaurant
# from your class. Print the two attributes individually, and then call both methods.


class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        """Init restaurant name and cuisine type"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Describe the restaurant"""
        print(
            f"The restaurant is named {self.restaurant_name} and it serves {self.cuisine_type} as its main dish type."
        )

    def open_restaurant(self):
        """Open the restaurant"""
        print(f"The restaurant {self.restaurant_name} is now open!")


my_restaurant = Restaurant("Prime Time Tacos", "Tacos")

print(f"My restaurant is named {my_restaurant.restaurant_name}.")
print(f"We serve {my_restaurant.cuisine_type} at my restaurant.\n")

my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

### Try it Yourself: 9-2

# Task: Start with your class from Exercise 9-1. Create three different instances
#  from the class, and call describe_restaurant() for each instance.

print("\n")
restaurant_one = Restaurant("First Class Bread", "Sandwiches")
restaurant_two = Restaurant("Best in Class Fish", "Seafood")
restaurant_three = Restaurant("World Class Sushi", "Sushi")

restaurant_one.describe_restaurant()
restaurant_two.describe_restaurant()
restaurant_three.describe_restaurant()