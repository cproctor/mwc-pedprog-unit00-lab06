from turtle import *

def prepare_to_draw(x, y):
    "Moves the turtle to (x, y) without drawing and prepares to draw."
    penup()
    goto(x, y)
    pendown()
    speed(0)
    setheading(0)

def grid_of_squares(side_length, margin, rows, columns):
    """Draws a (columns * rows) grid of squares.
    Each square has size `side_length`, with `margin` between squares.
    """
    # YOUR CODE HERE

#Keeps the drawing window open until key press  
input("Press return to end drawing...")
