# Try it Yourself | 5-10

current_users = ['john123', 'brad675', 'mike102', 'leo829', 'ted475']

new_users = ['jeff017', 'mike102', 'javier439', 'brad675', 'molly812']

for users in new_users:
    if users in current_users:
        print(f"{users} is taken, try another!")
    else:
        print(f"{users} is available!")