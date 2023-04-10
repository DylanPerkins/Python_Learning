# Section's Returning a Simple Value, and Making an Arguement Optional

def get_formatted_name(first_name, last_name, middle_name=''):
    """Return a full name, neatly formatted."""
    # Python interprets an empty string as False, and a non-empty String as True
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else: 
        full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)
# Output: Jimi Hendrix

# Middle name needs to be in the last slot
musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)
# Output: John Lee Hooker