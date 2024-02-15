### Try it Yourself: 9-13

### Task:
# Make a class Die with one attribute called sides, which has a default
# value of 6. Write a method called roll_die() that prints a random number
# between 1 and the number of sides the die has. Make a 6-sided die and roll it
# 10 times.
# Make a 10-sided die and a 20-sided die. Roll each die 10 times.

import random


class Die:

    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        chosen_side = random.randint(1, self.sides)

        print(chosen_side)


# Create a new Die instance with 6 sides, and call the roll_die method 10 times
six_sided_die = Die(6)

print("I will now roll my 6 Sided Die 10 times!")
for i in range(0, 10):
    six_sided_die.roll_die()

# Create a new Die instance with 10 sides, and call the roll_die method 10 times
ten_sided_die = Die(10)

print("\nI will now roll my 10 Sided Die 10 times!")
for i in range(0, 10):
    ten_sided_die.roll_die()

# Create a new Die instance with 20 sides, and call the roll_die method 10 times
twenty_sided_die = Die(20)

print("\nI will now roll my 20 Sided Die 10 times!")
for i in range(0, 10):
    twenty_sided_die.roll_die()
