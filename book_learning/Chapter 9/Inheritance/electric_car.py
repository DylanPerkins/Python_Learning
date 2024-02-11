# Parent Class
class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles


class Battery:
    """A simple attempt to model a battery for an electric car"""

    def __init__(self, battery_size=75) -> None:
        """Initialize a battery's attributes"""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size"""
        print(f"This car has a {self.battery_size}-kWh battery")

    def get_range(self):
        """Print a statement about the range of the battery"""
        if self.battery_size == 75:
            battery_range = 260
        elif self.battery_size == 100:
            battery_range = 315

        print(f"This vehicle can go about {battery_range} miles on a full charge.")


# Child Class
class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles"""

    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)  # Inits all parent attributes
        self.battery = Battery()  # Init new attribute from a class
        # self.battery_size = 75   Init new attribute only linked to this class


my_tesla = ElectricCar("tesla", "model s", 2019)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

### Notes:

# You can override any method from the parent class that doesn't fit what
# you're trying to model with the child class. To do this, you define a method
# in the child class with the same name as the method you want to override in
# the parent class. Python will disregard the parent class method and only
# pay attention to the method you define in the child class.
