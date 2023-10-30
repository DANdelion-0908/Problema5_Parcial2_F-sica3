import turtle as tr
import decimal as dec
from math import pow
import time

# Calculate maximun distance traveled by the particle
def planeDistance(elements: list):
    distance = abs(float(float(elements[4]) * pow(float(elements[5]), 2)) / (((float(elements[2])) * (float(elements[1])))))
    return distance

def planeDrawing(distance: float):
    planeTurtle = tr.Turtle()
    planeTurtle.penup()
    planeTurtle.pensize(5)
    planeTurtle.shape("circle")
    planeTurtle.color('#403d9e')
    planeTurtle.setposition(0,50)
    planeTurtle.pendown(distance)

    if (distance > 2000):
        planeTurtle.speed(0)
        planeTurtle.forward(distance)
        planeTurtle.backward(distance)

    else :
        dividedDistance = distance/ 3
        for i in range (0, 4):
            planeTurtle.speed(10 - 3*i)
            planeTurtle.forward(dividedDistance)

        time.sleep(0.25)

        for i in range (0,4):
            planeTurtle.speed(1 + 3*i)
            planeTurtle.backward(dividedDistance)