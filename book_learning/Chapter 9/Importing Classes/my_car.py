# Import the Car class from the python file named car. So, car.py's Car class.
from car import Car

# Create a new Car instance
my_new_car = Car("audi", "a4", 2019)

# Print a formatted string that describes the car
print(my_new_car.get_descriptive_name())

# Set the odometer reading of the car to 23
my_new_car.odometer_reading = 23

# Print the current odometer reading of the car
my_new_car.read_odometer()
