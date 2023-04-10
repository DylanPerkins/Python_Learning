# Section: Returning a Dictionary

def build_person(first_name, last_name, age=None):
    """Return a Dictionary of info about a person"""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

musician = build_person('jimi', 'hendrix', 27)
print(musician)
# Output {'first': 'jimi', 'last': 'hendrix', 'age': 27}