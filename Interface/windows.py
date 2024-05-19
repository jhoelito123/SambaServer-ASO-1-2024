import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *
import os.path

_location = os.path.dirname(__file__)

_bgcolor = '#d9d9d9'
_fgcolor = '#000000'

nameResource = "mis_archivos"
resource = [
    ["comment", "Chimichangas"],
    ["path", "/etc/casa"],
    ["readOnly", YES],
    ["createMask", 777]
]

resource2 = {
    'comment': "chimichangas",
    'path': "/etc/casa",
    'readOnly': 'YES',
    'createMask': 777,
}

class Toplevel1:
    def __init__(self, top=None,navigate_callback=None, update_resource_callback=None):
        #VENTANA DE ESTA INTERFAZ
        top.geometry("667x528+564+92")
        top.minsize(120, 1)
        top.maxsize(1924, 1061)
        top.resizable(1,  1)
        top.title("Editar Recurso")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="#000000")

        self.top = top
        self.navigate_callback = navigate_callback
        self.update_resource_callback = update_resource_callback
        
        self.labelTextTitle = tk.Label(self.top)
        self.labelTextTitle.place(relx=0.25, rely=0.0, height=25, width=205)
        self.labelTextTitle.configure(activebackground="#d9d9d9")
        self.labelTextTitle.configure(activeforeground="black")
        self.labelTextTitle.configure(anchor='w')
        self.labelTextTitle.configure(background="#d9d9d9")
        self.labelTextTitle.configure(compound='left')
        self.labelTextTitle.configure(disabledforeground="#a3a3a3")
        self.labelTextTitle.configure(font="-family {Courier New} -size 12 -weight bold")
        self.labelTextTitle.configure(foreground="#000000")
        self.labelTextTitle.configure(highlightbackground="#d9d9d9")
        self.labelTextTitle.configure(highlightcolor="#000000")
        self.labelTextTitle.configure(text='''Recurso compartido''')

        self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)
        
        self.nameResource = tk.Label(self.top)
        self.nameResource.place(relx=0.54, rely=0.0, height=25, width=271)
        self.nameResource.configure(activebackground="#d9d9d9")
        self.nameResource.configure(activeforeground="black")
        self.nameResource.configure(anchor='w')
        self.nameResource.configure(background="#d9d9d9")
        self.nameResource.configure(compound='left')
        self.nameResource.configure(disabledforeground="#a3a3a3")
        self.nameResource.configure(font="-family {Courier New} -size 12 -weight bold")
        self.nameResource.configure(foreground="#000000")
        self.nameResource.configure(highlightbackground="#d9d9d9")
        self.nameResource.configure(highlightcolor="#000000")
        self.nameResource.configure(text=nameResource) #global variable dependiendo

        self.butonBack = tk.Button(self.top)
        self.butonBack.place(relx=0.75, rely=0.911, height=26, width=67)
        self.butonBack.configure(activebackground="#d9d9d9")
        self.butonBack.configure(activeforeground="black")
        self.butonBack.configure(background="#d9d9d9")
        self.butonBack.configure(disabledforeground="#a3a3a3")
        self.butonBack.configure(font="-family {Consolas} -size 10")
        self.butonBack.configure(foreground="#000000")
        self.butonBack.configure(highlightbackground="#d9d9d9")
        self.butonBack.configure(highlightcolor="#000000")
        self.butonBack.configure(text='''Atrás''')
        self.butonBack.configure(command=self.navigate_callback)

        self.Listbox1 = tk.Listbox(self.top)
        self.Listbox1.place(relx=0.033, rely=0.068, relheight=0.506
                , relwidth=0.94)
        self.Listbox1.configure(background="white")
        self.Listbox1.configure(font="-family {Consolas} -size 12")
        self.Listbox1.configure(foreground="#000000")
        self.Listbox1.configure(highlightbackground="#d9d9d9")
        self.Listbox1.configure(highlightcolor="#000000")
        self.Listbox1.configure(selectbackground="#feffda")
        self.Listbox1.configure(selectforeground="black")
        self.Listbox1.insert(tk.END, "{:<20}{}".format("- -variable- -", "- -valor- -"))
        
        # Insertar los datos de resource en la Listbox
        updateListBox(self.Listbox1)
                
        # Botones para agregar, editar y quitar    
        self.butonSave = tk.Button(self.top)
        self.butonSave.place(relx=0.87, rely=0.911, height=26, width=67)
        self.butonSave.configure(activebackground="#d9d9d9")
        self.butonSave.configure(activeforeground="black")
        self.butonSave.configure(background="#b3af46")
        self.butonSave.configure(disabledforeground="#a3a3a3")
        self.butonSave.configure(font="-family {Consolas} -size 10")
        self.butonSave.configure(foreground="#000000")
        self.butonSave.configure(highlightbackground="#d9d9d9")
        self.butonSave.configure(highlightcolor="#000000")
        self.butonSave.configure(text='''Aceptar''')

        self.botonAdd = tk.Button(self.top)
        self.botonAdd.place(relx=0.045, rely=0.587, height=26, width=67)
        self.botonAdd.configure(activebackground="#d9d9d9")
        self.botonAdd.configure(activeforeground="black")
        self.botonAdd.configure(background="#d9d9d9")
        self.botonAdd.configure(disabledforeground="#a3a3a3")
        self.botonAdd.configure(font="-family {Consolas} -size 10")
        self.botonAdd.configure(foreground="#000000")
        self.botonAdd.configure(highlightbackground="#d9d9d9")
        self.botonAdd.configure(highlightcolor="#000000")
        self.botonAdd.configure(text='''Agregar''')

        self.botonEdit = tk.Button(self.top)
        self.botonEdit.place(relx=0.165, rely=0.587, height=26, width=57)
        self.botonEdit.configure(activebackground="#d9d9d9")
        self.botonEdit.configure(activeforeground="black")
        self.botonEdit.configure(background="#d9d9d9")
        self.botonEdit.configure(disabledforeground="#a3a3a3")
        self.botonEdit.configure(font="-family {Consolas} -size 10")
        self.botonEdit.configure(foreground="#000000")
        self.botonEdit.configure(highlightbackground="#d9d9d9")
        self.botonEdit.configure(highlightcolor="#000000")
        self.botonEdit.configure(text='''Editar''')
        self.botonEdit.configure(command=lambda: analiceEdit(self.Listbox1,self))

        self.botonQuit = tk.Button(self.top)
        self.botonQuit.place(relx=0.27, rely=0.587, height=26, width=57)
        self.botonQuit.configure(activebackground="#d9d9d9")
        self.botonQuit.configure(activeforeground="black")
        self.botonQuit.configure(background="#d9d9d9")
        self.botonQuit.configure(disabledforeground="#a3a3a3")
        self.botonQuit.configure(font="-family {Consolas} -size 10")
        self.botonQuit.configure(foreground="#000000")
        self.botonQuit.configure(highlightbackground="#d9d9d9")
        self.botonQuit.configure(highlightcolor="#000000")
        self.botonQuit.configure(text='''Quitar''')
        
