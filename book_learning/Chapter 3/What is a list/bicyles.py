# Putting items into a list
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
# Prints EXACTLY what is in the list, including the brackets.

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[0])
# Prints only the first item in the list
# Python considers the first item in a list to be at position 0, not position 1. 

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[0].title())
# Prints first item in list in title formatting

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[1])
print(bicycles[3])
# Prints the second and fourth item from the list

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[-1])
# Prints the LAST item in a list, -2 will return the second to last, -3 the third from last, etc.

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
message = f"My first bicylce was a {bicycles[0].title()}."
print(message)
# Prints a message using an f string with an indexed value from a list