# Number 1 - Hello
def hello(n):
    return "Hello " + str(n)

print('1) Using a function named hello to print a name: ' )
print(hello('Hussein'))

# Number 2 - y = x + 1
import matplotlib.pyplot as plot
def f(x):
    return x + 1

xs_2 = list(range(-5 , 6))
ys_2 = []

for x in xs_2:
    ys_2.append(f(x))

plot.plot(xs_2 , ys_2)
plot.show()

# Number 3 - Square of x
def g(x):
    return x ** 2

xs_3 = list(range(-100 , 101))
ys_3 = []

for x in xs_3:
    ys_3.append(g(x))

plot.plot(xs_3 , ys_3)
plot.show()

# Number 4 - Odd or Even
import matplotlib.pyplot as plot
def p(x):
    if x % 2 == 0:
        return -1
    else:
        return 1
    

xs_4 = list(range(-5 , 6))
ys_4 = []

for x in xs_4:
    ys_4.append(p(x))


plot.bar(xs_4 , ys_4)
plot.show()

# Number 5 - Sin
import matplotlib.pyplot as plot
import math
from math import sin

def q(x):
    return sin(x)

xs_5  = list(range(-5 , 6))
ys_5 = []

for x in xs_5:
    ys_5.append(q(x))

plot.plot(xs_5 , ys_5)
plot.show()

# Number 6 - sin 2
import matplotlib.pyplot as plot
import math
from math import sin
from numpy import arange

def q(x):
    return sin(x)

xs_5  = arange(-5 , 6 , 0.1)
ys_5 = []

for x in xs_5:
    ys_5.append(q(x))

plot.plot(xs_5 , ys_5)
plot.show()

## Number 7 - F to C
import matplotlib.pyplot as plot
import math
from numpy import arange

def t(x):
    return (1.8 * x) + 32

celsius_7 = arange(-32 , 212 , 1)
farenheit_7 = []

for x in celsius_7:
    farenheit_7.append(t(x))

plot.plot(celsius_7 , farenheit_7)
plot.show()

## Number 8
def playAgain():
    x = input("Do you want to play again? ")
    if x == "y".lower():
        return True
    else:
        return False
    
print(playAgain())