# Section: Moving Items from One List to Another

# Start with users that need to be verified,
# and an empty list to hold verified users.

unverified_users = ['alice', 'brian', 'candace']
verified_users = []

# Verify each user until there are no more unverified users.
# Move each verified user into the list of verified users.

while unverified_users: # Will run as long as unverified_users is not empty
    current_user = unverified_users.pop()

    print(f"Verifying user: {current_user.title()}")
    verified_users.append(current_user)

# Display all verified users.
print("\nThe following users have been verified:")
for verified_user in verified_users:
    print(verified_user.title())