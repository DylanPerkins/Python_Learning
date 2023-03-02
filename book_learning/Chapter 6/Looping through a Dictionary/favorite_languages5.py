# Looping Through All Values in a Dictionary

# If you are primarily interested in the values that a dictionary contains,
# you can use the values() method to return a list of values without any keys. 

favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'ruby',
 'phil': 'python',
 }

# This method doesn't check for repeats!
print("The following languages have been mentioned so far!")
for language in favorite_languages.values():
    print(language.title())

# This method does check for repeats!
print("The following languages have been mentioned so far!")
for language in set(favorite_languages.values()):
    print(language.title())

# When you wrap set() around a list that contains duplicate items, Python
# identifies the unique items in the list and builds a set from those items