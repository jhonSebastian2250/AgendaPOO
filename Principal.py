from Ventana import Ventana
from tkinter import *

__author__ = 'Jhon Sebastian Zuñiga'


class Principal:
    if __name__ == '__main__':
        ven = Ventana()  # Crea un objeto de la ventana
        imagen = PhotoImage(file="lupa.gif")
        Label(ven, image=imagen).place(x=600, y=50)
        ven.mainloop()  # Para que la ventana se ejecute y no se cierre
