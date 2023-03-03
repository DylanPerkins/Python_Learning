peoples = {

    'person_0': {
        'first_name': 'Dylan',
        'last_name': 'Perkins',
        'age': 23,
        'city': 'Worcester'
    },

    'person_1': {
        'first_name': 'John',
        'last_name': 'Webber',
        'age': 17,
        'city': 'Boston'
    },

    'person_2': {
        'first_name': 'Mike',
        'last_name': 'Joins',
        'age': 46,
        'city': 'Denver'
    }
}

for person, info in peoples.items():
    print(f"\n{person}:")
    full_name = f"{info['first_name']} {info['last_name']}"
    age = f"{info['age']}"
    cityLiving = f"{info['city']}"

    print(f"Full name - {full_name.title()}")
    print(f"They are {age} years old")
    print(f"They currently live in {cityLiving}")
