import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *
import os.path

_location = os.path.dirname(__file__)

import version1_support

_bgcolor = '#d9d9d9'
_fgcolor = '#000000'

class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''

        top.geometry("936x600+402+99")
        top.minsize(120, 1)
        top.maxsize(1924, 1061)
        top.resizable(1,  1)
        top.title("Configuración de servicio Samba")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#ffdf33")
        top.configure(highlightcolor="#000000")

        self.top = top
        self.che64 = tk.IntVar()
        self.che63 = tk.IntVar()
        self.che69 = tk.IntVar()

        self.botonCancel = tk.Button(self.top)
        self.botonCancel.place(relx=0.812, rely=0.905, height=26, width=67)
        self.botonCancel.configure(activebackground="#d9d9d9")
        self.botonCancel.configure(activeforeground="black")
        self.botonCancel.configure(background="#d9d9d9")
        self.botonCancel.configure(disabledforeground="#a3a3a3")
        self.botonCancel.configure(font="-family {Consolas} -size 10")
        self.botonCancel.configure(foreground="#000000")
        self.botonCancel.configure(highlightbackground="#d9d9d9")
        self.botonCancel.configure(highlightcolor="#000000")
        self.botonCancel.configure(text='''Cancelar''')

        self.botonAccept = tk.Button(self.top)
        self.botonAccept.place(relx=0.897, rely=0.905, height=26, width=67)
        self.botonAccept.configure(activebackground="#d9d9d9")
        self.botonAccept.configure(activeforeground="black")
        self.botonAccept.configure(background="#b3af46")
        self.botonAccept.configure(disabledforeground="#a3a3a3")
        self.botonAccept.configure(font="-family {Consolas} -size 10")
        self.botonAccept.configure(foreground="#000000")
        self.botonAccept.configure(highlightbackground="#d9d9d9")
        self.botonAccept.configure(highlightcolor="#000000")
        self.botonAccept.configure(text='''Aceptar''')
        
        self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

        self.navigator = ttk.Notebook(self.top)
        self.navigator.place(relx=0.017, rely=0.022, relheight=0.853
                , relwidth=0.953)
        self.navigator_t1 = tk.Frame(self.navigator)
        self.navigator.add(self.navigator_t1, padding=3)
        self.navigator.tab(0, text='''Inicio''', compound="left"
                ,underline='''-1''', )
        self.navigator_t1.configure(borderwidth="5")
        self.navigator_t1.configure(background="#d9d9d9")
        self.navigator_t1.configure(highlightbackground="#d9d9d9")
        self.navigator_t1.configure(highlightcolor="#000000")
        self.navigator_t2 = tk.Frame(self.navigator)
        self.navigator.add(self.navigator_t2, padding=3)
        self.navigator.tab(1, text='''Recursos compartidos''', compound="left"
                ,underline='''-1''', )
        self.navigator_t2.configure(background="#d9d9d9")
        self.navigator_t2.configure(highlightbackground="#d9d9d9")
        self.navigator_t2.configure(highlightcolor="#000000")
        self.navigator_t3 = tk.Frame(self.navigator)
        self.navigator.add(self.navigator_t3, padding=3)
        self.navigator.tab(2, text='''Identidad''', compound="left"
                ,underline='''-1''', )
        self.navigator_t3.configure(background="#d9d9d9")
        self.navigator_t3.configure(highlightbackground="#d9d9d9")
        self.navigator_t3.configure(highlightcolor="#000000")

        self.cuadroInicial = tk.Frame(self.navigator_t1)
        self.cuadroInicial.place(relx=0.011, rely=0.041, relheight=0.508
                , relwidth=0.971)
        self.cuadroInicial.configure(relief='groove')
        self.cuadroInicial.configure(borderwidth="2")
        self.cuadroInicial.configure(relief="groove")
        self.cuadroInicial.configure(background="#d9d9d9")
        self.cuadroInicial.configure(highlightbackground="#d9d9d9")
        self.cuadroInicial.configure(highlightcolor="#000000")

        self.textEstado = tk.Label(self.cuadroInicial)
        self.textEstado.place(relx=0.023, rely=0.161, height=22, width=153)
        self.textEstado.configure(activebackground="#d9d9d9")
        self.textEstado.configure(activeforeground="black")
        self.textEstado.configure(anchor='w')
        self.textEstado.configure(background="#d9d9d9")
        self.textEstado.configure(compound='left')
        self.textEstado.configure(disabledforeground="#a3a3a3")
        self.textEstado.configure(font="-family {Courier New} -size 12 -weight bold")
        self.textEstado.configure(foreground="#000000")
        self.textEstado.configure(highlightbackground="#d9d9d9")
        self.textEstado.configure(highlightcolor="#000000")
        self.textEstado.configure(text='''Estado actual:''')

        self.statusService = tk.Label(self.cuadroInicial)
        self.statusService.place(relx=0.219, rely=0.153, height=22, width=74)
        self.statusService.configure(activebackground="#d9d9d9")
        self.statusService.configure(activeforeground="black")
        self.statusService.configure(anchor='w')
        self.statusService.configure(background="#d9d9d9")
        self.statusService.configure(compound='left')
        self.statusService.configure(disabledforeground="#a3a3a3")
        self.statusService.configure(font="-family {Consolas} -size 11")
        self.statusService.configure(foreground="#000000")
        self.statusService.configure(highlightbackground="#d9d9d9")
        self.statusService.configure(highlightcolor="#000000")
        self.statusService.configure(text='''Inactivo''')

        self.textLaterConfig = tk.Label(self.cuadroInicial)
        self.textLaterConfig.place(relx=0.023, rely=0.246, height=21, width=225)
        self.textLaterConfig.configure(activebackground="#d9d9d9")
        self.textLaterConfig.configure(activeforeground="black")
        self.textLaterConfig.configure(anchor='w')
        self.textLaterConfig.configure(background="#d9d9d9")
        self.textLaterConfig.configure(compound='left')
        self.textLaterConfig.configure(disabledforeground="#a3a3a3")
        self.textLaterConfig.configure(font="-family {Courier New} -size 12 -weight bold")
        self.textLaterConfig.configure(foreground="#000000")
        self.textLaterConfig.configure(highlightbackground="#d9d9d9")
        self.textLaterConfig.configure(highlightcolor="#000000")
        self.textLaterConfig.configure(text='''Después de configurar:''')

        self.restart = tk.Checkbutton(self.cuadroInicial)
        self.restart.place(relx=0.278, rely=0.335, relheight=0.093
                , relwidth=0.175)
        self.restart.configure(activebackground="#d9d9d9")
        self.restart.configure(activeforeground="black")
        self.restart.configure(anchor='w')
        self.restart.configure(background="#d9d9d9")
        self.restart.configure(compound='left')
        self.restart.configure(disabledforeground="#a3a3a3")
        self.restart.configure(font="-family {Consolas} -size 10")
        self.restart.configure(foreground="#000000")
        self.restart.configure(highlightbackground="#d9d9d9")
        self.restart.configure(highlightcolor="#000000")
        self.restart.configure(justify='left')
        self.restart.configure(text='''Reiniciar servicio''')
        self.restart.configure(variable=self.che64)

        self.estadoActual = tk.Checkbutton(self.cuadroInicial)
        self.estadoActual.place(relx=0.046, rely=0.335, relheight=0.093
                , relwidth=0.209)
        self.estadoActual.configure(activebackground="#d9d9d9")
        self.estadoActual.configure(activeforeground="black")
        self.estadoActual.configure(anchor='w')
        self.estadoActual.configure(background="#d9d9d9")
        self.estadoActual.configure(compound='left')
        self.estadoActual.configure(disabledforeground="#a3a3a3")
        self.estadoActual.configure(font="-family {Consolas} -size 10")
        self.estadoActual.configure(foreground="#000000")
        self.estadoActual.configure(highlightbackground="#d9d9d9")
        self.estadoActual.configure(highlightcolor="#000000")
        self.estadoActual.configure(justify='left')
        self.estadoActual.configure(text='''Mantener estado actual''')
        self.estadoActual.configure(variable=self.che63)

        self.startServiceCheck = tk.Checkbutton(self.cuadroInicial)
        self.startServiceCheck.place(relx=0.046, rely=0.52, relheight=0.097
                , relwidth=0.105)
        self.startServiceCheck.configure(activebackground="#d9d9d9")
        self.startServiceCheck.configure(activeforeground="black")
        self.startServiceCheck.configure(anchor='w')
        self.startServiceCheck.configure(background="#d9d9d9")
        self.startServiceCheck.configure(compound='left')
        self.startServiceCheck.configure(disabledforeground="#a3a3a3")
        self.startServiceCheck.configure(font="-family {Consolas} -size 10")
        self.startServiceCheck.configure(foreground="#000000")
        self.startServiceCheck.configure(highlightbackground="#d9d9d9")
        self.startServiceCheck.configure(highlightcolor="#000000")
        self.startServiceCheck.configure(justify='left')
        self.startServiceCheck.configure(text='''¿Iniciar?''')
        self.startServiceCheck.configure(variable=self.che69)

        self.Label1 = tk.Label(self.cuadroInicial)
        self.Label1.place(relx=0.023, rely=0.448, height=19, width=213)
        self.Label1.configure(activebackground="#d9d9d9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(anchor='w')
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(compound='left')
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font="-family {Courier New} -size 12 -weight bold")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="#000000")
        self.Label1.configure(text='''Después de reiniciar:''')

        self.tituloInicio = tk.Label(self.cuadroInicial)
        self.tituloInicio.place(relx=0.313, rely=0.04, height=22, width=324)
        self.tituloInicio.configure(activebackground="#d9d9d9")
        self.tituloInicio.configure(activeforeground="black")
        self.tituloInicio.configure(anchor='w')
        self.tituloInicio.configure(background="#d9d9d9")
        self.tituloInicio.configure(compound='left')
        self.tituloInicio.configure(disabledforeground="#a3a3a3")
        self.tituloInicio.configure(font="-family {Courier New} -size 15 -weight bold")
        self.tituloInicio.configure(foreground="#000000")
        self.tituloInicio.configure(highlightbackground="#d9d9d9")
        self.tituloInicio.configure(highlightcolor="#000000")
        self.tituloInicio.configure(text='''Configuración del Servicio''')

        self.Label2 = tk.Label(self.navigator_t2)
        self.Label2.place(relx=0.023, rely=0.019, height=20, width=214)
        self.Label2.configure(activebackground="#d9d9d9")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(anchor='w')
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(compound='left')
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font="-family {Courier New} -size 12 -weight bold")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="#000000")
        self.Label2.configure(text='''Recursos compartidos''')

        self.listActual = ScrolledListBox(self.navigator_t2)
        self.listActual.place(relx=0.023, rely=0.062, relheight=0.348
                , relwidth=0.938)
        self.listActual.configure(background="white")
        self.listActual.configure(cursor="xterm")
        self.listActual.configure(disabledforeground="#a3a3a3")
        self.listActual.configure(font="TkFixedFont")
        self.listActual.configure(foreground="black")
        self.listActual.configure(highlightbackground="#d9d9d9")
        self.listActual.configure(highlightcolor="#d9d9d9")
        self.listActual.configure(selectbackground="#d9d9d9")
        self.listActual.configure(selectforeground="black")

        self.botonAdd = tk.Button(self.navigator_t2)
        self.botonAdd.place(relx=0.023, rely=0.432, height=26, width=57)
        self.botonAdd.configure(activebackground="#d9d9d9")
        self.botonAdd.configure(activeforeground="black")
        self.botonAdd.configure(background="#d9d9d9")
        self.botonAdd.configure(disabledforeground="#a3a3a3")
        self.botonAdd.configure(font="-family {Consolas} -size 10")
        self.botonAdd.configure(foreground="#000000")
        self.botonAdd.configure(highlightbackground="#d9d9d9")
        self.botonAdd.configure(highlightcolor="#000000")
        self.botonAdd.configure(text='''Agregar''')

        self.botonEdit = tk.Button(self.navigator_t2)
        self.botonEdit.place(relx=0.101, rely=0.432, height=26, width=57)
        self.botonEdit.configure(activebackground="#d9d9d9")
        self.botonEdit.configure(activeforeground="black")
        self.botonEdit.configure(background="#d9d9d9")
        self.botonEdit.configure(disabledforeground="#a3a3a3")
        self.botonEdit.configure(font="-family {Consolas} -size 10")
        self.botonEdit.configure(foreground="#000000")
        self.botonEdit.configure(highlightbackground="#d9d9d9")
        self.botonEdit.configure(highlightcolor="#000000")
        self.botonEdit.configure(text='''Editar''')

        self.botonDel = tk.Button(self.navigator_t2)
        self.botonDel.place(relx=0.18, rely=0.432, height=26, width=57)
        self.botonDel.configure(activebackground="#d9d9d9")
        self.botonDel.configure(activeforeground="black")
        self.botonDel.configure(background="#d9d9d9")
        self.botonDel.configure(disabledforeground="#a3a3a3")
        self.botonDel.configure(font="-family {Consolas} -size 10")
        self.botonDel.configure(foreground="#000000")
        self.botonDel.configure(highlightbackground="#d9d9d9")
        self.botonDel.configure(highlightcolor="#000000")
        self.botonDel.configure(text='''Quitar''')

        self.Label3 = tk.Label(self.navigator_t3)
        self.Label3.place(relx=0.371, rely=0.041, height=21, width=214)
        self.Label3.configure(activebackground="#d9d9d9")
        self.Label3.configure(activeforeground="black")
        self.Label3.configure(anchor='w')
        self.Label3.configure(background="#d9d9d9")
        self.Label3.configure(compound='left')
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(font="-family {Courier New} -size 12 -weight bold")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(highlightbackground="#d9d9d9")
        self.Label3.configure(highlightcolor="#000000")
        self.Label3.configure(text='''Configuración básica''')

        self.frameWorkGroup = tk.Frame(self.navigator_t3)
        self.frameWorkGroup.place(relx=0.022, rely=0.102, relheight=0.4
                , relwidth=0.926)
        self.frameWorkGroup.configure(relief='groove')
        self.frameWorkGroup.configure(borderwidth="2")
        self.frameWorkGroup.configure(relief="groove")
        self.frameWorkGroup.configure(background="#d9d9d9")
        self.frameWorkGroup.configure(highlightbackground="#d9d9d9")
        self.frameWorkGroup.configure(highlightcolor="#000000")

        self.labelWorkgroup = tk.Label(self.frameWorkGroup)
        self.labelWorkgroup.place(relx=0.012, rely=0.051, height=21, width=163)
        self.labelWorkgroup.configure(activebackground="#d9d9d9")
        self.labelWorkgroup.configure(activeforeground="black")
        self.labelWorkgroup.configure(anchor='w')
        self.labelWorkgroup.configure(background="#d9d9d9")
        self.labelWorkgroup.configure(compound='left')
        self.labelWorkgroup.configure(disabledforeground="#a3a3a3")
        self.labelWorkgroup.configure(font="-family {Consolas} -size 11")
        self.labelWorkgroup.configure(foreground="#000000")
        self.labelWorkgroup.configure(highlightbackground="#d9d9d9")
        self.labelWorkgroup.configure(highlightcolor="#000000")
        self.labelWorkgroup.configure(text='''Nombre de WorkGroup''')

        self.entryWorkGroup = tk.Entry(self.frameWorkGroup)
        self.entryWorkGroup.place(relx=0.012, rely=0.185, height=20
                , relwidth=0.442)
        self.entryWorkGroup.configure(background="white")
        self.entryWorkGroup.configure(disabledforeground="#a3a3a3")
        self.entryWorkGroup.configure(font="-family {Consolas} -size 11")
        self.entryWorkGroup.configure(foreground="#000000")
        self.entryWorkGroup.configure(highlightbackground="#d9d9d9")
        self.entryWorkGroup.configure(highlightcolor="#000000")
        self.entryWorkGroup.configure(insertbackground="#000000")
        self.entryWorkGroup.configure(selectbackground="#d9d9d9")
        self.entryWorkGroup.configure(selectforeground="black")

