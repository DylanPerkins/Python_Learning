### Try it Yourself: 9-7

### Task:
# An administrator is a special kind of user. Write a class called
# Admin that inherits from the User class you wrote in Exercise 9-3 (page 162)
# or Exercise 9-5 (page 167). Add an attribute, privileges, that stores a list
# of strings like "can add post", "can delete post", "can ban user", and so on.
# Write a method called show_privileges() that lists the administrator's set of
# privileges. Create an instance of Admin, and call your method.


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


class Admin(Users):

    def __init__(self, first_name, last_name, country, job) -> str:
        super().__init__(first_name, last_name, country, job)
        self.privileges = [
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
        for privilege in self.privileges:
            print(f"\t- {privilege}")

admin_user = Admin("Dylan", "Classified", "USA", "Software Developer")
admin_user.show_privileges()
