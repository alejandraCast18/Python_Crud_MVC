import tkinter as tk
from basedatos import Basedatos
from vista import Vista
from controlador import Controlador

ventana = tk.Tk()
ventana.resizable(width=False, height=False)
bd = Basedatos() 
vista = Vista(ventana) 
controlador = Controlador(bd) 
vista.set_controlador(controlador) 


if __name__ == '__main__':
    app = vista
    app.mainloop()