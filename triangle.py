from tkinter import *
import math

class Triangle:
    """Programme qui permet de calculer le périmètre et l’aire d’un triangle rectangle"""
    def __init__(self):
        self.hauteur = 0
        self.base = 0

    def aire(self):
        return round((self.base * self.hauteur) / 2.0,2)

    def perimetre(self):
        return round((self.base + self.hauteur + math.sqrt(self.base ** 2.0 + self.hauteur ** 2.0)),2)

   
def calculAire():
    maTriangle = Triangle()
    maTriangle.hauteur = float(entry_hauteur.get())
    maTriangle.base = float(entry_base.get())
    textresult.configure(text = "Aire :  \t" + str(maTriangle.aire()))
    



def calculPerimetre():
    maTriangle = Triangle()
    maTriangle.hauteur = float(entry_hauteur.get())
    maTriangle.base = float(entry_base.get())
    textresult.configure(text = "Perimetre :  \t" + str(maTriangle.perimetre()))

root = Tk()
root.title("Triangle")
root.geometry("480x360")



textbase = Label(root, text = "base : ")
textbase.grid(row = 0, column = 0, sticky = E)

entry_base = Entry(root)
entry_base.grid(row = 0, column = 1, sticky = E)



texthauteur = Label(root, text = "hauteur : ")
texthauteur.grid(row = 1, column = 0, sticky = E)


entry_hauteur = Entry(root)
entry_hauteur.grid(row = 1, column = 1, sticky = E)


textresult = Label(root, text = " --:")
textresult.grid(row = 3, column = 0, sticky = W)


boutonaire = Button(root, text = "Aire", command = calculAire)
boutonaire.grid(row = 5, column = 0)

boutonperimetre = Button(root, text = "Perimetre", command = calculPerimetre)
boutonperimetre.grid(row = 5, column = 1)




root.mainloop()
