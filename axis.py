import turtle
from turtle import RawTurtle, ScrolledCanvas

def drawAxis(screenSize: float):
    t1 = turtle.Turtle()
    t2 = turtle.Turtle()
    t3 = turtle.Turtle()
    t4 = turtle.Turtle()

    turtles = [t1,t2,t3,t4]

    for x in turtles:
        x.pensize(3)
        x.shapesize(2,2,2)

    t1.forward(screenSize)

    t2.left(180)
    t2.forward(screenSize)

    t3.left(90)
    t3.forward(screenSize)

    t4.right(90)
    t4.forward(screenSize)