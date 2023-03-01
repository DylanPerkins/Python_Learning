dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])
# Making a Tuple. Items inside the tuple cannot be changed, if tried then program will throw an error. Parentheses are not required either, while the comma is.
 

dimensions = (200, 50)
for dimension in dimensions:
    print(dimension)
# Looping works the same in a tuple as a normal list


dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)
# Editing of a tuple is not possible, but rewriting the value of the variable for the tuple is possible.
