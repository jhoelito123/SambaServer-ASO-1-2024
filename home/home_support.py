import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *

import home

_debug = True # False to eliminate debug printing from callback functions.

def main(*args):
    '''Main entry point for the application.'''
    global root
    root = tk.Tk()
    root.protocol( 'WM_DELETE_WINDOW' , root.destroy)
    # Creates a toplevel widget.
    global _top1, _w1
    _top1 = root
    _w1 = home.intro(_top1)
    root.mainloop()

if __name__ == '__main__':
    home.start_up()




