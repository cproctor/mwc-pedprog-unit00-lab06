from turtle import *

def prepare_to_draw(x, y):
    "Moves the turtle to (x, y) without drawing and prepares to draw."
    penup()
    goto(x, y)
    pendown()
    speed(0)
    setheading(0)

def draw_cone():
    "Draws an ice cream cone."
    # YOUR CODE GOES HERE

def draw_ice_cream_scoop():
    "Draws one scoop of ice cream."
    # YOUR CODE GOES HERE

def draw_ice_cream_cone(num_scoops):
    "Draws an ice cream cone with scoops on top."
    # YOUR CODE GOES HERE

# Once you finish testing, replace the next line with the commented-out 
# line below, allowing the player to choose how many scoops they want.
choice = 3
# choice = int(input("How many scoops of ice cream would you like?"))
draw_ice_cream_cone(choice)
input("Press return...")
