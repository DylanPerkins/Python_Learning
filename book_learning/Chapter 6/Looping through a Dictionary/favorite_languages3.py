# Looping Through All the Keys in a Dictionary

favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'ruby',
 'phil': 'python',
 }

for name in favorite_languages.keys(): # .keys Tells to only grab the keys
    print(name.title())

# Looping through the keys is actually the default behavior when looping
# through a dictionary. So for name in favorite_languages: is the same as 
# for name in favorite_languages.keys():

# The keys() method isn't just for looping: it actually returns a list of all
# the keys

# I will likely always call .keys() just to make the code easier to read

friends = ['phil', 'sarah']
for name in favorite_languages.keys(): 
    print(f"Hi {name.title()}!") # Says hi to all keys in favorite_languages dictionary

    if name in friends: # if name exists both in the list friends and the dictionary
        language = favorite_languages[name].title() #set the variable language to the key's value
        print(f"\t{name.title()}, I see you love {language}!") # \t is a tab or an indent


# You can use `not in` through dictionaries too!

if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")