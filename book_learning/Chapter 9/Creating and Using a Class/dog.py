class Dog:
    """A simple attempt to model a dog"""

    def __init__(self, name, age):
        """Initialize name and age attributes"""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command"""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command"""
        print(f"{self.name} rolled over!")


### Notes
# The __init__ method is a special method that runs automatically when we create a
# new Dog class instance

# The self parameter references the instance itself

# When we want to create a new Dog instance, all we need to do is pass name and age.

# Variables like name and age are called attributes, and are attached to the new
# instance that was created. These variables can be accessed throughout the instance.

# Newly created Dog instances will have access to the `sit` and `roll_over`
# methods by default as well


### Section: Making an Instance from a Class

my_dog = Dog("Willie", 6)

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")

my_dog.sit()
my_dog.roll_over()

your_dog = Dog("Lucy", 3)

print(f"\nYour dog's name is {your_dog.name}.")
print(f"Your dog is {your_dog.age} years old.")

### Notes

# A class is basically a set of instructions for how to make an instance.

# To access the attributes of an instance or to use functions from the parent
# class, we use dot notation.

# We can create several instances within the same file and access them at
# the same time without Python getting confused. Even if we had used the same 
# name or age as another instance.
