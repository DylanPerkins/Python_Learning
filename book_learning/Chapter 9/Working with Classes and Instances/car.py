class Car:
    """A simple attempt to represent a car"""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted and descriptive name"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement that shows the car's mileage"""
        print(f"This car has {self.odometer_reading} miles on it")

    # Method attribute modification
    # def update_odometer(self, mileage):
    #     """Set the odometer reading to the given value"""
    #     self.odometer_reading = mileage

    # Method attribute modification (with rejection logic)
    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    # Incremental attribute modification
    def increment_odometer(self, miles):
        """Add the given amount of miles to the odometer"""
        self.odometer_reading += miles


my_new_car = Car("audi", "RS e-tron", 2024)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

# Direct attribute modification
my_new_car.odometer_reading = 23
my_new_car.read_odometer()

# Method attribute modification
my_new_car.update_odometer(45)
my_new_car.read_odometer()

# Incremental attribute modification
my_used_car = Car("toyota", "camry", 2019)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(25_500)
my_used_car.read_odometer()

my_used_car.increment_odometer(132)
my_used_car.read_odometer()

### Notes:

# When an instance is created, attributes can be defined without being
# passed in as parameters. These attributes can be defined in the __init__()
# method, where they are assigned a default value.

# You can change an attribute's value in three ways: you can change the value
# directly through an instance, set the value through a method, or increment
# the value (add a certain amount to it) through a method. Let's look at each
# of these approaches.
