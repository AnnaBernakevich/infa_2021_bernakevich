from random import randint
import turtle

turtles = []
n = 10
dt = 1
d_min = 1
steps_of_time_number = 100

def create():
    t = turtle.Turtle()
    t.turtlesize(2)
    t.shape('circle')
    t.penup()
    t_new = {
        'm': 10,
        'r': 10,
        'p': {'x': randint(-200, 200),
              'y': randint(-200, 200)},
        'v': {'x': randint(0, 10),
              'y': randint(0, 10)},
        't': t
    }
    return t_new

for i in range(n):
    turtles.append(create())


for i in range(steps_of_time_number):
    for turtle1 in turtles:
        for turtle2 in turtles:
            if turtle2 != turtle1:
                dx = abs(turtle1['p']['x'] - turtle2['p']['x'])
                dy = abs(turtle1['p']['y'] - turtle2['p']['y'])
                if dx <= d_min or dy <= d_min:
                    turtle1['v']['x'] *= - 1
                    turtle1['v']['y'] *= - 1
    for turtle in turtles:
        if abs(turtle['p']['x']) >= 200:
            turtle['v']['x'] *= - 1
        if abs(turtle['p']['y']) >= 200:
            turtle['v']['y'] *= - 1
        turtle['p']['x'] += turtle['v']['x'] * dt
        turtle['p']['y'] += turtle['v']['y'] * dt
        turtle['t'].goto(turtle['p']['x'], turtle['p']['y'])

