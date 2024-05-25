import tkinter as tk
from Interface.home import start_up as start_home
from Interface.firstInterface import start_up_Interface as start_interface
from Interface.windows import start_up_windows

class App:
    def __init__(self):
        self.root = tk.Tk()
        self.root.withdraw()
        self.current_window = None
        self.root.protocol('WM_DELETE_WINDOW', self.on_closing)
        self.show_home()
                            
    def show_home(self):
        if self.current_window:
            self.current_window.destroy()
        self.current_window = tk.Toplevel(self.root)
        self.current_window.protocol("WM_DELETE_WINDOW", self.on_closing)
        start_home(self.current_window, self.show_interface)

    def show_interface(self, client):
        if self.current_window:
            self.current_window.destroy()
        self.client = client
        self.current_window = tk.Toplevel(self.root)
        self.current_window.protocol("WM_DELETE_WINDOW", self.on_closing)
        start_interface(self.current_window, self.show_home, self.show_windows, self.client)
    
    def show_windows(self, resource):
        if self.current_window:
            self.current_window.destroy()
        self.current_window = tk.Toplevel(self.root)
        self.current_window.protocol("WM_DELETE_WINDOW", self.on_closing)
        start_up_windows(self.current_window, self.show_interface, resource, self.client)
    
    def on_closing(self):
        if self.current_window:
            self.current_window.destroy()
        self.root.destroy()
        
if __name__ == "__main__":
    app = App()
    app.root.mainloop()