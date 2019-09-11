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

import turtle


def drawbox(wn, darko):
    """
    Docstring for drawbox
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


    # ...


def function_2(wn, darko):
    """
    Docstring for function_2
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
    # ...


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

