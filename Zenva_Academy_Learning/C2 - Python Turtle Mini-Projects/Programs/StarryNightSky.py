from turtle import *
from random import *

bgcolor("black")        # Sets Background color to black
hideturtle()            # Hides little arrow head
speed(0)                # Sets spped of pen to instant

height = round(window_height() / 2)         # Grabs screen height, and rounds to prevent divison errors with randrange
width = round(window_width() / 2)           # Grabs screen width, and rounds to prevent divison errors with randrange

stars = 0

while stars <= 100:                         # Runs while stars is less than 100
    diameter = randrange(3, 20)             # Generates random diameter
    penup()                                 # Lifts Pen, cannot draw
    setx(randrange(-width, width))          # Sets x position using a random number within the windows width
    sety(randrange(-height, height))        # Sets y position using a random number within the windows height
    pendown()                               # Drops Pen, can draw
    color("yellow")                         # Makes a yellow halo around the star
    dot(diameter + 1)
    color("white")                          # Makes the star!
    dot(diameter)
    stars += 1                              # + 1 on star counter

done()
