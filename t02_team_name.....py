######################################################################
# Author: Zy'Shavia Garrett & Shawn Villahermosa
# Usernames: garrettz & villahermosas
#
# Assignment: T02: Exploring Turtles in Python
# Purpose: Introduces the use of the turtles library
#
######################################################################

import turtle

wn = turtle.Screen()          # Sets up the window
wn.bgcolor("black")      # Color of background
wn.title("Shavia & Shawn")    # Window title

shavia = turtle.Turtle()      # Names the turtle
shavia.color("green")         # Colors the turtle
shavia.pensize(5)             # How big the pen size is
shavia.shape("turtle")

shawn = turtle.Turtle()
shawn.color("Blue")
shawn.pensize(5)
shawn.shape("turtle")

fish = turtle.Turtle()
fish.color("Red")
fish.shape("circle")

head = 0
shavia.setheading(head)

# Start of pen for Shavia
shavia.penup()
shavia.backward(100)
shavia.left(90)
shavia.forward(100)
shavia.left(90)
shavia.forward(30)

# Initial for Shavia
shavia.pendown()
shavia.backward(70)
shavia.right(120)
shavia.backward(120)
shavia.right(60)
shavia.forward(70)

# Start of pen for Shawn
shawn.penup()
shawn.left(90)
shawn.forward(110)
shawn.right(90)
shawn.forward(70)

# Initial for Shawn
shawn.pendown()
shawn.backward(70)
shawn.right(90)
shawn.forward(50)
shawn.left(90)
shawn.forward(70)
shawn.right(90)
shawn.forward(50)
shawn.right(90)
shawn.forward(70)

# Circle stamp
fish.penup()
size = 5
for i in range(100):
    fish.stamp()
    size = size + 3
    fish.forward(size)
    fish.left(30)

# Hello

wn.exitonclick()