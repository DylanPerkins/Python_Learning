# Section: A List in a Dictionary

favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell']
}


# Print out a person's fav language!
for name, languages in favorite_languages.items():
    if len(languages) == 1: # If key's list value is 1, run this
        print(f"\n{name.title()}'s favorite language is:")
        for language in languages:
            print(f"\t{language.title()}")
    else: # if longer than 1, run this
        print(f"\n{name.title()}'s favorite language(s) are:")
        for language in languages:
            print(f"\t{language.title()}")