def updateListBox(listbox):
    listbox.delete(0, tk.END)
    for clave, valor in resource2.items():
        listbox.insert(tk.END, "{:<20}{}".format(clave, valor))
                    
#EVENTOS DEL LOS BOTONES AGREGAR, EDITAR, QUITAR        
def analiceEdit(listbox,self):
    selected_index = listbox.curselection()
    if selected_index:
        selected_item_text = listbox.get(selected_index[0])
        variable = selected_item_text.split()[0]
        
        if variable == "comment":
            current_comment = selected_item_text.split()[1]  # Obtener el comentario actual
            self.edit_comment_window = tk.Toplevel(self.top)
            top_comment_instance = topComment(self.edit_comment_window, initial_comment=current_comment, listbox=listbox)
            print("Editar comentario")
        elif variable == "path":
            current_path = selected_item_text.split()[1]
            self.edit_path_window = tk.Toplevel(self.top)
            top_path_instance = topPath(self.edit_path_window,initial_path = current_path, listbox=listbox)
            print("Editar ruta")
        elif variable == "readOnly":
            current_ro = selected_item_text.split()[1]
            self.edit_ro = tk.Toplevel(self.top)
            top_ro_instance = topRO(self.edit_ro,initial_ro=current_ro, listbox=listbox)
            print("Editar permisos de lectura/escritura")
        elif variable == "createMask":
            print("Editar otra propiedad")
            currentMask = selected_item_text.split()[1]
            self.editMask = tk.Toplevel(self.top)
            top_mask = topUmask(self.editMask,initialMask=currentMask, listbox=listbox)    
        else:
            print("Caso aparte")
    else:
        print("Ningún elemento seleccionado")

class topRO:
    def __init__(self, top=None,initial_ro="", listbox=None):
        top.geometry("331x116+850+202")
        top.minsize(120, 1)
        top.maxsize(1924, 1061)
        top.resizable(1,  1)
        top.title("Read Only")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="#000000")

        self.top = top
        self.listbox=listbox
        self.che51 = tk.BooleanVar(value=True if initial_ro=='YES' else False)

        def update_RO(self):
                if self.che51.get():
                        ro_status = "YES"
                else:
                        ro_status = "NO"
                # Aquí puedes agregar la lógica para guardar el estado actualizado
                print("Read Only actualizado:", ro_status)
                resource2['readOnly'] = ro_status
                updateListBox(self.listbox)
                self.top.destroy()
        
        self.checkReadOnly = tk.Checkbutton(self.top)
        self.checkReadOnly.place(relx=0.393, rely=0.319, relheight=0.198
                , relwidth=0.184)
        self.checkReadOnly.configure(activebackground="#d9d9d9")
        self.checkReadOnly.configure(activeforeground="black")
        self.checkReadOnly.configure(anchor='w')
        self.checkReadOnly.configure(background="#d9d9d9")
        self.checkReadOnly.configure(compound='left')
        self.checkReadOnly.configure(disabledforeground="#a3a3a3")
        self.checkReadOnly.configure(font="-family {Comic Sans MS} -size 10 -slant italic")
        self.checkReadOnly.configure(foreground="#000000")
        self.checkReadOnly.configure(highlightbackground="#d9d9d9")
        self.checkReadOnly.configure(highlightcolor="#000000")
        self.checkReadOnly.configure(justify='left')
        self.checkReadOnly.configure(text='''YES''')
        self.checkReadOnly.configure(variable=self.che51)

        self.acceptRO = tk.Button(self.top)
        self.acceptRO.place(relx=0.785, rely=0.69, height=26, width=57)
        self.acceptRO.configure(activebackground="#d9d9d9")
        self.acceptRO.configure(activeforeground="black")
        self.acceptRO.configure(background="#b3af46")
        self.acceptRO.configure(disabledforeground="#a3a3a3")
        self.acceptRO.configure(font="-family {Comic Sans MS} -size 9")
        self.acceptRO.configure(foreground="#000000")
        self.acceptRO.configure(highlightbackground="#d9d9d9")
        self.acceptRO.configure(highlightcolor="#000000")
        self.acceptRO.configure(text='''Aceptar''')
        self.acceptRO.configure(command=lambda: update_RO(self))

        self.cancelRO = tk.Button(self.top)
        self.cancelRO.place(relx=0.574, rely=0.69, height=26, width=57)
        self.cancelRO.configure(activebackground="#d9d9d9")
        self.cancelRO.configure(activeforeground="black")
        self.cancelRO.configure(background="#d9d9d9")
        self.cancelRO.configure(disabledforeground="#a3a3a3")
        self.cancelRO.configure(font="-family {Comic Sans MS} -size 9")
        self.cancelRO.configure(foreground="#000000")
        self.cancelRO.configure(highlightbackground="#d9d9d9")
        self.cancelRO.configure(highlightcolor="#000000")
        self.cancelRO.configure(text='''Cancelar''')
        self.cancelRO.configure(command=self.top.destroy)

        self.labelRO = tk.Label(self.top)
        self.labelRO.place(relx=0.363, rely=0.078, height=20, width=94)
        self.labelRO.configure(activebackground="#d9d9d9")
        self.labelRO.configure(activeforeground="black")
        self.labelRO.configure(anchor='w')
        self.labelRO.configure(background="#d9d9d9")
        self.labelRO.configure(compound='left')
        self.labelRO.configure(disabledforeground="#a3a3a3")
        self.labelRO.configure(font="-family {Comic Sans MS} -size 11 -weight bold")
        self.labelRO.configure(foreground="#000000")
        self.labelRO.configure(highlightbackground="#d9d9d9")
        self.labelRO.configure(highlightcolor="#000000")
        self.labelRO.configure(text='''Read Only?''')

