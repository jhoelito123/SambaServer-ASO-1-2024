
import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *
import os.path

_location = os.path.dirname(__file__)

import version1_support

_bgcolor = 'white'
_fgcolor = 'black'
_tabfg1 = 'black' 
_tabfg2 = 'white' 
_bgmode = 'light' 
_tabbg1 = '#d9d9d9' 
_tabbg2 = 'gray40' 


class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''

        top.geometry("936x652+473+160")
        top.minsize(120, 1)
        top.maxsize(1924, 1061)
        top.resizable(1,  1)
        top.title("Configuracion de servidor Samba")
        top.configure(background="white")
        top.configure(highlightbackground="white")
        top.configure(highlightcolor="black")

        self.top = top
        self.che64 = tk.IntVar()
        self.che63 = tk.IntVar()
        self.che69 = tk.IntVar()
        
        self.TNotebook1 = ttk.Notebook(self.top)
        self.TNotebook1.place(relx=0.017, rely=0.021, relheight=0.854
                , relwidth=0.953)
        self.ventanaInicio = tk.Frame(self.TNotebook1)
        self.TNotebook1.add(self.ventanaInicio, padding=3)
        self.TNotebook1.tab(0, text='''Inicio''', compound="left"
                ,underline='''-1''', )
        self.ventanaInicio.configure(background="white")
        self.ventanaInicio.configure(highlightbackground="white")
        self.ventanaInicio.configure(highlightcolor="black")
        self.ventanaRecursos = tk.Frame(self.TNotebook1)
        self.TNotebook1.add(self.ventanaRecursos, padding=3)
        self.TNotebook1.tab(1, text='''Recursos compartidos''', compound="left"
                ,underline='''-1''', )
        self.ventanaRecursos.configure(background="white")
        self.ventanaRecursos.configure(highlightbackground="white")
        self.ventanaRecursos.configure(highlightcolor="black")
        self.ventanaIdentidad = tk.Frame(self.TNotebook1)
        self.TNotebook1.add(self.ventanaIdentidad, padding=3)
        self.TNotebook1.tab(2, text='''Identidad''', compound="left"
                ,underline='''-1''', )
        self.ventanaIdentidad.configure(background="white")
        self.ventanaIdentidad.configure(highlightbackground="white")
        self.ventanaIdentidad.configure(highlightcolor="black")

        self.cuadroInicial = tk.Frame(self.ventanaInicio)
        self.cuadroInicial.place(relx=0.011, rely=0.042, relheight=0.508
                , relwidth=0.971)
        self.cuadroInicial.configure(relief='groove')
        self.cuadroInicial.configure(borderwidth="2")
        self.cuadroInicial.configure(relief="groove")
        self.cuadroInicial.configure(background="white")
        self.cuadroInicial.configure(highlightbackground="white")
        self.cuadroInicial.configure(highlightcolor="black")

        self.tituloIdentidad = tk.Label(self.cuadroInicial)
        self.tituloIdentidad.place(relx=0.313, rely=0.041, height=23, width=322)
        self.tituloIdentidad.configure(activebackground="#d9d9d9")
        self.tituloIdentidad.configure(activeforeground="black")
        self.tituloIdentidad.configure(anchor='w')
        self.tituloIdentidad.configure(background="white")
        self.tituloIdentidad.configure(compound='left')
        self.tituloIdentidad.configure(disabledforeground="#bfbfbf")
        self.tituloIdentidad.configure(font="-family {Courier New} -size 15 -weight bold")
        self.tituloIdentidad.configure(foreground="black")
        self.tituloIdentidad.configure(highlightbackground="white")
        self.tituloIdentidad.configure(highlightcolor="black")
        self.tituloIdentidad.configure(text='''Configuración del Servicio''')

        self.textEstado = tk.Label(self.cuadroInicial)
        self.textEstado.place(relx=0.023, rely=0.16, height=23, width=152)
        self.textEstado.configure(activebackground="#d9d9d9")
        self.textEstado.configure(activeforeground="black")
        self.textEstado.configure(anchor='w')
        self.textEstado.configure(background="white")
        self.textEstado.configure(compound='left')
        self.textEstado.configure(disabledforeground="#bfbfbf")
        self.textEstado.configure(font="-family {Courier New} -size 12 -weight bold")
        self.textEstado.configure(foreground="black")
        self.textEstado.configure(highlightbackground="white")
        self.textEstado.configure(highlightcolor="black")
        self.textEstado.configure(text='''Estado actual:''')

        self.statusService = tk.Label(self.cuadroInicial)
        self.statusService.place(relx=0.219, rely=0.153, height=23, width=73)
        self.statusService.configure(activebackground="#d9d9d9")
        self.statusService.configure(activeforeground="black")
        self.statusService.configure(anchor='w')
        self.statusService.configure(background="white")
        self.statusService.configure(compound='left')
        self.statusService.configure(disabledforeground="#bfbfbf")
        self.statusService.configure(font="-family {Consolas} -size 11")
        self.statusService.configure(foreground="black")
        self.statusService.configure(highlightbackground="white")
        self.statusService.configure(highlightcolor="black")
        self.statusService.configure(text='''Inactivo''')

        self.textLaterConfig = tk.Label(self.cuadroInicial)
        self.textLaterConfig.place(relx=0.023, rely=0.243, height=24, width=224)
        self.textLaterConfig.configure(activebackground="#d9d9d9")
        self.textLaterConfig.configure(activeforeground="black")
        self.textLaterConfig.configure(anchor='w')
        self.textLaterConfig.configure(background="white")
        self.textLaterConfig.configure(compound='left')
        self.textLaterConfig.configure(disabledforeground="#bfbfbf")
        self.textLaterConfig.configure(font="-family {Courier New} -size 12 -weight bold")
        self.textLaterConfig.configure(foreground="black")
        self.textLaterConfig.configure(highlightbackground="white")
        self.textLaterConfig.configure(highlightcolor="black")
        self.textLaterConfig.configure(text='''Después de configurar:''')

        self.Label1 = tk.Label(self.cuadroInicial)
        self.Label1.place(relx=0.023, rely=0.448, height=21, width=213)
        self.Label1.configure(activebackground="#d9d9d9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(anchor='w')
        self.Label1.configure(background="white")
        self.Label1.configure(compound='left')
        self.Label1.configure(disabledforeground="#bfbfbf")
        self.Label1.configure(font="-family {Courier New} -size 12 -weight bold")
        self.Label1.configure(foreground="black")
        self.Label1.configure(highlightbackground="white")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''Después de reiniciar:''')

        self.restart = tk.Checkbutton(self.cuadroInicial)
        self.restart.place(relx=0.278, rely=0.336, relheight=0.093
                , relwidth=0.174)
        self.restart.configure(activebackground="#d9d9d9")
        self.restart.configure(activeforeground="black")
        self.restart.configure(anchor='w')
        self.restart.configure(background="white")
        self.restart.configure(compound='left')
        self.restart.configure(disabledforeground="#bfbfbf")
        self.restart.configure(font="-family {Consolas} -size 10")
        self.restart.configure(foreground="black")
        self.restart.configure(highlightbackground="white")
        self.restart.configure(highlightcolor="black")
        self.restart.configure(justify='left')
        self.restart.configure(text='''Reiniciar servicio''')
        self.restart.configure(variable=self.che64)

        self.estadoActual = tk.Checkbutton(self.cuadroInicial)
        self.estadoActual.place(relx=0.046, rely=0.336, relheight=0.093
                , relwidth=0.21)
        self.estadoActual.configure(activebackground="#d9d9d9")
        self.estadoActual.configure(activeforeground="black")
        self.estadoActual.configure(anchor='w')
        self.estadoActual.configure(background="white")
        self.estadoActual.configure(compound='left')
        self.estadoActual.configure(disabledforeground="#bfbfbf")
        self.estadoActual.configure(font="-family {Consolas} -size 10")
        self.estadoActual.configure(foreground="black")
        self.estadoActual.configure(highlightbackground="white")
        self.estadoActual.configure(highlightcolor="black")
        self.estadoActual.configure(justify='left')
        self.estadoActual.configure(text='''Mantener estado actual''')
        self.estadoActual.configure(variable=self.che63)

        self.startServiceCheck = tk.Checkbutton(self.cuadroInicial)
        self.startServiceCheck.place(relx=0.046, rely=0.522, relheight=0.093
                , relwidth=0.106)
        self.startServiceCheck.configure(activebackground="#d9d9d9")
        self.startServiceCheck.configure(activeforeground="black")
        self.startServiceCheck.configure(anchor='w')
        self.startServiceCheck.configure(background="white")
        self.startServiceCheck.configure(compound='left')
        self.startServiceCheck.configure(disabledforeground="#bfbfbf")
        self.startServiceCheck.configure(font="-family {Consolas} -size 10")
        self.startServiceCheck.configure(foreground="black")
        self.startServiceCheck.configure(highlightbackground="white")
        self.startServiceCheck.configure(highlightcolor="black")
        self.startServiceCheck.configure(justify='left')
        self.startServiceCheck.configure(text='''¿Iniciar?''')
        self.startServiceCheck.configure(variable=self.che69)

        self.botonAccept = tk.Button(self.top)
        self.botonAccept.place(relx=0.896, rely=0.911, height=26, width=67)
        self.botonAccept.configure(activebackground="#d9d9d9")
        self.botonAccept.configure(activeforeground="black")
        self.botonAccept.configure(background="#b3af46")
        self.botonAccept.configure(disabledforeground="#bfbfbf")
        self.botonAccept.configure(font="-family {Consolas} -size 10")
        self.botonAccept.configure(foreground="black")
        self.botonAccept.configure(highlightbackground="white")
        self.botonAccept.configure(highlightcolor="black")
        self.botonAccept.configure(text='''Aceptar''')

        self.botonCancel = tk.Button(self.top)
        self.botonCancel.place(relx=0.812, rely=0.905, height=26, width=67)
        self.botonCancel.configure(activebackground="#d9d9d9")
        self.botonCancel.configure(activeforeground="black")
        self.botonCancel.configure(background="white")
        self.botonCancel.configure(disabledforeground="#bfbfbf")
        self.botonCancel.configure(font="-family {Consolas} -size 10")
        self.botonCancel.configure(foreground="black")
        self.botonCancel.configure(highlightbackground="white")
        self.botonCancel.configure(highlightcolor="black")
        self.botonCancel.configure(text='''Cancelar''')

def start_up():
    version1_support.main()

if __name__ == '__main__':
    version1_support.main()