# The following code is added to facilitate the Scrolled widgets you specified.
class AutoScroll(object):
    '''Configure the scrollbars for a widget.'''
    def __init__(self, master):
        #  Rozen. Added the try-except clauses so that this class
        #  could be used for scrolled entry widget for which vertical
        #  scrolling is not supported. 5/7/14.
        try:
            vsb = ttk.Scrollbar(master, orient='vertical', command=self.yview)
        except:
            pass
        hsb = ttk.Scrollbar(master, orient='horizontal', command=self.xview)
        try:
            self.configure(yscrollcommand=self._autoscroll(vsb))
        except:
            pass
        self.configure(xscrollcommand=self._autoscroll(hsb))
        self.grid(column=0, row=0, sticky='nsew')
        try:
            vsb.grid(column=1, row=0, sticky='ns')
        except:
            pass
        hsb.grid(column=0, row=1, sticky='ew')
        master.grid_columnconfigure(0, weight=1)
        master.grid_rowconfigure(0, weight=1)
        # Copy geometry methods of master  (taken from ScrolledText.py)
        methods = tk.Pack.__dict__.keys() | tk.Grid.__dict__.keys() \
                  | tk.Place.__dict__.keys()
        for meth in methods:
            if meth[0] != '_' and meth not in ('config', 'configure'):
                setattr(self, meth, getattr(master, meth))

    @staticmethod
    def _autoscroll(sbar):
        '''Hide and show scrollbar as needed.'''
        def wrapped(first, last):
            first, last = float(first), float(last)
            if first <= 0 and last >= 1:
                sbar.grid_remove()
            else:
                sbar.grid()
            sbar.set(first, last)
        return wrapped

    def __str__(self):
        return str(self.master)

