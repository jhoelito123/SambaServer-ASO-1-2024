import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox
from tkinter.constants import *
import os.path
import subprocess
import paramiko

_location = os.path.dirname(__file__)
colorLight = "#feffda"
colorGold = "#b3af46"
colorDef = "#d9d9d9"
label_config = {
    "background": colorLight,
    "font": ("Comic Sans MS", 12, "italic"),
    "foreground": "black",
    "anchor": "w",
}

class intro:
    def __init__(self, top=None, navigate_callback=None):
        top.geometry("681x673+612+210")
        top.minsize(120, 1)
        top.maxsize(1924, 1061)
        top.resizable(1,  1)
        top.title("Bienvenido")
        top.configure(background=colorLight)

        self.top = top
        self.navigate_callback = navigate_callback
        
        self.titleApp = tk.Label(self.top)
        self.titleApp.place(relx=0.015, rely=0.059, height=61, width=654)
        self.titleApp.configure(**label_config)
        self.titleApp.configure(font="-family {Comic Sans MS} -size 30 -weight bold")
        self.titleApp.configure(text='''Configuración de Servicio Samba''')
        
        self.logoSUSE = tk.Label(self.top)
        self.logoSUSE.place(relx=0.044, rely=0.208, height=201, width=273)
        self.logoSUSE.configure(**label_config)
        photo_location = os.path.join(_location,"src/suseLogo.png")
        global _img0
        _img0 = tk.PhotoImage(file=photo_location)
        self.logoSUSE.configure(image=_img0)

        self.logoSAMBA = tk.Label(self.top)
        self.logoSAMBA.place(relx=0.602, rely=0.238, height=111, width=220)
        self.logoSAMBA.configure(**label_config)
        photo_location = os.path.join(_location,"src/Samba medium.png")
        global _img1
        _img1 = tk.PhotoImage(file=photo_location)
        self.logoSAMBA.configure(image=_img1)

        self.cruz = tk.Label(self.top)
        self.cruz.place(relx=0.485, rely=0.268, height=81, width=45)
        self.cruz.configure(**label_config)
        self.cruz.configure(font="-family {Segoe UI} -size 36 -weight bold")
        self.cruz.configure(text='''X''')

        # self.LogoPyC = tk.Label(self.top)
        # self.LogoPyC.place(relx=0.059, rely=0.847, height=81, width=76)
        # self.LogoPyC.configure(**label_config)
        # photo_location = os.path.join(_location,"src/pyc little.png")
        # global _img2
        # _img2 = tk.PhotoImage(file=photo_location)
        # self.LogoPyC.configure(image=_img2)

        self.adam = tk.Label(self.top)
        self.adam.place(relx=0.176, rely=0.862, height=21, width=164)
        self.adam.configure(**label_config)
        self.adam.configure(text='''Adam Jhoel Mamani''')

        self.john = tk.Label(self.top)
        self.john.place(relx=0.631, rely=0.936, height=31, width=244)
        self.john.configure(**label_config)
        self.john.configure(text='''John Henry Chavarria Zurita''')

        self.armando = tk.Label(self.top)
        self.armando.place(relx=0.382, rely=0.892, height=31, width=195)
        self.armando.configure(**label_config)
        self.armando.configure(text='''Armando Gaspar Mamani''')

        self.label1 = tk.Label(self.top)
        self.label1.place(relx=0.25, rely=0.516, height=51, width=365)
        self.label1.configure(**label_config)
        self.label1.configure(font="-family {Comic Sans MS} -size 15")
        self.label1.configure(text='''Ingrese el usuario root de este Equipo''')

        self.label2 = tk.Label(self.top)
        self.label2.place(relx=0.191, rely=0.575, height=51, width=455)
        self.label2.configure(**label_config)
        self.label2.configure(font="-family {Comic Sans MS} -size 15")
        self.label2.configure(text='''para acceder a la configuración de este servicio:''')

        self.entryPass = tk.Entry(self.top)
        self.entryPass.place(relx=0.264, rely=0.684, height=20, relwidth=0.52)
        self.entryPass.configure(background="white")
        self.entryPass.configure(font="-family {Comic Sans MS} -size 10")
        self.entryPass.configure(foreground="black")
        self.entryPass.configure(selectforeground="black")
        self.entryPass.configure(show="*")

        """self.entryUser = tk.Entry(self.top)
        self.entryUser.place(relx=0.264, rely=0.624, height=20, relwidth=0.52)
        self.entryUser.configure(background="white")
        self.entryUser.configure(font="-family {Comic Sans MS} -size 10")
        self.entryUser.configure(foreground="black")
        self.entryUser.configure(selectforeground="black")"""

        self.labelPass = tk.Label(self.top)
        self.labelPass.place(relx=0.103, rely=0.684, height=21, width=84)
        self.labelPass.configure(**label_config)
        self.labelPass.configure(text='''Password:''')

        """self.labelUser = tk.Label(self.top)
        self.labelUser.place(relx=0.117, rely=0.624, height=21, width=64)
        self.labelUser.configure(**label_config)
        self.labelUser.configure(text='''User:''')"""

        self.Button1 = tk.Button(self.top)
        self.Button1.place(relx=0.47, rely=0.743, height=36, width=77)
        self.Button1.configure(activebackground=colorLight)
        self.Button1.configure(background=colorGold)
        self.Button1.configure(font="-family {Comic Sans MS} -size 14 -weight bold")
        self.Button1.configure(foreground="black")
        self.Button1.configure(text='''Enter''')
        self.Button1.configure(command=lambda: self.login_user(self.entryPass.get()))

    def login_user(self,password):
        command = "service sshd restart"
        process = subprocess.Popen(['sudo', '-S'] + command.split(), stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate(input=password.encode() + b'\n')
        
        HOST = 'localhost'
        try:
            client = paramiko.SSHClient()
            client.set_missing_host_key_policy( paramiko.AutoAddPolicy() )
            client.connect(HOST, username='root', password=password)
                        
            self.navigate_callback(client)
        except paramiko.ssh_exception.AuthenticationException as e:
            messagebox.showerror("Login", "Credenciales incorrectas")

#PA QUE TANTAS VENTANAS y el otro bucle (igual me estoy equivocando :v)
def start_up(parent=None,navigate_callback=None):
    _w1 = intro(parent,navigate_callback)

if __name__ == '__main__':
    start_up()