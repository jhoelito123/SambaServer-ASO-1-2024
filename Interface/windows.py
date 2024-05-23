import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *
import os.path

_location = os.path.dirname(__file__)

_bgcolor = '#d9d9d9'
_fgcolor = '#feffda'
title_config = {
    "background": _bgcolor,
    "font": ("Courier New", 12, "bold"),
    "foreground": "black",
    "anchor": "w",
}
miniButton = {
    "activebackground": _fgcolor,
    "background":'#b3af46',
    "font": ("Comic Sans MS", 9),
    "foreground": "black",
    "anchor": "center",
}

allElements = []
nameResource = ""
resourceStatic = [
] 

resourceConfig = {
}

class Toplevel1:
    def __init__(self, top=None, resource=None, navigate_callback=None, update_resource_callback=None):
        #VENTANA DE ESTA INTERFAZ
        top.geometry("667x528+564+92")
        top.minsize(120, 1)
        top.maxsize(1924, 1061)
        top.resizable(1,  1)
        top.title("Editar Recurso")
        top.configure(background="#d9d9d9")

        global resourceStatic, resourceConfig, allElements
        self.resource = resource  #recurso pasado
        self.top = top
        self.navigate_callback = navigate_callback
        self.update_resource_callback = update_resource_callback
        resourceStatic = self.resource.copy()
        resourceConfig = self.resource
        allElements = list(resource.keys()) #obtenemos todas las llaves del diccionario
        
        print("el recurso pasado es: ", resource)
        
        self.labelTextTitle = tk.Label(self.top)
        self.labelTextTitle.place(relx=0.25, rely=0.0, height=25, width=205)
        self.labelTextTitle.configure(**title_config)
        self.labelTextTitle.configure(text='''Recurso compartido''')

        self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

        self.butonBack = tk.Button(self.top)
        self.butonBack.place(relx=0.75, rely=0.911, height=26, width=67)
        self.butonBack.configure(activebackground=_fgcolor, background=_bgcolor)
        self.butonBack.configure(font="-family {Consolas} -size 10")
        self.butonBack.configure(text='''Atrás''', command=self.revert_and_navigate)

        self.Listbox1 = tk.Listbox(self.top)
        self.Listbox1.place(relx=0.033, rely=0.068, relheight=0.506, relwidth=0.94)
        self.Listbox1.configure(background="white")
        self.Listbox1.configure(font="-family {Consolas} -size 12")
        self.Listbox1.configure(foreground="#000000")
        self.Listbox1.configure(selectbackground=_fgcolor)
        self.Listbox1.configure(selectforeground="black")
        self.Listbox1.insert(tk.END, "{:<20}{}".format("- -variable- -", "- -valor- -"))
        
        # Insertar los datos de resource en la Listbox
        updateListBox(self.Listbox1)
        
        self.nameResource = tk.Label(self.top)
        self.nameResource.place(relx=0.54, rely=0.0, height=25, width=271)
        self.nameResource.configure(**title_config)
        self.nameResource.configure(text=nameResource) #global variable dependiendo
                
        # Botones para agregar, editar y quitar    
        self.butonSave = tk.Button(self.top)
        self.butonSave.place(relx=0.87, rely=0.911, height=26, width=67)
        self.butonSave.configure(activebackground=_fgcolor, background="#b3af46")
        self.butonSave.configure(font="-family {Consolas} -size 10")
        self.butonSave.configure(text='''Aceptar''')
        self.butonSave.configure(command=self.save_and_navigate)

        self.botonAdd = tk.Button(self.top)
        self.botonAdd.place(relx=0.045, rely=0.587, height=26, width=67)
        self.botonAdd.configure(activebackground=_fgcolor, background=_bgcolor)
        self.botonAdd.configure(font="-family {Consolas} -size 10")
        self.botonAdd.configure(text='''Agregar''')

        self.botonEdit = tk.Button(self.top)
        self.botonEdit.place(relx=0.165, rely=0.587, height=26, width=57)
        self.botonEdit.configure(activebackground=_fgcolor, background=_bgcolor)
        self.botonEdit.configure(font="-family {Consolas} -size 10")
        self.botonEdit.configure(text='''Editar''')
        self.botonEdit.configure(command=lambda: analiceEdit(self.Listbox1,self))

        self.botonQuit = tk.Button(self.top)
        self.botonQuit.place(relx=0.27, rely=0.587, height=26, width=57)
        self.botonQuit.configure(activebackground=_fgcolor, background=_bgcolor)
        self.botonQuit.configure(font="-family {Consolas} -size 10")
        self.botonQuit.configure(text='''Quitar''', command=self.remove_selected)
    
    def save_and_navigate(self):
        # navegar de vuelta a la ventana anterior
        if self.navigate_callback:
            self.navigate_callback()
    
    def revert_and_navigate(self): 
        global resourceStatic, resourceConfig
        # Revertir los cambios copiando los valores de resourceStatic
        self.resource.clear()
        self.resource.update(resourceStatic)
        resourceConfig.clear()
        resourceConfig.update(resourceStatic)
        if self.navigate_callback:
            self.navigate_callback()
    
    def remove_selected(self):
        selected_index = self.Listbox1.curselection()
        if selected_index:
            selected_item_text = self.Listbox1.get(selected_index[0])
            variable = selected_item_text.split()[0]
            # Verificar si la clave está en la lista global
            if variable in allElements:
                self.Listbox1.delete(selected_index[0])
                del resourceConfig[variable]
                allElements.remove(variable)
                print(f"Se ha eliminado el elemento {variable} correctamente.")
            else:
                print(f"El elemento {variable} no se puede eliminar.")

        else:
            print("No se ha seleccionado ningún elemento para eliminar.")
        
