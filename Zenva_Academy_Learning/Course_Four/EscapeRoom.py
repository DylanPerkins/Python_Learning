
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

class Room:
    # Fields
    escape_code = 0
    game_objects = []

    # Initializer
    def __init__(self, escape_code, game_objects):
        self.escape_code = escape_code
        self.game_objects = game_objects

    # Returns whether the entered code equals the escape code
    def check_code(self, code):
        return code == self.escape_code
    
    # Returns a list of the names of the game objects in the room
    def get_game_object_names(self):
        names = []
        for game_object in self.game_objects:
            names.append(game_object.name)
        return names
    
class Game:
    # Initializer
    def __init__(self):
        self.attempts = 0
        objects = self.create_object()
        self.rooms = Room(123, objects)

    def create_object(self):
        return [
            GameObject(
            "Sweater",
            "A blue sweater with the number 12 on it.",
            "Soft and warm.",
            "Like a fresh spring day." 
            ),
            GameObject(
            "Chair",
            "A wooden chair with a soft cushion.",
            "Hard and sturdy.",
            "Smells of old, worn wood."
            ),
            GameObject(
            "Journal",
            "A leather bound journal with a pen.",
            "Smooth and cool.",
            "Smells of fresh ink."
            ),
            GameObject(
            "Bowl of Soup",
            "A bowl of hot soup.",
            "Warm and wet.",
            "Smells of chicken and vegetables."
            ),
            GameObject(
            "Clock",
            "A grandfather clock.",
            "Hard and smooth.",
            "Smells of old wood and metal."
            )
        ]
    

    