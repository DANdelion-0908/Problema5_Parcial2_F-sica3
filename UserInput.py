import tkinter as tk
from tkinter import ttk
import Simulation
import PlaneMathDraw
import decimal
import SphereMath
import blackHole

LIGHT_SPEED = 2.998e8

# Specific Particles
def setParticlesStats(event):
    selection = particleList.get()

    if(selection == "Partícula Personalizada"):
        particleChargeEntry.config(state=tk.ACTIVE)
        weightEntry.config(state=tk.ACTIVE)

    if(selection == "Protón"):
        particleChargeEntry.set(1.6e-19)
        weightEntry.set(1.67e-27)
        particleChargeEntry.config(state=tk.DISABLED)
        weightEntry.config(state=tk.DISABLED)

    elif(selection == "Positrón"):
        particleChargeEntry.set(1.6e-19)
        weightEntry.set(9.11e-31)
        particleChargeEntry.config(state=tk.DISABLED)
        weightEntry.config(state=tk.DISABLED)

    elif(selection == "Partícula Alfa"):
        particleChargeEntry.set(3.2e-19)
        weightEntry.set(6.68e-27)
        particleChargeEntry.config(state=tk.DISABLED)
        weightEntry.config(state=tk.DISABLED)

    elif(selection == "Núcleo de Litio"):
        particleChargeEntry.set(4.8e-19)
        weightEntry.set(1.169e-26)
        particleChargeEntry.config(state=tk.DISABLED)
        weightEntry.config(state=tk.DISABLED)

    elif(selection == "Núcleo de Carbón"):
        particleChargeEntry.set(9.6e-19)
        weightEntry.set(20.04e-27)
        particleChargeEntry.config(state=tk.DISABLED)
        weightEntry.config(state=tk.DISABLED)

# Figure Frame Enabler/Disabler
def figureEnabler():
    selection = figureSelection.get()
    if(selection == 1):
        notebook.add(sphereFrame, text='Esfera')
        notebook.forget(planeFrame)

    elif selection == 2:
        notebook.add(planeFrame, text="Plano")
        notebook.forget(sphereFrame)

# Button Enabler
def buttonEnabler():
    sphereElements = ["sphere", radioEntry.get(), chargeEntry.get(), particleList.get(), particleChargeEntry.get(), weightEntry.get(), speedEntry.get()]
    planeElements = ["plane", densityEntry.get() ,particleChargeEntry.get(), particleList.get(), weightEntry.get(), speedEntry.get()]
    selection = figureSelection.get()
    speed = decimal.Decimal(speedEntry.get())
    if(selection == 1 and speed < LIGHT_SPEED):

        initialUEL = SphereMath.calculateInitialElectricPotentialEnergy(Q= float(sphereElements[2]), q= float(sphereElements[4]), r= float(sphereElements[1]))
        scapeVelocity = SphereMath.calculateMinimumScapeVelocity(Ki = initialUEL, m= float(sphereElements[5]) )
        
        if( scapeVelocity > LIGHT_SPEED):
            blackHole.spawnBlackHole()

        elif all(elements != "" for elements in sphereElements):
            Simulation.Simulation(sphereElements)

        else:
            errorWindow = tk.Tk()
            errorWindow.resizable(False, False)
            errorWindow.title("¡ERROR!")
            lightSpeedLabel = ttk.Label(errorWindow, text="Asegúrate de llenar todos los campos.")
            lightSpeedLabel.pack()

    elif(selection == 2 and speed < LIGHT_SPEED):
        if all(elements != "" for elements in planeElements):
            planeDistanceLabel.config(text="Distancia recorrida: " + str(PlaneMathDraw.planeDistance(planeElements)) + " m")
            Simulation.Simulation(planeElements)

        else:
            errorWindow = tk.Tk()
            errorWindow.resizable(False, False)
            errorWindow.title("¡ERROR!")
            lightSpeedLabel = ttk.Label(errorWindow, text="Asegúrate de llenar todos los campos.")
            lightSpeedLabel.pack()

    elif(speed > LIGHT_SPEED):
        errorWindow = tk.Tk()
        errorWindow.resizable(False, False)
        errorWindow.title("¡ERROR!")
        lightSpeedLabel = ttk.Label(errorWindow, text="Ingresa una velocidad menor o igual a la velocidad de la luz en el vacío (2.998x10^8).")
        lightSpeedLabel.pack()
    
    else:
        errorWindow = tk.Tk()
        errorWindow.resizable(False, False)
        errorWindow.title("¡ERROR!")
        lightSpeedLabel = ttk.Label(errorWindow, text="Asegúrate de llenar todos los campos.")
        lightSpeedLabel.pack()

