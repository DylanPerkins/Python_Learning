# Try it Yourself | 6-6

favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'ruby',
 'phil': 'python',
 }

people = ['jen', 'mike', 'leo', 'ben']

for person in people:
    if person in favorite_languages.keys():
        print(f"Thank you, {person.title()}, for responding!")
    else:
        print(f"{person.title()}, can you please take the poll?")

# 1. We define a dictionary `favorite_languages` which contains the names of people and 
# their favorite programming languages.
# 2. We define a list `people` which contains the names of people we want to loop through.
# 3. We use a `for` loop to loop through `people` list.
# 4. For each person in the list, we check if they have responded by using the `if` condition 
# and checking if their name is in the `favorite_languages` dictionary.
# 5. If they have responded, we print a message thanking them for responding.
# 6. If they have not responded yet, we print a message inviting them to take the poll.