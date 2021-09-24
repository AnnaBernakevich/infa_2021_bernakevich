from random import *
import turtle

turtle.shape('turtle')
for i in range(100):
    a = randint(1, 10)
    alpha = randint(0, 360)
    turtle.forward(10*a)
    turtle.right(alpha)