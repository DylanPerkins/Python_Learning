
# Create a GameObject Class

# Add fields and an inilializer
# Implement a method

# Self:
# - Self is a reference to the current instance of the class
# - Self is used to access variables that belongs to the class
# - Self is used to access methods that belongs to the class

class GameObject:
    # Fields, this declaration is not necessary
    name = ""
    appearance = ""
    feel = ""
    smell = ""

    # Initializer
    def __init__(self, name, appearance, feel, smell):
        self.name = name
        self.appearance = appearance
        self.feel = feel
        self.smell = smell

    # Methods
    def look(self):
        return f"You look at the {self.name} and see {self.appearance}.\n"


    def touch(self):
        return f"You touch the {self.name} and feel {self.feel}.\n"


    def smell(self):
        return f"You smell the {self.name} and smell {self.smell}.\n"
    
game_object = GameObject("rock", "a rock", "rough", "dusty")