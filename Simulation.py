from drawings import *
import turtle
from axis import *
import PlaneMathDraw
from SphereMath import *
    
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

        sphereRadius = float(figureList[1])
        sphereCharge = float(figureList[2])
        particleCharge = float(figureList[4])
        particleMass = float(figureList[5])
        initialvelocity = float(figureList[6])
        

        initialUEL = calculateInitialElectricPotentialEnergy(Q= sphereCharge, q= particleCharge, r= sphereRadius)
        scapeVelocity = calculateMinimumScapeVelocity(Ki = initialUEL, m= particleMass)
        maxDistance = calculateMaximumDistance(Q = sphereCharge, q = particleCharge, m= particleMass, Vi= initialvelocity, r1= sphereRadius)

        print(scapeVelocity)
        print(maxDistance)

        if(initialvelocity < scapeVelocity):
            Sphere(sphereRadius, gorge)
            drawMaxdistanceNoScape(maxDistance, sphereRadius)
            print("No escapa")

        else:
            Sphere(sphereRadius, gorge)
            scapeDistance = calculateMaximumDistance(Q = sphereCharge, q = particleCharge, m= particleMass, Vi= scapeVelocity, r1= sphereRadius)
            drawScapeAnimation(scapeDistance, sphereRadius)
            print("escapa")




    elif(figureList[0] == "plane"):
        InfinitePlain(200, gorge)
        PlaneMathDraw.planeDrawing(PlaneMathDraw.planeDistance(figureList))

    turtle.setup(800, verticalScreensize - 150)
    turtle.screensize(horizontalScreenSize, verticalScreensize)

    turtle.done()