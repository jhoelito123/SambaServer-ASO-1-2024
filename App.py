import tkinter as tk
from Interface.home import intro
from Interface.firstInterface import Toplevel1

class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("Mi Aplicación")
        
        # Crear las instancias de las interfaces
        self.home = intro(self)
        self.first_interface = Toplevel1(self)
        
        # Mostrar la interfaz de inicio al inicio
        self.show_home_interface()
    
    def show_home_interface(self):
        # Ocultar la interfaz actual (si hay alguna)
        if hasattr(self, "current_interface"):
            self.current_interface.pack_forget()
        
        # Mostrar la interfaz de inicio
        self.home.pack(fill=tk.BOTH, expand=True)
        self.current_interface = self.home
    
    def show_first_interface(self):
        # Ocultar la interfaz actual (si hay alguna)
        if hasattr(self, "current_interface"):
            self.current_interface.pack_forget()
        
        # Mostrar la primera interfaz
        self.first_interface.pack(fill=tk.BOTH, expand=True)
        self.current_interface = self.first_interface

if __name__ == "__main__":
    app = App()
    app.mainloop()
