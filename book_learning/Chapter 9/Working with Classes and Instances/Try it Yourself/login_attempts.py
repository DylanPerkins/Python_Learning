### Try it Yourself: 9-5

### Task: Add an attribute called login_attempts to your User class from
# Exercise 9-3 (page 162). Write a method called increment_login_attempts() that
# increments the value of login_attempts by 1. Write another method called
# reset_login_attempts() that resets the value of login_attempts to 0. Make an
# instance of the User class and call increment_login_attempts() several times.
# Print the value of login_attempts to make sure it was incremented properly,
# and then call reset_login_attempts(). Print login_attempts again to make
# sure it was reset to 0.


class Users:

    def __init__(self, first_name, last_name, country, job) -> str:
        self.first_name = first_name
        self.last_name = last_name
        self.country = country
        self.job = job
        self.login_attempts = 0

    def describe_user(self):
        """Formatted user description"""
        print(
            f"This user's name is {self.first_name} {self.last_name}. "
            + f"They reside in {self.country} and they work as a {self.job}"
        )

    def greet_user(self):
        """Formatted user greeting"""
        print(f"Hello {self.first_name} {self.last_name}! How are you?")

    def increment_login_attempts(self):
        """Increment the login attempts by one"""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Resets the login attempts for a user to zero"""
        self.login_attempts = 0


user_one = Users("George", "Barkley", "USA", "Scientist")

# Prints default amount (0)
print(user_one.login_attempts)

# Simulates login attempts, incrementing by 1
user_one.increment_login_attempts()
user_one.increment_login_attempts()
user_one.increment_login_attempts()
user_one.increment_login_attempts()
user_one.increment_login_attempts()
print(user_one.login_attempts)

# Resets login attempts
user_one.reset_login_attempts()
print(user_one.login_attempts)
