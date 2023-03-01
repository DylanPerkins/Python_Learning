# Try it Yourself | 5-8

usernames = ['john123', 'brad675', 'mike102', 'leo829', 'ted475', 'admin']

for username in usernames:
    if username == 'admin':
        print("Hello admin, would you like to see a status report?")
    else:
        print(f"Hello {username}, thank you for logging in!")