def _create_container(func):
    '''Creates a ttk Frame with a given master, and use this new frame to
    place the scrollbars and the widget.'''
    def wrapped(cls, master, **kw):
        container = ttk.Frame(master)
        container.bind('<Enter>', lambda e: _bound_to_mousewheel(e, container))
        container.bind('<Leave>', lambda e: _unbound_to_mousewheel(e, container))
        return func(cls, container, **kw)
    return wrapped

class ScrolledListBox(AutoScroll, tk.Listbox):
    '''A standard Tkinter Listbox widget with scrollbars that will
    automatically show/hide as needed.'''
    @_create_container
    def __init__(self, master, **kw):
        tk.Listbox.__init__(self, master, **kw)
        AutoScroll.__init__(self, master)
    def size_(self):
        sz = tk.Listbox.size(self)
        return sz

import platform
def _bound_to_mousewheel(event, widget):
    child = widget.winfo_children()[0]
    if platform.system() == 'Windows' or platform.system() == 'Darwin':
        child.bind_all('<MouseWheel>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Shift-MouseWheel>', lambda e: _on_shiftmouse(e, child))
    else:
        child.bind_all('<Button-4>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Button-5>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Shift-Button-4>', lambda e: _on_shiftmouse(e, child))
        child.bind_all('<Shift-Button-5>', lambda e: _on_shiftmouse(e, child))

