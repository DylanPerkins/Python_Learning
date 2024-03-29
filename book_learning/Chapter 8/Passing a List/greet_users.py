# Section: Passing a List intro

# When you pass a list to a function, the function gets direct access to the
# contents of the list.


def greet_users(names):
    """Print a simple greeting to each user in the list"""
    for name in names:
        msg = f"Hello, {name.title()}"
        print(msg)


usernames = ["dylan", "heidi", "luna", "luca"]
greet_users(usernames)
