import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *
import os.path
from windows import

_location = os.path.dirname(__file__)

class intro:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''

        top.geometry("681x673+612+210")
        top.minsize(120, 1)
        top.maxsize(1924, 1061)
        top.resizable(1,  1)
        top.title("Bienvenido")
        top.configure(background="#feffda")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="#000000")

        self.top = top

        self.titleApp = tk.Label(self.top)
        self.titleApp.place(relx=0.015, rely=0.059, height=61, width=654)
        self.titleApp.configure(activebackground="#d9d9d9")
        self.titleApp.configure(activeforeground="black")
        self.titleApp.configure(anchor='w')
        self.titleApp.configure(background="#feffda")
        self.titleApp.configure(compound='left')
        self.titleApp.configure(disabledforeground="#a3a3a3")
        self.titleApp.configure(font="-family {Comic Sans MS} -size 30 -weight bold")
        self.titleApp.configure(foreground="#000000")
        self.titleApp.configure(highlightbackground="#d9d9d9")
        self.titleApp.configure(highlightcolor="#000000")
        self.titleApp.configure(text='''Configuración de Servicio Samba''')
        
        self.logoSUSE = tk.Label(self.top)
        self.logoSUSE.place(relx=0.044, rely=0.178, height=161, width=273)
        self.logoSUSE.configure(activebackground="#d9d9d9")
        self.logoSUSE.configure(activeforeground="black")
        self.logoSUSE.configure(anchor='w')
        self.logoSUSE.configure(background="#feffda")
        self.logoSUSE.configure(compound='left')
        self.logoSUSE.configure(cursor="fleur")
        self.logoSUSE.configure(disabledforeground="#a3a3a3")
        self.logoSUSE.configure(foreground="#000000")
        self.logoSUSE.configure(highlightbackground="#d9d9d9")
        self.logoSUSE.configure(highlightcolor="#000000")
        photo_location = os.path.join(_location,"src/suse logo.png")
        global _img0
        _img0 = tk.PhotoImage(file=photo_location)
        self.logoSUSE.configure(image=_img0)

        self.logoSAMBA = tk.Label(self.top)
        self.logoSAMBA.place(relx=0.602, rely=0.208, height=111, width=220)
        self.logoSAMBA.configure(activebackground="#d9d9d9")
        self.logoSAMBA.configure(activeforeground="black")
        self.logoSAMBA.configure(anchor='w')
        self.logoSAMBA.configure(background="#feffda")
        self.logoSAMBA.configure(compound='left')
        self.logoSAMBA.configure(disabledforeground="#a3a3a3")
        self.logoSAMBA.configure(foreground="#000000")
        self.logoSAMBA.configure(highlightbackground="#d9d9d9")
        self.logoSAMBA.configure(highlightcolor="#000000")
        photo_location = os.path.join(_location,"src/Samba medium.png")
        global _img1
        _img1 = tk.PhotoImage(file=photo_location)
        self.logoSAMBA.configure(image=_img1)

        self.cruz = tk.Label(self.top)
        self.cruz.place(relx=0.485, rely=0.238, height=81, width=45)
        self.cruz.configure(activebackground="#d9d9d9")
        self.cruz.configure(activeforeground="black")
        self.cruz.configure(anchor='w')
        self.cruz.configure(background="#feffda")
        self.cruz.configure(compound='left')
        self.cruz.configure(disabledforeground="#a3a3a3")
        self.cruz.configure(font="-family {Segoe UI} -size 36 -weight bold")
        self.cruz.configure(foreground="black")
        self.cruz.configure(highlightbackground="#d9d9d9")
        self.cruz.configure(highlightcolor="#000000")
        self.cruz.configure(text='''X''')

        self.LogoPyC = tk.Label(self.top)
        self.LogoPyC.place(relx=0.059, rely=0.847, height=81, width=76)
        self.LogoPyC.configure(activebackground="#d9d9d9")
        self.LogoPyC.configure(activeforeground="black")
        self.LogoPyC.configure(anchor='w')
        self.LogoPyC.configure(background="#feffda")
        self.LogoPyC.configure(compound='left')
        self.LogoPyC.configure(disabledforeground="#a3a3a3")
        self.LogoPyC.configure(foreground="#000000")
        self.LogoPyC.configure(highlightbackground="#d9d9d9")
        self.LogoPyC.configure(highlightcolor="#000000")
        photo_location = os.path.join(_location,"src/pyc little.png")
        global _img2
        _img2 = tk.PhotoImage(file=photo_location)
        self.LogoPyC.configure(image=_img2)

        self.adam = tk.Label(self.top)
        self.adam.place(relx=0.176, rely=0.862, height=21, width=164)
        self.adam.configure(activebackground="#d9d9d9")
        self.adam.configure(activeforeground="black")
        self.adam.configure(anchor='w')
        self.adam.configure(background="#feffda")
        self.adam.configure(compound='left')
        self.adam.configure(disabledforeground="#a3a3a3")
        self.adam.configure(font="-family {Comic Sans MS} -size 13 -slant italic")
        self.adam.configure(foreground="black")
        self.adam.configure(highlightbackground="#d9d9d9")
        self.adam.configure(highlightcolor="#000000")
        self.adam.configure(text='''Adam Jhoel Mamani''')

        self.john = tk.Label(self.top)
        self.john.place(relx=0.631, rely=0.936, height=31, width=244)
        self.john.configure(activebackground="#d9d9d9")
        self.john.configure(activeforeground="black")
        self.john.configure(anchor='w')
        self.john.configure(background="#feffda")
        self.john.configure(compound='left')
        self.john.configure(disabledforeground="#a3a3a3")
        self.john.configure(font="-family {Comic Sans MS} -size 13 -slant italic")
        self.john.configure(foreground="black")
        self.john.configure(highlightbackground="#d9d9d9")
        self.john.configure(highlightcolor="#000000")
        self.john.configure(text='''John Henry Chavarria Zurita''')

        self.armando = tk.Label(self.top)
        self.armando.place(relx=0.382, rely=0.892, height=31, width=195)
        self.armando.configure(activebackground="#d9d9d9")
        self.armando.configure(activeforeground="black")
        self.armando.configure(anchor='w')
        self.armando.configure(background="#feffda")
        self.armando.configure(compound='left')
        self.armando.configure(disabledforeground="#a3a3a3")
        self.armando.configure(font="-family {Comic Sans MS} -size 12 -slant italic")
        self.armando.configure(foreground="black")
        self.armando.configure(highlightbackground="#d9d9d9")
        self.armando.configure(highlightcolor="#000000")
        self.armando.configure(text='''Armando Gaspar Mamani''')

        self.label1 = tk.Label(self.top)
        self.label1.place(relx=0.25, rely=0.416, height=51, width=365)
        self.label1.configure(activebackground="#d9d9d9")
        self.label1.configure(activeforeground="black")
        self.label1.configure(anchor='w')
        self.label1.configure(background="#feffda")
        self.label1.configure(compound='left')
        self.label1.configure(disabledforeground="#a3a3a3")
        self.label1.configure(font="-family {Comic Sans MS} -size 15")
        self.label1.configure(foreground="black")
        self.label1.configure(highlightbackground="#d9d9d9")
        self.label1.configure(highlightcolor="#000000")
        self.label1.configure(text='''Ingrese el usuario root de este Equipo''')

        self.label2 = tk.Label(self.top)
        self.label2.place(relx=0.191, rely=0.475, height=51, width=455)
        self.label2.configure(activebackground="#d9d9d9")
        self.label2.configure(activeforeground="black")
        self.label2.configure(anchor='w')
        self.label2.configure(background="#feffda")
        self.label2.configure(compound='left')
        self.label2.configure(disabledforeground="#a3a3a3")
        self.label2.configure(font="-family {Comic Sans MS} -size 15")
        self.label2.configure(foreground="black")
        self.label2.configure(highlightbackground="#d9d9d9")
        self.label2.configure(highlightcolor="#000000")
        self.label2.configure(text='''para acceder a la configuración de este servicio:''')

        self.entryPass = tk.Entry(self.top)
        self.entryPass.place(relx=0.264, rely=0.684, height=20, relwidth=0.52)
        self.entryPass.configure(background="white")
        self.entryPass.configure(disabledforeground="#a3a3a3")
        self.entryPass.configure(font="-family {Courier New} -size 10")
        self.entryPass.configure(foreground="black")
        self.entryPass.configure(highlightbackground="#d9d9d9")
        self.entryPass.configure(highlightcolor="#000000")
        self.entryPass.configure(insertbackground="#000000")
        self.entryPass.configure(selectbackground="#d9d9d9")
        self.entryPass.configure(selectforeground="black")
        self.entryPass.configure(show="*")


        self.entryUser = tk.Entry(self.top)
        self.entryUser.place(relx=0.264, rely=0.624, height=20, relwidth=0.52)
        self.entryUser.configure(background="white")
        self.entryUser.configure(disabledforeground="#a3a3a3")
        self.entryUser.configure(font="TkFixedFont")
        self.entryUser.configure(foreground="black")
        self.entryUser.configure(highlightbackground="#d9d9d9")
        self.entryUser.configure(highlightcolor="#000000")
        self.entryUser.configure(insertbackground="#000000")
        self.entryUser.configure(selectbackground="#d9d9d9")
        self.entryUser.configure(selectforeground="black")

        self.labelPass = tk.Label(self.top)
        self.labelPass.place(relx=0.103, rely=0.684, height=21, width=84)
        self.labelPass.configure(activebackground="#d9d9d9")
        self.labelPass.configure(activeforeground="black")
        self.labelPass.configure(anchor='w')
        self.labelPass.configure(background="#feffda")
        self.labelPass.configure(compound='left')
        self.labelPass.configure(disabledforeground="#a3a3a3")
        self.labelPass.configure(font="-family {Comic Sans MS} -size 12 -slant italic")
        self.labelPass.configure(foreground="black")
        self.labelPass.configure(highlightbackground="#d9d9d9")
        self.labelPass.configure(highlightcolor="#000000")
        self.labelPass.configure(text='''Password:''')

        self.labelUser = tk.Label(self.top)
        self.labelUser.place(relx=0.117, rely=0.624, height=21, width=64)
        self.labelUser.configure(activebackground="#d9d9d9")
        self.labelUser.configure(activeforeground="black")
        self.labelUser.configure(anchor='w')
        self.labelUser.configure(background="#feffda")
        self.labelUser.configure(compound='left')
        self.labelUser.configure(disabledforeground="#a3a3a3")
        self.labelUser.configure(font="-family {Comic Sans MS} -size 12 -slant italic")
        self.labelUser.configure(foreground="black")
        self.labelUser.configure(highlightbackground="#d9d9d9")
        self.labelUser.configure(highlightcolor="#000000")
        self.labelUser.configure(text='''User:''')

        self.Button1 = tk.Button(self.top)
        self.Button1.place(relx=0.47, rely=0.743, height=36, width=77)
        self.Button1.configure(activebackground="#d9d9d9")
        self.Button1.configure(activeforeground="black")
        self.Button1.configure(background="#b3af46")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(font="-family {Comic Sans MS} -size 14 -weight bold")
        self.Button1.configure(foreground="black")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="#000000")
        self.Button1.configure(text='''Enter''')

root = tk.Tk()

def start_up():
    '''Inicializa la aplicación.'''
    root.deiconify()
    root.protocol('WM_DELETE_WINDOW', root.destroy)
    _w1 = intro(root)
    root.mainloop()

if __name__ == '__main__':
    start_up()