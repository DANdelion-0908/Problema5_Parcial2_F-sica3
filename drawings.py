import turtle
from turtle import RawTurtle, ScrolledCanvas
import decimal

def DrawCircle(tr: turtle, height: float, width: float, outline: float, color: str):
    tr.pensize(outline)
    if(color != ""):
        tr.pencolor(color)

    tr.shape("circle")
    tr.shapesize(height, width, outline)
    tr.fillcolor(color)

def Sphere(radius: float, t1: turtle):

    #Initial setup
    t1.pensize(5)
    t1.penup()
    t1.teleport(0, -1*radius)
    t1.pendown()

    #Drawing half of the circle
    t1.circle(radius, 180)

    #Painting half of the circle
    t1.fillcolor("Blue")
    t1.begin_fill()
    t1.circle(radius, 180)
    t1.end_fill()
    t1.penup()

    #Positioning pen to the circle's center
    t1.backward(radius)
    t1.left(90)
    t1.forward(radius)
    t1.right(90)
    t1.forward(radius)
    t1.pendown()


    #Making the inner circle
    DrawCircle(t1, radius/10, radius/10 * 0.20, 0.5, "darkblue")

#Function to draw a grid
def draw_grid(step, size,turtle):
    for i in range(-size, (size+1), step):
        turtle.penup()
        turtle.goto(i, -size)
        turtle.pendown()
        turtle.goto(i, size)
        
    for i in range(-size, (size+1), step):
        turtle.penup()
        turtle.goto(-size, i)
        turtle.pendown()
        turtle.goto(size, i)

#Funcion principal para test








