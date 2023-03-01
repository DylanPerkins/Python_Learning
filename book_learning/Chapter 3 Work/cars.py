# Organizing a list.


# Sorting a List Permanently with the sort() Method
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)
# Sorts the list alphabetically 

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)
print(cars)
# Sorts the list in reverse alphabetical order



cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

print("\nHere is the original list again:")
print(cars)
# Printing a sorted list without changing the actual list in any way with the sorted() Function



cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)

cars.reverse()
print(cars)
# Prints the list in reverse order, does not do any type of sorting



cars = ['bmw', 'audi', 'toyota', 'subaru']
print(len(cars))
# Finds the length of a list with the len() function and then prints it