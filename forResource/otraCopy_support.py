import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *

import windows

_debug = True # False to eliminate debug printing from callback functions.

def main(*args):
    '''Main entry point for the application.'''
    global root
    root = tk.Tk()
    root.protocol( 'WM_DELETE_WINDOW' , root.destroy)
    # Creates a toplevel widget.
    global _top1, _w1
    _top1 = root
    _w1 = windows.Toplevel1(_top1)
    # Creates a toplevel widget.
    global _top2, _w2
    _top2 = tk.Toplevel(root)
    _w2 = windows.topRO(_top2)
    # Creates a toplevel widget.
    global _top3, _w3
    _top3 = tk.Toplevel(root)
    _w3 = windows.topComment(_top3)
    # Creates a toplevel widget.
    global _top4, _w4
    _top4 = tk.Toplevel(root)
    _w4 = windows.topPath(_top4)
    # Creates a toplevel widget.
    global _top5, _w5
    _top5 = tk.Toplevel(root)
    _w5 = windows.newResource(_top5)
    # Creates a toplevel widget.
    global _top6, _w6
    _top6 = tk.Toplevel(root)
    _w6 = windows.topUmask(_top6)
    root.mainloop()

if __name__ == '__main__':
    windows.start_up()




