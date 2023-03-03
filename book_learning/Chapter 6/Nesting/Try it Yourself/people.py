# Try it Yourself | 6-7


# Dictionary 1
person_0 = {
    'first_name': 'Dylan',
    'last_name': 'Perkins',
    'age': 23,
    'city': 'Worcester'
}

# Dictionary 2
person_1 = {
    'first_name': 'John',
    'last_name': 'Webber',
    'age': 17,
    'city': 'Boston'
}

# Dictionary 3
person_2 = {
    'first_name': 'Mike',
    'last_name': 'Joins',
    'age': 46,
    'city': 'Denver'
}

# Add each dictionary to a list. Add `counter` variable for spacing
peoples = [person_0, person_1, person_2]
counter = 0

# Sets each dictionary as the variable peeople
# Then, sets the keys as `user_info` and their values as `answer`
# Uses a counter to add a newline space between each user's set of info
for people in peoples:
    for user_info, answer in people.items():
        print(f"{user_info.title()}: {answer}")
        counter = counter + 1
    if (counter == 4):
        counter = 0
        print("")
        