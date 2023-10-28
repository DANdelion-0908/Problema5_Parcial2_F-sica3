from drawings import *
import turtle


def Simulation(figureList: list):
    for x in figureList:
        print(x)

    turtle.clearscreen()
    gorge = turtle.Turtle()
    turtle.tracer(False)
    turtle.update()
    screensize = 300
    actualscreen = 2000 #resolucion de la pantalla

    draw_grid(10, actualscreen, turtle=gorge)

    turtle.tracer(True)
    turtle.update()

    turtle.screensize(actualscreen,801)

    Sphere(float (figureList[0]), gorge)

    turtle.done()