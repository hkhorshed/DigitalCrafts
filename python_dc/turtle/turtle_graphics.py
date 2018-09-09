# Lecture Example 1

from turtle import *

forward(100)
right(90)
forward(100)
right(90)
forward(100)
right(90)
forward(100)
mainloop()

# Lecture Example 2

from turtle import *

up()
forward(50)
left(90)
forward(50)
left(90)
down()

forward(100)
left(90)
forward(100)
left(90)
forward(100)
left(90)
forward(100)
mainloop()

# Lecture Example 3 - Circle

from turtle import *
pencolor('orange')
width(10)
circle(180)

# Lecture Example 4 - Star Drawing

from turtle import *
for i in range(5):
    forward(100)
    right(144)
mainloop()