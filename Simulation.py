from drawings import *
import turtle
from axis import *


def Simulation(figureList: list):
    for x in figureList:
        print(x)

    turtle.clearscreen()
    gorge = turtle.Turtle()
    turtle.tracer(False)
    turtle.update()
    verticalScreensize = 800
    horizontalScreenSize = 2000 #resolucion de la pantalla

    draw_grid(10, horizontalScreenSize, turtle=gorge)
    #In this section we evaluate which sphere was sent by the UI
    

    drawAxis(verticalScreensize / 2)

    turtle.tracer(True)
    turtle.update()

    if(figureList[0] == "sphere"):
        Sphere(float (figureList[1]), gorge)

    elif(figureList[0] == "plane"):
        InfinitePlain(200, gorge)

    turtle.setup(800, verticalScreensize - 150)
    turtle.screensize(horizontalScreenSize, verticalScreensize)

    

    turtle.done()