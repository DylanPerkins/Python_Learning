### Try it Yourself: 9-6

### Task:
# An ice cream stand is a specific kind of restaurant. Write a class called
# IceCreamStand that inherits from the Restaurant class you wrote in
# Exercise 9-4 (page 167). Add an attribute called flavors that stores a list
# of ice cream flavors. Write a method that displays these flavors. Create an
# instance of IceCreamStand, and call this method.


class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        """Init restaurant name and cuisine type"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Describe the restaurant"""
        print(
            f"The restaurant is named {self.restaurant_name} and it serves {self.cuisine_type} as its main dish type."
        )

    def open_restaurant(self):
        """Open the restaurant"""
        print(f"The restaurant {self.restaurant_name} is now open!")

    def set_number_served(self, amount):
        """Set the number of customers served to the given amount"""
        self.number_served = amount

    def increment_number_served(self, amount):
        """Increment the amount of customers served"""
        self.number_served += amount


class IceCreamStand(Restaurant):

    def __init__(self, restaurant_name, cuisine_type, *flavors):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    def display_flavors(self):
        """Display the flavors of ice cream"""
        print("The flavors we have are:")
        for flavor in self.flavors:
            print(f"\t{flavor}")

iceCreamStand = IceCreamStand("Ice Cream Emporium", "Ice Cream", "Vanilla", "Chocolate", "Swirl", "Mint")
iceCreamStand.display_flavors()