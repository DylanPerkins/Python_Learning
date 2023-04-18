# Section: Using Arbitrary Keyword Arguments

# Sometimes you’ll want to accept an arbitrary number of arguments, but you
# won’t know ahead of time what kind of information will be passed.

# So, you can write functions that accept as many key-value pairs as the
# calling statement provides.

def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

# This function expects a first and last name, and then it allows the user to
# pass in as many name-value pairs as they want.
# The double asterisks before the parameter **user_info cause Python to create
# an empty dictionary called user_info and pack whatever name-value pairs it
# receives into this dictionary.

user_profile = build_profile('albert', 'einstein',
                            location='princeton',
                            field='physics')
print(user_profile)