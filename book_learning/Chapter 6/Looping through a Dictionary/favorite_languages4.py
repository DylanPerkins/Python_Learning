# Looping Through a Dictionary's Keys in a Particular Order

# You can sort the dictionary as they're returned in the for loop
# We can use the sorted() function to get a copy of the keys in order

favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'ruby',
 'phil': 'python',
 }

for name in sorted(favorite_languages.keys()): # Sorts keys alphabetically
    print(f"{name.title()}, thank you for taking the poll.")