def updateListBox(listbox):
    listbox.delete(0, tk.END)
    #for testing elements
    """listbox.insert(tk.END, "{:<20}{}".format("- -variable- -", "- -valor- -"))
    listbox.insert(tk.END, "{:<20}{}".format("createMask", 753))
    listbox.insert(tk.END, "{:<20}{}".format("readOnly", NO))
    listbox.insert(tk.END, "{:<20}{}".format("InheritAcls", YES))"""
    global nameResource
    for clave, valor in resourceConfig.items():
        if clave.lower() == "nombre":
            nameResource = valor
        else:
            listbox.insert(tk.END, "{:<20}{}".format(clave+":", valor))
                    
#EVENTOS DEL LOS BOTONES AGREGAR, EDITAR, QUITAR        
def analiceEdit(listbox,self):
    selected_index = listbox.curselection()
    if selected_index:
        selected_item_text = listbox.get(selected_index[0])
        item_text = selected_item_text.strip().split(":") ##Dividimos en 2 partes, la primero es la clave y la segunda el valor 
        variable = item_text[0]
                
        if variable == "comment":            
            current_comment = item_text[1].strip()  # Obtener el comentario actual
            self.edit_comment_window = tk.Toplevel(self.top)
            top_comment_instance = topComment(self.edit_comment_window, initial_comment=current_comment, listbox=listbox)
            print("Editar comentario")
        elif variable == "path":
            current_path = item_text[1].strip()
            self.edit_path_window = tk.Toplevel(self.top)
            top_path_instance = topPath(self.edit_path_window,initial_path = current_path, listbox=listbox)
            print("Editar ruta")
        elif variable == 'read only':
            current_ro = item_text[1].strip()
            self.edit_ro = tk.Toplevel(self.top)
            top_ro_instance = topRO(self.edit_ro,initial_ro=current_ro, listbox=listbox)
            print("Editar permisos de lectura/escritura")
        elif variable == 'inherit acls':
            current_inherit = item_text[1].strip()
            self.edit_Inherit = tk.Toplevel(self.top)
            top_inherit_instance = topInherit(self.edit_Inherit,initial_Inherit=current_inherit, listbox=listbox)
            print("Editar inherit")
        elif variable == "create mask":
            print("Editar otra la mask")
            currentMask = item_text[1].strip()
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
        top.configure(background=_bgcolor)

        self.top = top
        self.listbox=listbox
        self.che51 = tk.BooleanVar(value=True if initial_ro=='Yes' else False)

        def update_RO(self):
                if self.che51.get():
                        ro_status = "Yes"
                else:
                        ro_status = "No"
                # Aquí puedes agregar la lógica para guardar el estado actualizado
                print("Read Only actualizado:", ro_status)
                resourceConfig['read only'] = ro_status
                updateListBox(self.listbox)
                self.top.destroy()
        
        self.checkReadOnly = tk.Checkbutton(self.top)
        self.checkReadOnly.place(relx=0.393, rely=0.319, relheight=0.198, relwidth=0.184)
        self.checkReadOnly.configure(activebackground=_bgcolor,background=_bgcolor)
        self.checkReadOnly.configure(anchor='w',compound='left',foreground="#000000")
        self.checkReadOnly.configure(font="-family {Comic Sans MS} -size 10 -slant italic")
        self.checkReadOnly.configure(justify='left',text='''YES''')
        self.checkReadOnly.configure(variable=self.che51)

        self.acceptRO = tk.Button(self.top)
        self.acceptRO.place(relx=0.785, rely=0.69, height=26, width=57)
        self.acceptRO.configure(**miniButton,text='''Aceptar''')
        self.acceptRO.configure(command=lambda: update_RO(self))

        self.cancelRO = tk.Button(self.top)
        self.cancelRO.place(relx=0.574, rely=0.69, height=26, width=63)
        self.cancelRO.configure(**miniButton,text='''Cancelar''')
        self.cancelRO.configure(background=_bgcolor)
        self.cancelRO.configure(command=self.top.destroy)

        self.labelRO = tk.Label(self.top)
        self.labelRO.place(relx=0.363, rely=0.078, height=20, width=94)
        self.labelRO.configure(**title_config,text='''Read Only?''')
        self.labelRO.configure(font="-family {Comic Sans MS} -size 11 -weight bold")

