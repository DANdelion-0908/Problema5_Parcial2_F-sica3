from drawings import *
import turtle

def Simulation():

    gorge = turtle.Turtle()

    turtle.Turtle()
    turtle.tracer(False)
    turtle.update()
    screensize = 300
    actualscreen = 2000 #resolucion de la pantalla

    draw_grid(10, actualscreen, turtle= gorge)

    turtle.tracer(True)
    turtle.update()

    turtle.screensize(actualscreen,801)

    Sphere(50)

    turtle.exitonclick()

Simulation()