class topComment:
    def __init__(self, top=None, initial_comment="", listbox=None):
        screen_width = top.winfo_screenwidth()
        screen_height = top.winfo_screenheight()

        # Calcular las coordenadas para centrar la ventana
        x = (screen_width - 250) // 2  # El ancho de la ventana es 250
        y = (screen_height - 116) // 2  # La altura de la ventana es 116

        top.geometry(f"250x116+{x}+{y}")
        top.minsize(120, 1)
        top.maxsize(1924, 1061)
        top.resizable(1,  1)
        top.title("Comment")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="#000000")

        self.top = top
        self.listbox = listbox
        
        def update_comment(self):
                new_comment = self.entryComment.get()
                # Aquí puedes agregar la lógica para guardar el comentario actualizado
                print("Comentario actualizado:", new_comment)
                resource2['comment'] = new_comment
                updateListBox(self.listbox)
                self.top.destroy()
        
        self.entryComment = tk.Entry(top)
        self.entryComment.place(relx=0.12, rely=0.345, height=20, relwidth=0.776)
        self.entryComment.insert(0, initial_comment)

        self.entryComment.configure(background="white")
        self.entryComment.configure(disabledforeground="#a3a3a3")
        self.entryComment.configure(font="-family {Comic Sans MS} -size 10 -slant italic")
        self.entryComment.configure(foreground="#000000")
        self.entryComment.configure(highlightbackground="#d9d9d9")
        self.entryComment.configure(highlightcolor="#000000")
        self.entryComment.configure(insertbackground="#000000")
        self.entryComment.configure(selectbackground="#d9d9d9")
        self.entryComment.configure(selectforeground="black")

        self.labelComment = tk.Label(self.top)
        self.labelComment.place(relx=0.36, rely=0.086, height=20, width=74)
        self.labelComment.configure(activebackground="#d9d9d9")
        self.labelComment.configure(activeforeground="black")
        self.labelComment.configure(anchor='w')
        self.labelComment.configure(background="#d9d9d9")
        self.labelComment.configure(compound='left')
        self.labelComment.configure(disabledforeground="#a3a3a3")
        self.labelComment.configure(font="-family {Comic Sans MS} -size 11 -weight bold")
        self.labelComment.configure(foreground="#000000")
        self.labelComment.configure(highlightbackground="#d9d9d9")
        self.labelComment.configure(highlightcolor="#000000")
        self.labelComment.configure(text='''Comment''')

        self.acceptComment = tk.Button(self.top)
        self.acceptComment.place(relx=0.68, rely=0.69, height=26, width=57)
        self.acceptComment.configure(activebackground="#d9d9d9")
        self.acceptComment.configure(activeforeground="black")
        self.acceptComment.configure(background="#b3af46")
        self.acceptComment.configure(disabledforeground="#a3a3a3")
        self.acceptComment.configure(font="-family {Comic Sans MS} -size 9")
        self.acceptComment.configure(foreground="#000000")
        self.acceptComment.configure(highlightbackground="#d9d9d9")
        self.acceptComment.configure(highlightcolor="#000000")
        self.acceptComment.configure(text='''Aceptar''')
        self.acceptComment.configure(command=lambda: update_comment(self))
        
        self.cancelComment = tk.Button(self.top)
        self.cancelComment.place(relx=0.4, rely=0.69, height=26, width=57)
        self.cancelComment.configure(activebackground="#d9d9d9")
        self.cancelComment.configure(activeforeground="black")
        self.cancelComment.configure(background="#d9d9d9")
        self.cancelComment.configure(disabledforeground="#a3a3a3")
        self.cancelComment.configure(font="-family {Comic Sans MS} -size 9")
        self.cancelComment.configure(foreground="#000000")
        self.cancelComment.configure(highlightbackground="#d9d9d9")
        self.cancelComment.configure(highlightcolor="#000000")
        self.cancelComment.configure(text='''Cancelar''')
        self.cancelComment.configure(command=self.top.destroy)