class topInherit:
    def __init__(self, top=None,initial_Inherit="", listbox=None):
        top.geometry("331x116+850+202")
        top.minsize(120, 1)
        top.maxsize(1924, 1061)
        top.resizable(1,  1)
        top.title("Inherit acls")
        top.configure(background=_bgcolor)

        self.top = top
        self.listbox=listbox
        self.che51 = tk.BooleanVar(value=True if initial_Inherit=='Yes' else False)

        def update_RO(self):
                if self.che51.get():
                        ro_status = "Yes"
                else:
                        ro_status = "No"
                # Aquí puedes agregar la lógica para guardar el estado actualizado
                print("Inherit ACL actualizado:", ro_status)
                resourceConfig['inherit acls'] = ro_status
                updateListBox(self.listbox)
                self.top.destroy()
        
        self.checkReadOnly = tk.Checkbutton(self.top)
        self.checkReadOnly.place(relx=0.393, rely=0.319, relheight=0.198, relwidth=0.184)
        self.checkReadOnly.configure(activebackground=_bgcolor,background=_bgcolor)
        self.checkReadOnly.configure(anchor='w',compound='left',foreground="#000000")
        self.checkReadOnly.configure(font="-family {Comic Sans MS} -size 10 -slant italic")
        self.checkReadOnly.configure(justify='left',text='''YES''')
        self.checkReadOnly.configure(variable=self.che51)

        self.acceptRO = tk.Button(self.top)
        self.acceptRO.place(relx=0.785, rely=0.69, height=26, width=57)
        self.acceptRO.configure(**miniButton,text='''Aceptar''')
        self.acceptRO.configure(command=lambda: update_RO(self))

        self.cancelRO = tk.Button(self.top)
        self.cancelRO.place(relx=0.574, rely=0.69, height=26, width=63)
        self.cancelRO.configure(**miniButton,text='''Cancelar''')
        self.cancelRO.configure(background=_bgcolor)
        self.cancelRO.configure(command=self.top.destroy)

        self.labelRO = tk.Label(self.top)
        self.labelRO.place(relx=0.363, rely=0.078, height=20, width=114)
        self.labelRO.configure(**title_config,text='''Inherit acls?''')
        self.labelRO.configure(font="-family {Comic Sans MS} -size 11 -weight bold")

