# The Python Standard Library is a collection of modules that come with Python installation.
# It provides a wide range of functionality for various tasks, eliminating the need for external libraries.

# Some commonly used modules in the Python Standard Library include:
# - os: Provides functions for interacting with the operating system, such as file operations.
# - sys: Provides access to some variables used or maintained by the interpreter and functions that interact with the interpreter.
# - math: Provides mathematical functions and constants.
# - datetime: Provides classes for working with dates and times.
# - random: Provides functions for generating random numbers.
# - json: Provides functions for working with JSON data.
# - urllib: Provides functions for working with URLs.
# - re: Provides regular expression matching operations.
# - collections: Provides additional data structures like deque, defaultdict, etc.

# Example usage of the datetime module:
import datetime

# Get the current date and time
current_datetime = datetime.datetime.now()
print(f"Unformatted current date and time: {current_datetime}")

# Format the date and time as a string
formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
print(f"Formatted current date and time: {formatted_datetime}")

# Example usage of the random module:
import random

# Generate a random integer between 1 and 100
random_number = random.randint(1, 100)
print(f"This time the random number is: {random_number}")

# Example usage of the collections module:
from collections import defaultdict

# Create a dictionary with a default value of 0
counter = defaultdict(int)
counter["apple"] += 1
counter["banana"] += 1
print(counter)
print(counter.keys())
print(counter.values())