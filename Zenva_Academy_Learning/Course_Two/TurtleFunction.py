from turtle import *

# Function needs to be defined before it can be called

def move_and_turn (distance, angle):
    forward(distance)
    right(angle)

move_and_turn(100, 45)
move_and_turn(50, 90)

done()