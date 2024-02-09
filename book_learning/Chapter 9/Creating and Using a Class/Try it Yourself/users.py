### Try it Yourself: 9-3

# Task: Make a class called User. Create two attributes called first_name and
# last_name, and then create several other attributes that are typically stored
# in a user profile. Make a method called describe_user() that prints a summary
# of the user's information. Make another method called greet_user() that prints
# a personalized greeting to the user.Create several instances representing
# different users, and call both methods for each user.


class Users:

    def __init__(self, first_name, last_name, country, job) -> str:
        self.first_name = first_name
        self.last_name = last_name
        self.country = country
        self.job = job

    def describe_user(self):
        print(
            f"This user's name is {self.first_name} {self.last_name}. "
            + f"They reside in {self.country} and they work as a {self.job}"
        )

    def greet_user(self):
        print(f"Hello {self.first_name} {self.last_name}! How are you?")


user_one = Users("George", "Barkly", "USA", "Scientist")
user_two = Users("Mark", "Waters", "Mexico", "Doctor")
user_three = Users("Jeff", "Fox", "Canada", "Janitor")
user_four = Users("Sarah", "Walters", "France", "Pilot")

user_one.describe_user()
user_two.describe_user()
user_three.describe_user()
user_four.describe_user()

print("\n")

user_one.greet_user()
user_two.greet_user()
user_three.greet_user()
user_four.greet_user()
