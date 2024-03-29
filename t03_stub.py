#################################################################################
# Author: Mason Richardson, Jeremy Campbell
# Username: richardsonmas, campbellj
#
# Assignment: T03
# Purpose: This program fills a square without leaving any gaps.
#################################################################################
# Acknowledgements:
#
#
#################################################################################
# Designating which library to open.
import turtle


def drawbox(wn, darko):
    """
    This function is drawing the white box in the turtle screen.
    """
    darko.penup()
    darko.setpos(-263,263)
    darko.pendown()
    darko.forward(526)
    darko.right(90)
    darko.forward(526)
    darko.right(90)
    darko.forward(526)
    darko.right(90)
    darko.forward(526)


# White box with an orange screen has been constructed.


def function_2(wn, darko):
    """
    This function is telling the turtle which path to stamp.
    """
    darko.penup()
    darko.setpos(-237,237)
    darko.pendown()
    darko.right(180)
    darko.forward(474)
    darko.right(-90)
    darko.forward(26)
    darko.right(-90)
    for i in range(9):
        darko.forward(474)
        darko.right(90)
        darko.forward(26)
        darko.right(90)
        darko.forward(474)
        darko.right(-90)
        darko.forward(26)
        darko.right(-90)
    # ...finished


def main():
    """
    The "top" function of this program; the one that calls all other functions.
    """
    # ...
    wn = turtle.Screen()
    darko = turtle.Turtle()
    darko.pensize(26)
    wn.title = "Boustrophedonnie Darko"
    wn.bgcolor("orange")
    darko.color("white")

    drawbox(wn, darko)            # Function call to function_1
    function_2(wn, darko)            # Function call to function_2
    wn.exitonclick()

main()

