# Final Project: Turtle Mini-Game

from turtle import *

# Create a turtle that can move in 4 directions
# Have an end goal for the turtle to reach
# Have visual feedback for the turtle when it reaches the end goal

move_distance = 35     # Sets the distance the turtle moves each time a key is pressed

bgcolor("#D2691E")
speed(0)


# Create the ocean
penup()
color("blue")
begin_fill()
goto(300, 450)
goto(600, 450)
goto(600, -450)
goto(300, -450)
goto(300, 450)
end_fill()


# Create the turtle
penup()
goto(-250, 0)
color("darkgreen")
shape("turtle")

def move_up():
    setheading(90)     # Sets the turtle's heading to 90 degrees (up)
    forward(move_distance)
    check_goal()

def move_down():
    setheading(270)     # Sets the turtle's heading to 270 degrees (down)
    forward(move_distance)
    check_goal()

def move_left():
    setheading(180)     # Sets the turtle's heading to 180 degrees (left)
    forward(move_distance)
    check_goal()

def move_right():
    setheading(0)       # Sets the turtle's heading to 0 degrees (right)
    forward(move_distance)
    check_goal()


# Create the goal
def check_goal():
    if xcor() > 300:
        hideturtle()
        color("white")
        write("You Win!")

        onkey(None, "Up")
        onkey(None, "Down")
        onkey(None, "Left")
        onkey(None, "Right")


# Setup the key listeners
listen()
onkey(move_up, "Up")
onkey(move_down, "Down")
onkey(move_left, "Left")
onkey(move_right, "Right")


done()
