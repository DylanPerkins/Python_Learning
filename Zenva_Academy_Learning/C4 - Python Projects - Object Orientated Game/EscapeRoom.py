# Self:
# - Self is a reference to the current instance of the class
# - Self is used to access variables that belongs to the class
# - Self is used to access methods that belongs to the class


class GameObject:
    # Initializer
    def __init__(self, name, appearance, feel, scent):
        self.name = name
        self.appearance = appearance
        self.feel = feel
        self.scent = scent

    # Methods
    def look(self):
        return f"You look at the {self.name} and you see that it's {self.appearance}.\n"

    def touch(self):
        return f"You touch the {self.name} and it feels {self.feel}.\n"

    def smell(self):
        return f"You smell the {self.name} and it {self.scent}.\n"


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
        for object in self.game_objects:
            names.append(object.name)

        return names


class Game:
    # Initializer
    def __init__(self):
        self.attempts = 0
        objects = self.create_objects()
        self.room = Room(123, objects)

    def create_objects(self):
        return [
            GameObject(
                "Sweater",
                "a blue sweater with the number 12 on it",
                "soft and warm",
                "like a fresh spring day",
            ),
            GameObject(
                "Chair",
                "a wooden chair with a soft cushion",
                "hard and sturdy",
                "smells of old, worn wood",
            ),
            GameObject(
                "Journal",
                "a leather bound journal with a pen",
                "smooth and cool",
                "smells of fresh ink",
            ),
            GameObject(
                "Bowl of Soup",
                "a bowl of hot soup",
                "warm and wet",
                "smells of chicken and vegetables",
            ),
            GameObject(
                "Clock",
                "a grandfather clock",
                "hard and smooth",
                "smells of old wood and metal",
            ),
        ]

    def take_turn(self):
        prompt = self.get_room_prompt()
        selection = int(input(prompt))

        if selection >= 1 and selection <= 5:
            self.select_object(selection - 1)
            self.take_turn()
        elif selection >= 100 and selection <= 999:
            is_code_correct = self.guess_code(selection)

            if is_code_correct:
                print(
                    f"It took you {self.attempts} attempts to escape. Congratulations!"
                )
            else:
                if self.attempts == 3:
                    print("You ran out of attempts. Game Over.")
                else:
                    print("Incorrect code. Try again.")
                    self.take_turn()
        else:
            print("Invalid selection. Please try again.\n")
            self.take_turn()

    def get_room_prompt(self):
        prompt = "Enter a 3 Digit Code, or choose an object to interact with:\n"
        names = self.room.get_game_object_names()
        index = 1

        for name in names:
            prompt += f"{index}. {name}\n"
            index += 1

        return prompt

    def select_object(self, index):
        selected_object = self.room.game_objects[index]
        prompt = self.get_object_interaction_string(selected_object.name)
        interaction = int(input(prompt))
        clue = self.interact_with_object(selected_object, interaction)
        print(clue)

    def get_object_interaction_string(self, name):
        return f"How do you want to interact with the {name}?\n1. Look\n2. Touch\n3. Smell\n"

    def interact_with_object(self, object, interaction: int):
        if interaction == 1:
            return object.look()
        elif interaction == 2:
            return object.touch()
        elif interaction == 3:
            return object.smell()
        else:
            return "Invalid interaction."

    def guess_code(self, code: int):
        if self.room.check_code(code):
            return True
        else:
            self.attempts += 1
            return False


game = Game()
game.take_turn()
