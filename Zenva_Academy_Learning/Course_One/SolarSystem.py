# Course's "Final Project"

from turtle import *

# 0 is instant, 1 is the slowest, 10 is the fastest 
speed(0)

bgcolor("black")

penup()
backward(150)
pendown()

# Orange Planet
color("orange")
begin_fill()
circle(60)
end_fill()

# Move Forward, no draw
penup()
forward(100)
pendown()

# Gray Planet
color("gray")
begin_fill()
circle(20)
end_fill()

# Move Forward, no draw
penup()
forward(80)
pendown()

# Red Planet
color("red")
begin_fill()
circle(40)
end_fill()

# Move Forward, no draw
penup()
forward(90)
pendown()

# Green Planet
color("green")
begin_fill()
circle(30)
end_fill()

done()