class topPath:
    def __init__(self, top=None,initial_path="", listbox=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''

        top.geometry("241x116+312+348")
        top.minsize(120, 1)
        top.maxsize(1924, 1061)
        top.resizable(1,  1)
        top.title("Define Path")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="#000000")

        self.top = top
        self.listbox = listbox

        def update_path(self):
            new_path = self.entryPath.get()
            # Aquí puedes agregar la lógica para guardar el comentario actualizado
            print("Comentario actualizado:", new_path)
            resource2['path'] = new_path
            updateListBox(self.listbox)
            self.top.destroy()
        
        self.acceptPath = tk.Button(self.top)
        self.acceptPath.place(relx=0.68, rely=0.69, height=26, width=57)
        self.acceptPath.configure(activebackground="#d9d9d9")
        self.acceptPath.configure(activeforeground="black")
        self.acceptPath.configure(background="#b3af46")
        self.acceptPath.configure(disabledforeground="#a3a3a3")
        self.acceptPath.configure(font="-family {Comic Sans MS} -size 9")
        self.acceptPath.configure(foreground="#000000")
        self.acceptPath.configure(highlightbackground="#d9d9d9")
        self.acceptPath.configure(highlightcolor="#000000")
        self.acceptPath.configure(text='''Aceptar''')
        self.acceptPath.configure(command=lambda: update_path(self))

        self.entryPath = tk.Entry(self.top)
        self.entryPath.place(relx=0.083, rely=0.345, height=20, relwidth=0.805)
        self.entryPath.configure(background="white")
        self.entryPath.configure(disabledforeground="#a3a3a3")
        self.entryPath.configure(font="-family {Comic Sans MS} -size 10 -slant italic")
        self.entryPath.configure(foreground="#000000")
        self.entryPath.configure(highlightbackground="#d9d9d9")
        self.entryPath.configure(highlightcolor="#000000")
        self.entryPath.configure(insertbackground="#000000")
        self.entryPath.configure(selectbackground="#d9d9d9")
        self.entryPath.configure(selectforeground="black")
        self.entryPath.insert(0, initial_path)

        self.cancelPath = tk.Button(self.top)
        self.cancelPath.place(relx=0.398, rely=0.69, height=26, width=57)
        self.cancelPath.configure(activebackground="#d9d9d9")
        self.cancelPath.configure(activeforeground="black")
        self.cancelPath.configure(background="#d9d9d9")
        self.cancelPath.configure(disabledforeground="#a3a3a3")
        self.cancelPath.configure(font="-family {Comic Sans MS} -size 9")
        self.cancelPath.configure(foreground="#000000")
        self.cancelPath.configure(highlightbackground="#d9d9d9")
        self.cancelPath.configure(highlightcolor="#000000")
        self.cancelPath.configure(text='''Cancelar''')
        self.cancelPath.configure(command=top.destroy)

        self.labelP = tk.Label(self.top)
        self.labelP.place(relx=0.415, rely=0.086, height=20, width=42)
        self.labelP.configure(activebackground="#d9d9d9")
        self.labelP.configure(activeforeground="black")
        self.labelP.configure(anchor='w')
        self.labelP.configure(background="#d9d9d9")
        self.labelP.configure(compound='left')
        self.labelP.configure(disabledforeground="#a3a3a3")
        self.labelP.configure(font="-family {Comic Sans MS} -size 11 -weight bold")
        self.labelP.configure(foreground="#000000")
        self.labelP.configure(highlightbackground="#d9d9d9")
        self.labelP.configure(highlightcolor="#000000")
        self.labelP.configure(text='''Path''')

