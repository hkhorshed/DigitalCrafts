from turtle import *


def eqilateral_triangle():
    begin_fill()
    color("Blue")
    for i in range(3):
        forward(100)
        left(120)
    end_fill()

def square():
    for i in range(4):
        color("Blue")
        forward(100)
        right(90)

def pentagon():
    begin_fill()
    color("Red")
    for i in range(5):
        begin_fill()
        color("Yello")
        left(72)
        forward(100)
    end_fill()

def hexagon():
    for i in range(6):
        pensize(3)
        left(60)
        forward(100)

# Octagon

def octagon():
    for i in range(8):
        pensize(6)
        left(45)
        forward(100)

# Star

def star():
    for i in range(5):
        color("Orange")
        right(144)
        forward(100)
        left(72)
        forward(100)

def circle():
    begin_fill()
    color("Green")
    circle(75)
    end_fill()
    mainloop()