def _unbound_to_mousewheel(event, widget):
    if platform.system() == 'Windows' or platform.system() == 'Darwin':
        widget.unbind_all('<MouseWheel>')
        widget.unbind_all('<Shift-MouseWheel>')
    else:
        widget.unbind_all('<Button-4>')
        widget.unbind_all('<Button-5>')
        widget.unbind_all('<Shift-Button-4>')
        widget.unbind_all('<Shift-Button-5>')

def _on_mousewheel(event, widget):
    if platform.system() == 'Windows':
        widget.yview_scroll(-1*int(event.delta/120),'units')
    elif platform.system() == 'Darwin':
        widget.yview_scroll(-1*int(event.delta),'units')
    else:
        if event.num == 4:
            widget.yview_scroll(-1, 'units')
        elif event.num == 5:
            widget.yview_scroll(1, 'units')

def _on_shiftmouse(event, widget):
    if platform.system() == 'Windows':
        widget.xview_scroll(-1*int(event.delta/120), 'units')
    elif platform.system() == 'Darwin':
        widget.xview_scroll(-1*int(event.delta), 'units')
    else:
        if event.num == 4:
            widget.xview_scroll(-1, 'units')
        elif event.num == 5:
            widget.xview_scroll(1, 'units')
def start_up():
    version1_support.main()

if __name__ == '__main__':
    version1_support.main()