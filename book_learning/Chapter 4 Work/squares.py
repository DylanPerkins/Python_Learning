squares = []
for value in range(1,11):
	square = value ** 2
	squares.append(square)

print(squares)
# Created a placeholder list, then made a range from 1-10 and squared each, then put each loop value into the list, then printed the raw list.

squares = []
for value in range(1,11):
	squares.append(value**2)

print(squares)
# Alternate way to write the same function, uses less lines

squares = [value**2 for value in range(1, 11)]
print(squares)
# Use of a 'list comprehension' to do both of the previous tasks, but in 1 line