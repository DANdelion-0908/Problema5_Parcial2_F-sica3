from tkinter import *
from PIL import ImageTk, Image

def spawnBlackHole():
    root = Toplevel()
    image_path = "res/black_hole_image.png"
    image = ImageTk.PhotoImage(Image.open(image_path))

    label_image = Label(root, image=image)
    label_image.pack(side=TOP)

    aclarationLabel = Label(root, text="La partícula se ha convertido en un agujero negro.", font=500)
    aclarationLabel.pack(side=BOTTOM)

    root.mainloop()