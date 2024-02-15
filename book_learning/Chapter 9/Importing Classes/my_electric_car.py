# Import the ElectricCar class from the python file named car. So, car.py's ElectricCar class.
from car import ElectricCar

# Create an instance of the ElectricCar class
my_tesla = ElectricCar("tesla", "model s", 2019)

# Print the descriptive name of the electric car
print(my_tesla.get_descriptive_name())

# Describe the battery of the electric car
my_tesla.battery.describe_battery()

# Get the range of the electric car
my_tesla.battery.get_range()