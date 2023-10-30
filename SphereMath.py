import turtle
import decimal
import math
import time

def calculateInitialElectricPotentialEnergy(Q: float, q: float, r: float):
    #Epsillon 0 constant, dielectric constante fo the void
    Eo = decimal.Decimal(8.85e-12)
    #Pi
    decimalPi = decimal.Decimal(math.pi)
    #Charge of the sphere
    Q = decimal.Decimal(Q)
    #Particle Charge
    q = decimal.Decimal(q)
    #Distance between the particle and sphere
    r = decimal.Decimal(r)

    U = (Q*q)/(4*decimalPi*Eo*r)

    return U


def calculateMinimumScapeVelocity(Ki: float, m: float):
    #Initial Kinetic energy (on infinity, initial electric potential energy = + initial kinetic energy)
    Ki = abs(decimal.Decimal(Ki))
    #Mass of the particle
    m = decimal.Decimal(m)

    Vi = math.sqrt( (2*Ki)/(m) )
    Vi = decimal.Decimal(Vi)

    return Vi

def calculateMaximumDistance(Q:float, q:float, m: float, Vi: float, r1: float):
    #Epsillon 0 constant, dielectric constante fo the void
    Eo = decimal.Decimal(8.85e-12)
    #Charge of the sphere
    Q = decimal.Decimal(Q)
    #Particle Charge
    q = decimal.Decimal(q)
    #Mass of the particle
    m = decimal.Decimal(m)
    #Initial velocity provided by the user
    Vi = decimal.Decimal(Vi)

    #Calculating Initial Electric Potential Energy
    Ui = decimal.Decimal(calculateInitialElectricPotentialEnergy(Q,q,r1))
    #Calculating Inistial Kinnetic Energy
    Ki = decimal.Decimal( (m * Vi * Vi) / 2 )

    decimalPi = decimal.Decimal(math.pi)
    
    MaxDistance = (Q*q)/(4*decimalPi*Eo* (Ki + Ui) )

    return MaxDistance

def calculateMaximumCharge(q: float, m:float, R:float):
    #Epsillon 0 constant, dielectric constante fo the void
    Eo = decimal.Decimal(8.85e-12)
    #Velocity of light
    C = decimal.Decimal(2.998e8)
    #Particle Charge
    q = decimal.Decimal(q)
    #Mass of the particle
    m = decimal.Decimal(m)
    #Distance, in this case the radius of the sphere
    R = decimal.Decimal(R)

    decimalPi = decimal.Decimal(math.pi)

    MaxQ = (2*decimalPi*Eo*m*R* C*C)/(q)

    return MaxQ

def drawMaxdistanceNoScape(maxDistance: float, radius: float):
    maxDistance = float(maxDistance)
    radius = float(radius)
    sphereTurtle = turtle.Turtle()
    sphereTurtle.setposition(radius,0)
    sphereTurtle.pensize(5)
    sphereTurtle.shape("circle")
    sphereTurtle.color('#403d9e')

    dividedDistnace = maxDistance/3

    if(maxDistance > 2000):
        sphereTurtle.speed(10)
        sphereTurtle.forward(2000)
        sphereTurtle.backward(2000)

    else:
        for i in range (0, 4):
            sphereTurtle.speed(10 - 3*i)
            sphereTurtle.forward(dividedDistnace)

        time.sleep(0.25)

        for i in range (0,4):
            sphereTurtle.speed(1 + 3*i)
            sphereTurtle.backward(dividedDistnace)


def drawScapeAnimation(scapeDistance: float, radius: float):
    scapeDistance = float(scapeDistance)
    radius = float(radius)
    sphereTurtle = turtle.Turtle()
    sphereTurtle.setposition(radius,0)
    sphereTurtle.pensize(5)
    sphereTurtle.shape("circle")
    sphereTurtle.color('#403d9e')

    sphereTurtle.speed(8)
    sphereTurtle.forward(2000)
