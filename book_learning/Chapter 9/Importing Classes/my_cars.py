# Importing the Car and ElectricCar classes from the car module
from car import Car, ElectricCar

# Creating an instance of the Car class
my_beetle = Car("volkswagen", "beetle", 2019)

# Printing the descriptive name of the car
print(my_beetle.get_descriptive_name())

# Creating an instance of the ElectricCar class
my_tesla = ElectricCar("tesla", "roadster", 2019)

# Printing the descriptive name of the electric car
print(my_tesla.get_descriptive_name())

### Import Method 2
# Another option when importing multiple classes from a module is to just import
# the entire module instead of specifying specific classes
## Example: import car

### Code Changes if importing an entire module.

# You will now have to mention the module name and then use dot notation to call
# upon a class from that module to use it.
# Example: my_beetle = car.Car("volkswagen", "beetle", 2019)

### Import Method 3
# Finally, you can import all classes from a module. This is not recommended, but
# people still do it.

## Example: from module_name import *

### Additional Notes:
# You can also add aliases to classes that you import to organize your code.

## Example:
# from car import ElectricCar as EC
# my_tesla = EC("tesla", "roadster", 2019)
