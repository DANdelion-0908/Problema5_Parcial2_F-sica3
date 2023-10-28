import tkinter as tk
from tkinter import ttk

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
    sphereElements = [radioEntry.get(), chargeEntry.get(), particleList.get(), particleChargeEntry.get(), weightEntry.get(), speedEntry.get()]
    planeElements = [densityEntry.get() ,particleChargeEntry.get(), particleList.get(), weightEntry.get(), speedEntry.get()]
    selection = figureSelection.get()
    if(selection == 1):
        if all(elements is not "" for elements in sphereElements):
            print("Funca")

        else:
            print("Faltan campos")

    elif(selection == 2):
        if all(elements is not None for elements in planeElements):
            print("Funca")

        else:
            print("Faltan campos")

    else:
        print("Faltan campos")

# Main Window
root = tk.Tk()
# root.config(width=500, height=500)
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

radioEntry = ttk.Spinbox(sphereFrame, from_=0.5, to=200, increment=0.1, format="%.1f m")
chargeEntry = ttk.Spinbox(sphereFrame, from_=0.5, to=200, increment=0.1, format="%.1f C")

radioLabel.grid(row=0, column=0, sticky= tk.W, pady=10)
chargeLabel.grid(row=1, column=0, sticky=tk.W)

radioEntry.grid(row=0, column=1, sticky=tk.W, pady=10)
chargeEntry.grid(row=1, column=1, sticky=tk.W)

# Plane Frame
densityLabel = ttk.Label(planeFrame, text="Densidad de carga: ")

densityEntry = ttk.Spinbox(planeFrame, from_=0.5, to=500, increment=0.1, format="%.1f C/m^2")

densityLabel.grid(row=0, column=0, sticky=tk.W, pady=20)
densityEntry.grid(row=0, column=1, sticky=tk.W)

# Particle Frame
particleLabel = ttk.Label(particleFrame, text="Partícula: ")
particleChargeLabel = ttk.Label(particleFrame, text="Carga: ")
weightLabel = ttk.Label(particleFrame, text="Masa: ")
speedLabel = ttk.Label(particleFrame, text="Velocidad Inicial: ")

particleChargeEntry = ttk.Spinbox(particleFrame, from_=0.5, to=500, increment=0.1, format="%.1f C")
weightEntry = ttk.Spinbox(particleFrame, from_=0.5, to=100, increment=0.1, format="%.1f kg")
speedEntry = ttk.Spinbox(particleFrame, from_=0.5, to=500, increment=0.1, format="%.1f m/s")

particleList = ttk.Combobox(particleFrame, state="readonly", values=["Protón","Neutrón", "Electrón", "Partícula Alfa"])

particleLabel.grid(row=0, column=0, sticky=tk.W, pady=10)
particleChargeLabel.grid(row=1, column=0, sticky=tk.W)
weightLabel.grid(row=2, column=0, sticky=tk.W, pady=10)
speedLabel.grid(row=3, column=0, sticky=tk.W)

particleList.grid(row=0, column=1, sticky=tk.W)
particleChargeEntry.grid(row=1, column=1, sticky=tk.W)
weightEntry.grid(row=2, column=1, sticky=tk.W)
speedEntry.grid(row=3, column=1, sticky=tk.W)

# Confirm Button
confirmButton = ttk.Button(root, text='Confirmar', command=buttonEnabler)
confirmButton.pack(fill=tk.X)

# Main process
root.mainloop()