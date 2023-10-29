import turtle as tr
import decimal as dec
from math import pow

# Calculate maximun distance traveled by the particle
def planeDistance(elements: list):
    distance = float((float(elements[4]) * pow(float(elements[5]), 2)) / 
                    (float(elements[2]) * float(elements[1])))
    return distance
    
def planeDrawing(distance: float):
    planeTurtle = tr.Turtle()
    planeTurtle.teleport(0,50)
    planeTurtle.pensize(5)
    planeTurtle.color('#403d9e')
    planeTurtle.forward(distance)