class newResource:
    def __init__(self, top=None):

        top.geometry("328x312+560+663")
        top.minsize(120, 1)
        top.maxsize(1924, 1061)
        top.resizable(1,  1)
        top.title("Add new Resource")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="#000000")

        self.top = top
        self.che67 = tk.IntVar()

        self.acceptNR = tk.Button(self.top)
        self.acceptNR.place(relx=0.762, rely=0.859, height=26, width=57)
        self.acceptNR.configure(activebackground="#d9d9d9")
        self.acceptNR.configure(activeforeground="black")
        self.acceptNR.configure(background="#b3af46")
        self.acceptNR.configure(disabledforeground="#a3a3a3")
        self.acceptNR.configure(font="-family {Comic Sans MS} -size 9")
        self.acceptNR.configure(foreground="#000000")
        self.acceptNR.configure(highlightbackground="#d9d9d9")
        self.acceptNR.configure(highlightcolor="#000000")
        self.acceptNR.configure(text='''Aceptar''')

        self.cancelNR = tk.Button(self.top)
        self.cancelNR.place(relx=0.549, rely=0.859, height=26, width=57)
        self.cancelNR.configure(activebackground="#d9d9d9")
        self.cancelNR.configure(activeforeground="black")
        self.cancelNR.configure(background="#d9d9d9")
        self.cancelNR.configure(disabledforeground="#a3a3a3")
        self.cancelNR.configure(font="-family {Comic Sans MS} -size 9")
        self.cancelNR.configure(foreground="#000000")
        self.cancelNR.configure(highlightbackground="#d9d9d9")
        self.cancelNR.configure(highlightcolor="#000000")
        self.cancelNR.configure(text='''Cancelar''')

        self.entryPathNR = tk.Entry(self.top)
        self.entryPathNR.place(relx=0.183, rely=0.628, height=20, relwidth=0.591)

        self.entryPathNR.configure(background="white")
        self.entryPathNR.configure(disabledforeground="#a3a3a3")
        self.entryPathNR.configure(font="-family {Comic Sans MS} -size 10 -slant italic")
        self.entryPathNR.configure(foreground="#000000")
        self.entryPathNR.configure(highlightbackground="#d9d9d9")
        self.entryPathNR.configure(highlightcolor="#000000")
        self.entryPathNR.configure(insertbackground="#000000")
        self.entryPathNR.configure(selectbackground="#d9d9d9")
        self.entryPathNR.configure(selectforeground="black")

        self.labelPathNR = tk.Label(self.top)
        self.labelPathNR.place(relx=0.396, rely=0.529, height=24, width=42)
        self.labelPathNR.configure(activebackground="#d9d9d9")
        self.labelPathNR.configure(activeforeground="black")
        self.labelPathNR.configure(anchor='w')
        self.labelPathNR.configure(background="#d9d9d9")
        self.labelPathNR.configure(compound='left')
        self.labelPathNR.configure(disabledforeground="#a3a3a3")
        self.labelPathNR.configure(font="-family {Comic Sans MS} -size 11 -weight bold")
        self.labelPathNR.configure(foreground="#000000")
        self.labelPathNR.configure(highlightbackground="#d9d9d9")
        self.labelPathNR.configure(highlightcolor="#000000")
        self.labelPathNR.configure(text='''Path''')

        self.entryCommentNR = tk.Entry(self.top)
        self.entryCommentNR.place(relx=0.183, rely=0.429, height=20
                , relwidth=0.591)
        self.entryCommentNR.configure(background="white")
        self.entryCommentNR.configure(disabledforeground="#a3a3a3")
        self.entryCommentNR.configure(font="-family {Comic Sans MS} -size 10 -slant italic")
        self.entryCommentNR.configure(foreground="#000000")
        self.entryCommentNR.configure(highlightbackground="#d9d9d9")
        self.entryCommentNR.configure(highlightcolor="#000000")
        self.entryCommentNR.configure(insertbackground="#000000")
        self.entryCommentNR.configure(selectbackground="#d9d9d9")
        self.entryCommentNR.configure(selectforeground="black")

        self.labelComment = tk.Label(self.top)
        self.labelComment.place(relx=0.366, rely=0.33, height=25, width=72)
        self.labelComment.configure(activebackground="#d9d9d9")
        self.labelComment.configure(activeforeground="black")
        self.labelComment.configure(anchor='w')
        self.labelComment.configure(background="#d9d9d9")
        self.labelComment.configure(compound='left')
        self.labelComment.configure(disabledforeground="#a3a3a3")
        self.labelComment.configure(font="-family {Comic Sans MS} -size 11 -weight bold")
        self.labelComment.configure(foreground="#000000")
        self.labelComment.configure(highlightbackground="#d9d9d9")
        self.labelComment.configure(highlightcolor="#000000")
        self.labelComment.configure(text='''Comment''')

        self.entryNameNR = tk.Entry(self.top)
        self.entryNameNR.place(relx=0.183, rely=0.231, height=20, relwidth=0.591)

        self.entryNameNR.configure(background="white")
        self.entryNameNR.configure(disabledforeground="#a3a3a3")
        self.entryNameNR.configure(font="-family {Comic Sans MS} -size 10 -slant italic")
        self.entryNameNR.configure(foreground="#000000")
        self.entryNameNR.configure(highlightbackground="#d9d9d9")
        self.entryNameNR.configure(highlightcolor="#000000")
        self.entryNameNR.configure(insertbackground="#000000")
        self.entryNameNR.configure(selectbackground="#d9d9d9")
        self.entryNameNR.configure(selectforeground="black")

        self.labelNameNR = tk.Label(self.top)
        self.labelNameNR.place(relx=0.396, rely=0.163, height=14, width=52)
        self.labelNameNR.configure(activebackground="#d9d9d9")
        self.labelNameNR.configure(activeforeground="black")
        self.labelNameNR.configure(anchor='w')
        self.labelNameNR.configure(background="#d9d9d9")
        self.labelNameNR.configure(compound='left')
        self.labelNameNR.configure(disabledforeground="#a3a3a3")
        self.labelNameNR.configure(font="-family {Comic Sans MS} -size 11 -weight bold")
        self.labelNameNR.configure(foreground="#000000")
        self.labelNameNR.configure(highlightbackground="#d9d9d9")
        self.labelNameNR.configure(highlightcolor="#000000")
        self.labelNameNR.configure(text='''Name''')

        self.chechRO_NR = tk.Checkbutton(self.top)
        self.chechRO_NR.place(relx=0.305, rely=0.728, relheight=0.09
                , relwidth=0.338)
        self.chechRO_NR.configure(activebackground="#d9d9d9")
        self.chechRO_NR.configure(activeforeground="black")
        self.chechRO_NR.configure(anchor='w')
        self.chechRO_NR.configure(background="#d9d9d9")
        self.chechRO_NR.configure(compound='left')
        self.chechRO_NR.configure(disabledforeground="#a3a3a3")
        self.chechRO_NR.configure(font="-family {Comic Sans MS} -size 11 -weight bold")
        self.chechRO_NR.configure(foreground="#000000")
        self.chechRO_NR.configure(highlightbackground="#d9d9d9")
        self.chechRO_NR.configure(highlightcolor="#000000")
        self.chechRO_NR.configure(justify='left')
        self.chechRO_NR.configure(text='''Read Only''')
        self.chechRO_NR.configure(variable=self.che67)

        self.labelNR = tk.Label(self.top)
        self.labelNR.place(relx=0.152, rely=0.032, height=25, width=224)
        self.labelNR.configure(activebackground="#d9d9d9")
        self.labelNR.configure(activeforeground="black")
        self.labelNR.configure(anchor='w')
        self.labelNR.configure(background="#d9d9d9")
        self.labelNR.configure(compound='left')
        self.labelNR.configure(disabledforeground="#a3a3a3")
        self.labelNR.configure(font="-family {Comic Sans MS} -size 13 -weight bold -slant italic")
        self.labelNR.configure(foreground="#000000")
        self.labelNR.configure(highlightbackground="#d9d9d9")
        self.labelNR.configure(highlightcolor="#000000")
        self.labelNR.configure(text='''Nuevo recurso compartido''')

