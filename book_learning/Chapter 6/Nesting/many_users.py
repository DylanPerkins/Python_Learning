# Section: A Dictionary in a Dictionary


# Define a dic. with a dic. as the key's value.
users = {
    'aeinstien': {
        'first': 'albert',
        'last': 'einstien',
        'location': 'princeton'
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris'
    }
}

for username, user_info in users.items(): # Splits dic.1's keys as the username, values as user_info
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}" # Assigns keys from user_info dic to callable values
    location = user_info['location'] # Same as fullname

    # Prints all
    print(f"\tFull name: {full_name.title()}") 
    print(f"\tLocation: {location.title()}")
