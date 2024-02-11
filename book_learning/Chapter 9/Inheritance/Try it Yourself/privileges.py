### Try it Yourself: 9-8

### Task:
# Write a separate Privileges class. The class should have one
# attribute, privileges, that stores a list of strings as described in Exercise 9-7.
# Move the show_privileges() method to this class. Make a Privileges instance
# as an attribute in the Admin class. Create a new instance of Admin and use your
# method to show its privileges.


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


class Privileges:

    def __init__(self):
        self.user_privileges = [
            "can add post",
            "can create thread",
            "can mute user",
            "can ban user",
            "can delete post",
            "can delete thread",
        ]

    def show_privileges(self):
        """Show the privileges a user can have"""
        print("This user can do the following:")
        for privilege in self.user_privileges:
            print(f"\t- {privilege}")


class Admin(Users):

    def __init__(self, first_name, last_name, country, job) -> str:
        super().__init__(first_name, last_name, country, job)
        self.user_privileges = Privileges()

admin_user = Admin("Dylan", "Classified", "USA", "Software Developer")
admin_user.user_privileges.show_privileges()