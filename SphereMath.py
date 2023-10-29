import turtle
import decimal
import math

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

    # Round the result to three decimal places
    U = round(U,3)
    return U


def calculateMinimumScapeVelocity(Ki: float, m: float):
    #Initial Kinetic energy (on infinity, initial electric potential energy = initial kinetic energy)
    Ki = -decimal.Decimal(Ki)
    #Mass of the particle
    m = decimal.Decimal(m)

    Vi = math.sqrt( (2*Ki)/(m) )
    Vi = decimal.Decimal(Vi)

    Vi = round(Vi, 1)
    return Vi

def calculateMaximumDistance(Q:float, q:float, m: float, Vi: float):
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

    decimalPi = decimal.Decimal(math.pi)
    
    MaxDistance = (Q*q)/(2*decimalPi*Eo*m*decimal.Decimal( math.pow(Vi,2) ))

    MaxDistance = round(MaxDistance, 3)
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

    MaxQ = round(MaxQ, 1)

    return MaxQ

result1UEL = calculateInitialElectricPotentialEnergy(-2e-6, 3.5e-6, 0.250)
result2VEL = calculateMinimumScapeVelocity(result1UEL, 1.50e-3)
result3DIST = calculateMaximumDistance(3.5e-6, 2e-6,  1.50e-3, result2VEL)
result4MAXQ = calculateMaximumCharge(-2e-6, 1.50e-3, 0.250e-8)

print("U inicial: ", result1UEL, "J")
print("Velocidad escape: ", result2VEL, "m/s")
print("Distancia maxima: ", result3DIST, "m")
print("Carga antes de agujero negro: ", result4MAXQ, "C")