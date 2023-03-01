# Try it Yourself | 5-9

usernames = []

if usernames:
    for username in usernames:
        if username == 'admin':
            print(f"Hello {username}, do you want to view a status report?")
        
        else: print(f"Hello {username}, thank you for logging in!")

else:
    print("We need to find some users!")

# Tested with usernames = [], works as intended
#
# Tested with usernames = ['john123', 'brad675', 'mike102', 
# 'leo829', 'ted475', 'admin'], also works as intended