# Main Window
root = tk.Tk()
root.title('Disparador de Partículas')
root.resizable(False, False)

# Creating notebook to store the frames
notebook = ttk.Notebook(root)
notebook.pack(expand=True, fill='both')

# Creating frames
shapeFrame = ttk.Frame(notebook)
sphereFrame = ttk.Frame(notebook)
planeFrame = ttk.Frame(notebook)
particleFrame = ttk.Frame(notebook)

# Adding frames to notebook
notebook.add(shapeFrame, text='Figura')
notebook.add(particleFrame, text='Partícula')
notebook.add(sphereFrame, text='Esfera')
notebook.hide(sphereFrame)
notebook.add(planeFrame, text="Plano")
notebook.hide(planeFrame)

# Figure Frame
figureSelection = tk.IntVar(root, 0)

sphereRadiobutton = ttk.Radiobutton(shapeFrame, 
                                    text='Esfera', 
                                    variable=figureSelection, 
                                    value=1,
                                    command=figureEnabler).pack(anchor=tk.CENTER, pady=10)

planeRadiobutton = ttk.Radiobutton(shapeFrame,
                                   text="Plano",
                                   variable=figureSelection,
                                   value=2,
                                   command=figureEnabler).pack(anchor=tk.CENTER)

# Sphere Frame
radioLabel = ttk.Label(sphereFrame, text="Radio: ")
chargeLabel = ttk.Label(sphereFrame, text="Carga: ")

radioEntry = ttk.Spinbox(sphereFrame, from_=0.5, to=200, increment=0.1)
chargeEntry = ttk.Spinbox(sphereFrame, from_=0.5, to=200, increment=0.1)

radioLabel.grid(row=0, column=0, sticky= tk.W, pady=10)
chargeLabel.grid(row=1, column=0, sticky=tk.W)

radioEntry.grid(row=0, column=1, sticky=tk.W, pady=10)
chargeEntry.grid(row=1, column=1, sticky=tk.W)

radioDimension = ttk.Label(sphereFrame, text="m").grid(row=0, column=2)
sphereChargeDimension = ttk.Label(sphereFrame, text="C").grid(row=1, column=2)

# Plane Frame
densityLabel = ttk.Label(planeFrame, text="Densidad de carga: ")
planeDistanceLabel = ttk.Label(planeFrame, text="Distancia recorrida: ") 

densityEntry = ttk.Spinbox(planeFrame, from_=0.5, to=500, increment=0.1)

densityLabel.grid(row=0, column=0, sticky=tk.W, pady=20)
densityEntry.grid(row=0, column=1, sticky=tk.W)
densityDimension = ttk.Label(planeFrame, text="C/m^2").grid(row=0, column=2)
planeDistanceLabel.grid(row=1, column=0, sticky=tk.E)

# Particle Frame
particleLabel = ttk.Label(particleFrame, text="Partícula: ")
particleChargeLabel = ttk.Label(particleFrame, text="Carga: ")
weightLabel = ttk.Label(particleFrame, text="Masa: ")
speedLabel = ttk.Label(particleFrame, text="Velocidad Inicial: ")

particleChargeEntry = ttk.Spinbox(particleFrame, from_=0.5, to=500, increment=0.1)
weightEntry = ttk.Spinbox(particleFrame, from_=0.5, to=100, increment=0.1)
speedEntry = ttk.Spinbox(particleFrame, from_=0.5, to=500, increment=0.1)
speedEntry.set(1)

particleList = ttk.Combobox(particleFrame, state="readonly", values=["Partícula Personalizada","Protón","Núcleo de Litio", "Positrón", "Partícula Alfa", "Núcleo de Carbón"])
particleList.bind("<<ComboboxSelected>>", setParticlesStats)

particleLabel.grid(row=0, column=0, sticky=tk.W, pady=10)
particleChargeLabel.grid(row=1, column=0, sticky=tk.W)
weightLabel.grid(row=2, column=0, sticky=tk.W, pady=10)
speedLabel.grid(row=3, column=0, sticky=tk.W)

particleList.grid(row=0, column=1, sticky=tk.W)
particleChargeEntry.grid(row=1, column=1, sticky=tk.W)
weightEntry.grid(row=2, column=1, sticky=tk.W)
speedEntry.grid(row=3, column=1, sticky=tk.W)

chargeDimension = ttk.Label(particleFrame, text="C").grid(row=1, column=2)
weightDimension = ttk.Label(particleFrame, text="kg").grid(row=2, column=2)
speedDimension = ttk.Label(particleFrame, text="m/s").grid(row=3, column=2)

# Confirm Button
confirmButton = ttk.Button(root, text='Confirmar', command=buttonEnabler)
confirmButton.pack(fill=tk.X)

# Main process
root.mainloop()