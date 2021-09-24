import turtle
turtle.shape('turtle')

numbers = [
    (0, 1, 1, 0, 1, 0, 1, 1, 1),
    (0, 0, 0, 1, 1, 0, 1, 0, 0),
    (1, 0, 1, 0, 1, 0, 0, 1, 0),
    (1, 0, 1, 1, 0, 1, 0, 0, 0),
    (0, 1, 0, 0, 1, 1, 1, 0, 0),
    (0, 1, 1, 0, 0, 1, 1, 1, 0),
    (0, 0, 0, 1, 0, 1, 1, 1, 1),
    (0, 0, 1, 1, 0, 0, 0, 0, 1),
    (0, 1, 1, 0, 1, 1, 1, 1, 1),
    (1, 1, 1, 0, 1, 1, 0, 0, 0),
]



def f(list, x):
    turtle.penup()
    if list[0]:
        turtle.goto(x, 0)
        turtle.pendown()
        turtle.goto(x + 10, 10)
        turtle.penup()
    if list[1]:
        turtle.goto(x, 10)
        turtle.pendown()
        turtle.goto(x, 20)
        turtle.penup()
    if list[2]:
        turtle.goto(x, 20)
        turtle.pendown()
        turtle.goto(x + 10, 20)
        turtle.penup()
    if list[3]:
        turtle.goto(x + 10, 20)
        turtle.pendown()
        turtle.goto(x, 10)
        turtle.penup()
    if list[4]:
        turtle.goto(x + 10, 20)
        turtle.pendown()
        turtle.goto(x + 10, 10)
        turtle.penup()
    if list[5]:
        turtle.goto(x + 10, 10)
        turtle.pendown()
        turtle.goto(x, 10)
        turtle.penup()
    if list[6]:
        turtle.goto(x + 10, 10)
        turtle.pendown()
        turtle.goto(x + 10, 0)
        turtle.penup()
    if list[7]:
        turtle.goto(x + 10, 0)
        turtle.pendown()
        turtle.goto(x, 0)
        turtle.penup()
    if list[8]:
        turtle.goto(x, 0)
        turtle.pendown()
        turtle.goto(x, 10)
        turtle.penup()

A = list(map(int, input().split()))
x = 0
for i in range(len(A)):
    f(numbers[A[i]], x + 20*i)

turtle.forward(20)

turtle.exitonclick()