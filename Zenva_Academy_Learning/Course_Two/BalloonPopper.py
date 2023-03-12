# Project One!

from turtle import *

bgcolor("white")

diameter = 50       # Balloon's diameter
pop_diameter = 100


def draw_balloon():
    color("red")
    dot(diameter)  # Draws a filled "dot" at the turtle location using x px as a diameter


# Variables can exist soley within the scope of a function.
# Need to explicitly say that we are using an outside variable,
# or python will think we are making a new one
def inflate_balloon():
    global diameter
    diameter += 15
    draw_balloon()

    if diameter >= pop_diameter:
        clear()
        diameter = 40
        write("POP!")


draw_balloon()

onkey(inflate_balloon, "space")
listen()

done()