class topComment:
    def __init__(self, top=None, initial_comment="", listbox=None):
        screen_width = top.winfo_screenwidth()
        screen_height = top.winfo_screenheight()
        x = (screen_width - 250) // 2  # El ancho de la ventana es 250
        y = (screen_height - 116) // 2  # La altura de la ventana es 116

        top.geometry(f"250x116+{x}+{y}")
        top.minsize(120, 1)
        top.maxsize(1924, 1061)
        top.resizable(1,  1)
        top.title("Comment")
        top.configure(background="#d9d9d9")

        self.top = top
        self.listbox = listbox
        
        def update_comment(self):
                new_comment = self.entryComment.get()
                # Aquí puedes agregar la lógica para guardar el comentario actualizado
                print("Comentario actualizado:", new_comment)
                resourceConfig['comment'] = new_comment
                updateListBox(self.listbox)
                self.top.destroy()
        
        self.entryComment = tk.Entry(top)
        self.entryComment.place(relx=0.12, rely=0.345, height=20, relwidth=0.776)
        self.entryComment.insert(0, initial_comment)

        self.entryComment.configure(background="white")
        self.entryComment.configure(font="-family {Comic Sans MS} -size 10 -slant italic")
        self.entryComment.configure(foreground="#000000")
        self.entryComment.configure(insertbackground="#000000")
        self.entryComment.configure(selectbackground="#d9d9d9")

        self.labelComment = tk.Label(self.top)
        self.labelComment.place(relx=0.36, rely=0.086, height=20, width=74)
        self.labelComment.configure(**title_config,text='''Comment''')
        self.labelComment.configure(font="-family {Comic Sans MS} -size 11 -weight bold")

        self.acceptComment = tk.Button(self.top)
        self.acceptComment.place(relx=0.68, rely=0.69, height=26, width=57)
        self.acceptComment.configure(**miniButton,text='''Aceptar''')
        self.acceptComment.configure(command=lambda: update_comment(self))
        
        self.cancelComment = tk.Button(self.top)
        self.cancelComment.place(relx=0.4, rely=0.69, height=26, width=63)
        self.cancelComment.configure(**miniButton,text='''Cancelar''')
        self.cancelComment.configure(background=_bgcolor)
        self.cancelComment.configure(command=self.top.destroy)

class topPath:
    def __init__(self, top=None,initial_path="", listbox=None):
        top.geometry("241x116+312+348")
        top.minsize(120, 1)
        top.maxsize(1924, 1061)
        top.resizable(1,  1)
        top.title("Define Path")
        top.configure(background=_bgcolor)
        self.top = top
        self.listbox = listbox

        def update_path(self):
            new_path = self.entryPath.get()
            # Aquí puedes agregar la lógica para guardar el comentario actualizado
            print("Comentario actualizado:", new_path)
            resourceConfig['path'] = new_path
            updateListBox(self.listbox)
            self.top.destroy()
        
        self.acceptPath = tk.Button(self.top)
        self.acceptPath.place(relx=0.68, rely=0.69, height=26, width=57)
        self.acceptPath.configure(**miniButton,text='''Aceptar''')
        self.acceptPath.configure(command=lambda: update_path(self))

        self.entryPath = tk.Entry(self.top)
        self.entryPath.place(relx=0.083, rely=0.345, height=20, relwidth=0.805)
        self.entryPath.configure(background="white")
        self.entryPath.configure(font="-family {Comic Sans MS} -size 10 -slant italic")
        self.entryPath.configure(foreground="#000000")
        self.entryPath.configure(insertbackground="#000000")
        self.entryPath.configure(selectbackground="#d9d9d9")
        self.entryPath.insert(0, initial_path)

        self.cancelPath = tk.Button(self.top)
        self.cancelPath.place(relx=0.398, rely=0.69, height=26, width=57)
        self.cancelPath.configure(**miniButton,text='''Cancelar''')
        self.cancelPath.configure(background="#d9d9d9")
        self.cancelPath.configure(command=top.destroy)

        self.labelP = tk.Label(self.top)
        self.labelP.place(relx=0.415, rely=0.086, height=20, width=42)
        self.labelP.configure(**title_config,text='''Path''')
        self.labelP.configure(font="-family {Comic Sans MS} -size 11 -weight bold")