class topUmask:
    def __init__(self, top=None,initialMask="", listbox=None):
        firstDigit = int(int(initialMask) /100)
        secondDigit = int((int(initialMask) / 10)%10)
        threeDigit = int(int(initialMask)%10) 
        print(firstDigit)
        print(secondDigit)
        print(threeDigit)
        top.geometry("340x226+942+657")
        top.minsize(120, 1)
        top.maxsize(1924, 1061)
        top.resizable(1,  1)
        top.title("Create Mask for Resoruce")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="#000000")

        self.top = top
        self.listbox = listbox
        self.cheOR = tk.BooleanVar()
        self.cheOW = tk.BooleanVar()
        self.cheOX = tk.BooleanVar()
        self.cheGR = tk.BooleanVar()
        self.cheGW = tk.BooleanVar()
        self.cheGX = tk.BooleanVar()
        self.cheUR = tk.BooleanVar()
        self.cheUW = tk.BooleanVar()
        self.cheUX = tk.BooleanVar()
        
        #Creo que se estan manjenado mal xd
        
        if firstDigit >= 4:
            self.cheUR.set(True)
        if firstDigit % 4 >= 2:
            self.cheUW.set(True)
        if firstDigit % 2 >= 1:
            self.cheUX.set(True)
            
        if secondDigit >= 4:
            self.cheGR.set(True)
        if secondDigit % 4 >= 2:
            self.cheGW.set(True)
        if secondDigit % 2 >= 1:
            self.cheGX.set(True)

        if threeDigit >= 4:
            self.cheOR.set(True)
        if threeDigit % 4 >= 2:
            self.cheOW.set(True)
        if threeDigit % 2 >= 1:
            self.cheOX.set(True)
            
        def updateMask(self):
            firstDigit = 0
            secondDigit = 0
            threeDigit = 0
            
            if self.cheUR.get(): firstDigit += 4
            if self.cheUW.get(): firstDigit += 2
            if self.cheUX.get(): firstDigit += 1
            
            if self.cheGR.get(): secondDigit += 4
            if self.cheGW.get(): secondDigit += 2
            if self.cheGX.get(): secondDigit += 1
            
            if self.cheOR.get(): threeDigit += 4
            if self.cheOW.get(): threeDigit += 2
            if self.cheOX.get(): threeDigit += 1
                        
            resource2["createMask"] = f'{firstDigit}{secondDigit}{threeDigit}'
            
            updateListBox(self.listbox)
            self.top.destroy()

        self.textGroup = tk.Label(self.top)
        self.textGroup.place(relx=0.059, rely=0.442, height=24, width=47)
        self.textGroup.configure(activebackground="#d9d9d9")
        self.textGroup.configure(activeforeground="black")
        self.textGroup.configure(anchor='w')
        self.textGroup.configure(background="#d9d9d9")
        self.textGroup.configure(compound='left')
        self.textGroup.configure(disabledforeground="#a3a3a3")
        self.textGroup.configure(font="-family {Comic Sans MS} -size 11 -slant italic")
        self.textGroup.configure(foreground="#000000")
        self.textGroup.configure(highlightbackground="#d9d9d9")
        self.textGroup.configure(highlightcolor="#000000")
        self.textGroup.configure(text='''Group''')

        self.textOthers = tk.Label(self.top)
        self.textOthers.place(relx=0.059, rely=0.575, height=24, width=57)
        self.textOthers.configure(activebackground="#d9d9d9")
        self.textOthers.configure(activeforeground="black")
        self.textOthers.configure(anchor='w')
        self.textOthers.configure(background="#d9d9d9")
        self.textOthers.configure(compound='left')
        self.textOthers.configure(disabledforeground="#a3a3a3")
        self.textOthers.configure(font="-family {Comic Sans MS} -size 11 -slant italic")
        self.textOthers.configure(foreground="#000000")
        self.textOthers.configure(highlightbackground="#d9d9d9")
        self.textOthers.configure(highlightcolor="#000000")
        self.textOthers.configure(text='''Others''')

        self.checkOR = tk.Checkbutton(self.top)
        self.checkOR.place(relx=0.353, rely=0.575, relheight=0.075
                , relwidth=0.053)
        self.checkOR.configure(activebackground="#d9d9d9")
        self.checkOR.configure(activeforeground="black")
        self.checkOR.configure(anchor='w')
        self.checkOR.configure(background="#d9d9d9")
        self.checkOR.configure(compound='left')
        self.checkOR.configure(disabledforeground="#a3a3a3")
        self.checkOR.configure(font="-family {Segoe UI} -size 10")
        self.checkOR.configure(foreground="#000000")
        self.checkOR.configure(highlightbackground="#d9d9d9")
        self.checkOR.configure(highlightcolor="#000000")
        self.checkOR.configure(justify='left')
        self.checkOR.configure(variable=self.cheOR)
        if(self.cheOR.get()): self.checkOR.select()

        self.checkOW = tk.Checkbutton(self.top)
        self.checkOW.place(relx=0.441, rely=0.575, relheight=0.075
                , relwidth=0.053)
        self.checkOW.configure(activebackground="#d9d9d9")
        self.checkOW.configure(activeforeground="black")
        self.checkOW.configure(anchor='w')
        self.checkOW.configure(background="#d9d9d9")
        self.checkOW.configure(compound='left')
        self.checkOW.configure(disabledforeground="#a3a3a3")
        self.checkOW.configure(font="-family {Segoe UI} -size 10")
        self.checkOW.configure(foreground="#000000")
        self.checkOW.configure(highlightbackground="#d9d9d9")
        self.checkOW.configure(highlightcolor="#000000")
        self.checkOW.configure(justify='left')
        self.checkOW.configure(variable=self.cheOW)
        if(self.cheOW.get()): self.checkOW.select()

        self.checkOX = tk.Checkbutton(self.top)
        self.checkOX.place(relx=0.529, rely=0.575, relheight=0.075
                , relwidth=0.053)
        self.checkOX.configure(activebackground="#d9d9d9")
        self.checkOX.configure(activeforeground="black")
        self.checkOX.configure(anchor='w')
        self.checkOX.configure(background="#d9d9d9")
        self.checkOX.configure(compound='left')
        self.checkOX.configure(disabledforeground="#a3a3a3")
        self.checkOX.configure(font="-family {Segoe UI} -size 10")
        self.checkOX.configure(foreground="#000000")
        self.checkOX.configure(highlightbackground="#d9d9d9")
        self.checkOX.configure(highlightcolor="#000000")
        self.checkOX.configure(justify='left')
        self.checkOX.configure(variable=self.cheOX)
        self.checkOX.configure(command= lambda: print(self.cheOX.get()))
        if(self.cheOX.get()): self.checkOX.select()
        

        self.checkGR = tk.Checkbutton(self.top)
        self.checkGR.place(relx=0.353, rely=0.442, relheight=0.075
                , relwidth=0.053)
        self.checkGR.configure(activebackground="#d9d9d9")
        self.checkGR.configure(activeforeground="black")
        self.checkGR.configure(anchor='w')
        self.checkGR.configure(background="#d9d9d9")
        self.checkGR.configure(compound='left')
        self.checkGR.configure(disabledforeground="#a3a3a3")
        self.checkGR.configure(font="-family {Segoe UI} -size 10")
        self.checkGR.configure(foreground="#000000")
        self.checkGR.configure(highlightbackground="#d9d9d9")
        self.checkGR.configure(highlightcolor="#000000")
        self.checkGR.configure(justify='left')
        self.checkGR.configure(variable=self.cheGR)
        if(self.cheGR.get()): self.checkGR.select()

        self.checkGW = tk.Checkbutton(self.top)
        self.checkGW.place(relx=0.441, rely=0.442, relheight=0.075
                , relwidth=0.053)
        self.checkGW.configure(activebackground="#d9d9d9")
        self.checkGW.configure(activeforeground="black")
        self.checkGW.configure(anchor='w')
        self.checkGW.configure(background="#d9d9d9")
        self.checkGW.configure(compound='left')
        self.checkGW.configure(disabledforeground="#a3a3a3")
        self.checkGW.configure(font="-family {Segoe UI} -size 10")
        self.checkGW.configure(foreground="#000000")
        self.checkGW.configure(highlightbackground="#d9d9d9")
        self.checkGW.configure(highlightcolor="#000000")
        self.checkGW.configure(justify='left')
        self.checkGW.configure(variable=self.cheGW)
        if(self.cheGW.get()): self.checkGW.select()

        self.checkGX = tk.Checkbutton(self.top)
        self.checkGX.place(relx=0.529, rely=0.442, relheight=0.075
                , relwidth=0.053)
        self.checkGX.configure(activebackground="#d9d9d9")
        self.checkGX.configure(activeforeground="black")
        self.checkGX.configure(anchor='w')
        self.checkGX.configure(background="#d9d9d9")
        self.checkGX.configure(compound='left')
        self.checkGX.configure(disabledforeground="#a3a3a3")
        self.checkGX.configure(font="-family {Segoe UI} -size 10")
        self.checkGX.configure(foreground="#000000")
        self.checkGX.configure(highlightbackground="#d9d9d9")
        self.checkGX.configure(highlightcolor="#000000")
        self.checkGX.configure(justify='left')
        self.checkGX.configure(variable=self.cheGX)
        if(self.cheGW.get()): self.checkGW.select()

        self.checkUW = tk.Checkbutton(self.top)
        self.checkUW.place(relx=0.441, rely=0.31, relheight=0.075
                , relwidth=0.053)
        self.checkUW.configure(activebackground="#d9d9d9")
        self.checkUW.configure(activeforeground="black")
        self.checkUW.configure(anchor='w')
        self.checkUW.configure(background="#d9d9d9")
        self.checkUW.configure(compound='left')
        self.checkUW.configure(disabledforeground="#a3a3a3")
        self.checkUW.configure(font="-family {Segoe UI} -size 10")
        self.checkUW.configure(foreground="#000000")
        self.checkUW.configure(highlightbackground="#d9d9d9")
        self.checkUW.configure(highlightcolor="#000000")
        self.checkUW.configure(justify='left')
        self.checkUW.configure(variable=self.cheUW)
        if(self.cheUW.get()): self.checkUW.select()

        self.checkUX = tk.Checkbutton(self.top)
        self.checkUX.place(relx=0.529, rely=0.31, relheight=0.075
                , relwidth=0.053)
        self.checkUX.configure(activebackground="#d9d9d9")
        self.checkUX.configure(activeforeground="black")
        self.checkUX.configure(anchor='w')
        self.checkUX.configure(background="#d9d9d9")
        self.checkUX.configure(compound='left')
        self.checkUX.configure(disabledforeground="#a3a3a3")
        self.checkUX.configure(font="-family {Segoe UI} -size 10")
        self.checkUX.configure(foreground="#000000")
        self.checkUX.configure(highlightbackground="#d9d9d9")
        self.checkUX.configure(highlightcolor="#000000")
        self.checkUX.configure(justify='left')
        self.checkUX.configure(variable=self.cheUX)
        if(self.cheUX.get()): self.checkUX.select()

        self.checkUR = tk.Checkbutton(self.top)
        self.checkUR.place(relx=0.353, rely=0.31, relheight=0.075
                , relwidth=0.053)
        self.checkUR.configure(activebackground="#d9d9d9")
        self.checkUR.configure(activeforeground="black")
        self.checkUR.configure(anchor='w')
        self.checkUR.configure(background="#d9d9d9")
        self.checkUR.configure(compound='left')
        self.checkUR.configure(disabledforeground="#a3a3a3")
        self.checkUR.configure(font="-family {Segoe UI} -size 10")
        self.checkUR.configure(foreground="#000000")
        self.checkUR.configure(highlightbackground="#d9d9d9")
        self.checkUR.configure(highlightcolor="#000000")
        self.checkUR.configure(justify='left')
        self.checkUR.configure(variable=self.cheUR)
        if(self.cheUR.get()): self.checkUR.select()
        
        self.textUser = tk.Label(self.top)
        self.textUser.place(relx=0.059, rely=0.31, height=24, width=48)
        self.textUser.configure(activebackground="#d9d9d9")
        self.textUser.configure(activeforeground="black")
        self.textUser.configure(anchor='w')
        self.textUser.configure(background="#d9d9d9")
        self.textUser.configure(compound='left')
        self.textUser.configure(disabledforeground="#a3a3a3")
        self.textUser.configure(font="-family {Comic Sans MS} -size 11 -slant italic")
        self.textUser.configure(foreground="#000000")
        self.textUser.configure(highlightbackground="#d9d9d9")
        self.textUser.configure(highlightcolor="#000000")
        self.textUser.configure(text='''User''')

        self.labR = tk.Label(self.top)
        self.labR.place(relx=0.353, rely=0.177, height=24, width=21)
        self.labR.configure(activebackground="#d9d9d9")
        self.labR.configure(activeforeground="black")
        self.labR.configure(anchor='w')
        self.labR.configure(background="#d9d9d9")
        self.labR.configure(compound='left')
        self.labR.configure(disabledforeground="#a3a3a3")
        self.labR.configure(font="-family {Comic Sans MS} -size 12 -weight bold -slant italic")
        self.labR.configure(foreground="#000000")
        self.labR.configure(highlightbackground="#d9d9d9")
        self.labR.configure(highlightcolor="#000000")
        self.labR.configure(text='''R''')

        self.labW = tk.Label(self.top)
        self.labW.place(relx=0.441, rely=0.177, height=24, width=31)
        self.labW.configure(activebackground="#d9d9d9")
        self.labW.configure(activeforeground="black")
        self.labW.configure(anchor='w')
        self.labW.configure(background="#d9d9d9")
        self.labW.configure(compound='left')
        self.labW.configure(disabledforeground="#a3a3a3")
        self.labW.configure(font="-family {Comic Sans MS} -size 12 -weight bold -slant italic")
        self.labW.configure(foreground="#000000")
        self.labW.configure(highlightbackground="#d9d9d9")
        self.labW.configure(highlightcolor="#000000")
        self.labW.configure(text='''W''')

        self.labX = tk.Label(self.top)
        self.labX.place(relx=0.529, rely=0.177, height=24, width=21)
        self.labX.configure(activebackground="#d9d9d9")
        self.labX.configure(activeforeground="black")
        self.labX.configure(anchor='w')
        self.labX.configure(background="#d9d9d9")
        self.labX.configure(compound='left')
        self.labX.configure(disabledforeground="#a3a3a3")
        self.labX.configure(font="-family {Comic Sans MS} -size 12 -weight bold -slant italic")
        self.labX.configure(foreground="#000000")
        self.labX.configure(highlightbackground="#d9d9d9")
        self.labX.configure(highlightcolor="#000000")
        self.labX.configure(text='''X''')

        self.labelP_1 = tk.Label(self.top)
        self.labelP_1.place(relx=0.324, rely=0.044, height=14, width=97)
        self.labelP_1.configure(activebackground="#d9d9d9")
        self.labelP_1.configure(activeforeground="black")
        self.labelP_1.configure(anchor='w')
        self.labelP_1.configure(background="#d9d9d9")
        self.labelP_1.configure(compound='left')
        self.labelP_1.configure(disabledforeground="#a3a3a3")
        self.labelP_1.configure(font="-family {Comic Sans MS} -size 11 -weight bold")
        self.labelP_1.configure(foreground="#000000")
        self.labelP_1.configure(highlightbackground="#d9d9d9")
        self.labelP_1.configure(highlightcolor="#000000")
        self.labelP_1.configure(text='''Create Mask''')

        self.cancelUM = tk.Button(self.top)
        self.cancelUM.place(relx=0.559, rely=0.796, height=26, width=57)
        self.cancelUM.configure(activebackground="#d9d9d9")
        self.cancelUM.configure(activeforeground="black")
        self.cancelUM.configure(background="#d9d9d9")
        self.cancelUM.configure(disabledforeground="#a3a3a3")
        self.cancelUM.configure(font="-family {Comic Sans MS} -size 9")
        self.cancelUM.configure(foreground="#000000")
        self.cancelUM.configure(highlightbackground="#d9d9d9")
        self.cancelUM.configure(highlightcolor="#000000")
        self.cancelUM.configure(text='''Cancelar''')
        self.cancelUM.configure(command=self.top.destroy)
            
        self.acceptUM = tk.Button(self.top)
        self.acceptUM.place(relx=0.794, rely=0.796, height=26, width=57)
        self.acceptUM.configure(activebackground="#d9d9d9")
        self.acceptUM.configure(activeforeground="black")
        self.acceptUM.configure(background="#b3af46")
        self.acceptUM.configure(disabledforeground="#a3a3a3")
        self.acceptUM.configure(font="-family {Comic Sans MS} -size 9")
        self.acceptUM.configure(foreground="#000000")
        self.acceptUM.configure(highlightbackground="#d9d9d9")
        self.acceptUM.configure(highlightcolor="#000000")
        self.acceptUM.configure(text='''Aceptar''')
        self.acceptUM.configure(command=lambda: updateMask(self))
    

def start_up_windows(parent=None,navigate_callback=None, update_resource_callback=None):
    _w1 = Toplevel1(parent,navigate_callback,update_resource_callback)

if __name__ == '__main__':
    start_up_windows()