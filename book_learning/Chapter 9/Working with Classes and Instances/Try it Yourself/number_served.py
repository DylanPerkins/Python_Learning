### Try it Yourself: 9-4

### Task:
# Start with your program from Exercise 9-1 (page 162). Add an attribute called
# number_served with a default value of 0. Create an instance called restaurant
# from this class. Print the number of customers the restaurant has served, and
# then change this value and print it again.Add a method called
# set_number_served() that lets you set the number of customers that have been
# served. Call this method with a new number and print the value again.Add a
# method called increment_number_served() that lets you increment the number
# of customers who've been served. Call this method with any number you like
# that could represent how many customers were served in, say, a day of business.


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


restaurant = Restaurant("Prime Time Tacos", "Tacos")

# Prints default amount (0)
print(f"We have served {restaurant.number_served} people today.")

# Updates amount served then prints
restaurant.set_number_served(13)
print(f"Now have served {restaurant.number_served} people today.")

# Update by incrementing from instances current amount
restaurant.increment_number_served(9)
print(f"Finally, we served {restaurant.number_served} people today.")
