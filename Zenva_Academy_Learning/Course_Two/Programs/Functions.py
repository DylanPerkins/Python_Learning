# Define the name of a function, and it's parameters
# A function does not require any parameters, info inside ()
def say_hello (name):
    print(f"How are you, {name}?")


# Will run the called function with the given input
say_hello("Bob")

# Use print when you want to show a value to a human. return is a keyword. 
# When a return statement is reached, Python will stop the execution of the 
# current function, sending a value out to where the function was called. 
# Use return when you want to send a value from one point in your 
# code to another.

def add_numbers (a, b):
    _sum = a + b
    return _sum

num = add_numbers(150, 2063)