from turtle import *

# This program will make any shape, just change the `sides` variable

sides = 5           # Change me for new shape!
angle = 360/sides

def move_and_turn (angle):
    forward(50)
    right(angle)

for i in range(sides):
    move_and_turn(angle)

done()

# Did this all on my own :D