class topUmask:
    def __init__(self, top=None,initialMask="", listbox=None):
        firstDigit = int(int(initialMask) /100)
        secondDigit = int((int(initialMask) / 10)%10)
        threeDigit = int(int(initialMask)%10) 
        top.geometry("340x226+312+348")
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
                        
            resourceConfig["create mask"] = f'0{firstDigit}{secondDigit}{threeDigit}'
            
            updateListBox(self.listbox)
            self.top.destroy()

        self.textGroup = tk.Label(self.top)
        self.textGroup.place(relx=0.059, rely=0.442, height=24, width=47)
        self.textGroup.configure(**title_config,text='''Group''')
        self.textGroup.configure(font="-family {Comic Sans MS} -size 11 -slant italic")

        self.textOthers = tk.Label(self.top)
        self.textOthers.place(relx=0.059, rely=0.575, height=24, width=47)
        self.textOthers.configure(**title_config,text='''Others''')
        self.textOthers.configure(font="-family {Comic Sans MS} -size 11 -slant italic")

        self.checkOR = tk.Checkbutton(self.top)
        self.checkOR.place(relx=0.353, rely=0.575, relheight=0.075 , relwidth=0.053)
        self.checkOR.configure(activebackground="#d9d9d9")
        self.checkOR.configure(background="#d9d9d9",anchor='w')
        self.checkOR.configure(compound='left')
        self.checkOR.configure(font="-family {Segoe UI} -size 10")
        self.checkOR.configure(foreground="#000000")
        self.checkOR.configure(justify='left')
        self.checkOR.configure(variable=self.cheOR)
        if(self.cheOR.get()): self.checkOR.select()

        self.checkOW = tk.Checkbutton(self.top)
        self.checkOW.place(relx=0.441, rely=0.575, relheight=0.075 , relwidth=0.053)
        self.checkOW.configure(activebackground="#d9d9d9",compound='left')
        self.checkOW.configure(background="#d9d9d9",anchor='w')
        self.checkOW.configure(font="-family {Segoe UI} -size 10")
        self.checkOW.configure(foreground="#000000",justify='left')
        self.checkOW.configure(variable=self.cheOW)
        if(self.cheOW.get()): self.checkOW.select()

        self.checkOX = tk.Checkbutton(self.top)
        self.checkOX.place(relx=0.529, rely=0.575, relheight=0.075 , relwidth=0.053)
        self.checkOX.configure(activebackground="#d9d9d9",compound='left')
        self.checkOX.configure(background="#d9d9d9",anchor='w')
        self.checkOX.configure(font="-family {Segoe UI} -size 10")
        self.checkOX.configure(foreground="#000000",justify='left')
        self.checkOX.configure(variable=self.cheOX)
        self.checkOX.configure(command= lambda: print(self.cheOX.get()))
        if(self.cheOX.get()): self.checkOX.select()
        

        self.checkGR = tk.Checkbutton(self.top)
        self.checkGR.place(relx=0.353, rely=0.442, relheight=0.075, relwidth=0.053)
        self.checkGR.configure(activebackground="#d9d9d9",anchor='w',background="#d9d9d9")
        self.checkGR.configure(compound='left',foreground="#000000",justify='left')
        self.checkGR.configure(font="-family {Segoe UI} -size 10")
        self.checkGR.configure(variable=self.cheGR)
        if(self.cheGR.get()): self.checkGR.select()

        self.checkGW = tk.Checkbutton(self.top)
        self.checkGW.place(relx=0.441, rely=0.442, relheight=0.075  , relwidth=0.053)
        self.checkGW.configure(activebackground="#d9d9d9", anchor='w',background="#d9d9d9")
        self.checkGW.configure(compound='left',foreground="#000000",justify='left')
        self.checkGW.configure(font="-family {Segoe UI} -size 10")
        self.checkGW.configure(variable=self.cheGW)
        if(self.cheGW.get()): self.checkGW.select()

        self.checkGX = tk.Checkbutton(self.top)
        self.checkGX.place(relx=0.529, rely=0.442, relheight=0.075, relwidth=0.053)
        self.checkGX.configure(activebackground="#d9d9d9",background="#d9d9d9",anchor='w')
        self.checkGX.configure(compound='left',foreground="#000000",justify='left')
        self.checkGX.configure(font="-family {Segoe UI} -size 10")
        self.checkGX.configure(variable=self.cheGX)
        if(self.cheGW.get()): self.checkGW.select()

        self.checkUW = tk.Checkbutton(self.top)
        self.checkUW.place(relx=0.441, rely=0.31, relheight=0.075 , relwidth=0.053)
        self.checkUW.configure(activebackground="#d9d9d9",background="#d9d9d9",anchor='w')
        self.checkUW.configure(compound='left',foreground="#000000",justify='left')
        self.checkUW.configure(font="-family {Segoe UI} -size 10")
        self.checkUW.configure(variable=self.cheUW)
        if(self.cheUW.get()): self.checkUW.select()

        self.checkUX = tk.Checkbutton(self.top)
        self.checkUX.place(relx=0.529, rely=0.31, relheight=0.075 , relwidth=0.053)
        self.checkUX.configure(activebackground="#d9d9d9",anchor='w',background="#d9d9d9")
        self.checkUX.configure(compound='left',foreground="#000000",justify='left')
        self.checkUX.configure(font="-family {Segoe UI} -size 10")
        self.checkUX.configure(variable=self.cheUX)
        if(self.cheUX.get()): self.checkUX.select()

        self.checkUR = tk.Checkbutton(self.top)
        self.checkUR.place(relx=0.353, rely=0.31, relheight=0.075   , relwidth=0.053)
        self.checkUR.configure(activebackground="#d9d9d9",anchor='w',background="#d9d9d9")
        self.checkUR.configure(compound='left',foreground="#000000",justify='left')
        self.checkUR.configure(font="-family {Segoe UI} -size 10")
        self.checkUR.configure(variable=self.cheUR)
        if(self.cheUR.get()): self.checkUR.select()
        
        self.textUser = tk.Label(self.top)
        self.textUser.place(relx=0.059, rely=0.31, height=24, width=48)
        self.textUser.configure(**title_config,text='''User''')
        self.textUser.configure(font="-family {Comic Sans MS} -size 11 -slant italic")

        self.labR = tk.Label(self.top)
        self.labR.place(relx=0.353, rely=0.177, height=24, width=21)
        self.labR.configure(**title_config,text='''R''')
        self.labR.configure(font="-family {Comic Sans MS} -size 12 -weight bold -slant italic")

        self.labW = tk.Label(self.top)
        self.labW.place(relx=0.441, rely=0.177, height=24, width=31)
        self.labW.configure(**title_config,text='''W''')
        self.labW.configure(font="-family {Comic Sans MS} -size 12 -weight bold -slant italic")

        self.labX = tk.Label(self.top)
        self.labX.place(relx=0.529, rely=0.177, height=24, width=21)
        self.labX.configure(**title_config,text='''X''')
        self.labX.configure(font="-family {Comic Sans MS} -size 12 -weight bold -slant italic")
        
        self.labelP_1 = tk.Label(self.top)
        self.labelP_1.place(relx=0.324, rely=0.044, height=14, width=97)
        self.labelP_1.configure(**title_config,text='''Create Mask''')
        self.labelP_1.configure(font="-family {Comic Sans MS} -size 11 -weight bold")

        self.cancelUM = tk.Button(self.top)
        self.cancelUM.place(relx=0.559, rely=0.796, height=26, width=57)
        self.cancelUM.configure(**miniButton,text='''Cancelar''')
        self.cancelUM.configure(background="#d9d9d9",command=self.top.destroy)
            
        self.acceptUM = tk.Button(self.top)
        self.acceptUM.place(relx=0.794, rely=0.796, height=26, width=57)
        self.acceptUM.configure(**miniButton,text='''Aceptar''')
        self.acceptUM.configure(command=lambda: updateMask(self))
    

def start_up_windows(parent=None,navigate_callback=None, update_resource_callback=None):
    
    _w1 = Toplevel1(parent,navigate_callback,update_resource_callback)

if __name__ == '__main__':
    start_up_windows()