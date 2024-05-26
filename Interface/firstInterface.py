import sys
import tkinter as tk
import tkinter.ttk as ttk
import subprocess
from tkinter.constants import *
import os.path
_location = os.path.dirname(__file__)
from tkinter import messagebox

colorDef = '#d9d9d9'
_fgcolor = '#feffda'
title_config = {
    "background": colorDef,
    "font": ("Courier New", 15, "bold"),
    "foreground": "black",
    "anchor": "w",
}

class Toplevel1:
    def __init__(self, top=None, navigate_callback=None,show_windows_callback=None):
        top.geometry("915x581+402+99")
        top.minsize(120, 1)
        top.maxsize(1924, 1061)
        top.resizable(1,  1)
        top.title("Configuración servicio Samba")
        top.configure(background=colorDef)

        self.top = top
        self.navigate_callback = navigate_callback
        self.show_windows_callback = show_windows_callback
        
        self.che63 = tk.IntVar()
        self.che69 = tk.IntVar()
        self.che64 = tk.IntVar()

        self.menubar = tk.Menu(top,font="-family {Consolas}",bg=_fgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

        self.navigator = ttk.Notebook(self.top)
        self.navigator.place(relx=0.017, rely=0.022, relheight=0.852, relwidth=0.953)
        self.navigator_t1 = tk.Frame(self.navigator)
        self.navigator.add(self.navigator_t1, padding=3)
        self.navigator.tab(0, text='''Inicio''', compound="left",underline='''-1''', )
        self.navigator_t1.configure(borderwidth="5")
        self.navigator_t1.configure(background=colorDef)
        self.navigator_t2 = tk.Frame(self.navigator)
        self.navigator.add(self.navigator_t2, padding=3)
        self.navigator.tab(1, text='''Recursos compartidos''', compound="left" ,underline='''-1''', )
        self.navigator_t2.configure(background=colorDef)
        self.navigator_t3 = tk.Frame(self.navigator)
        self.navigator.add(self.navigator_t3, padding=3)
        self.navigator.tab(2, text='''Identidad''', compound="left",underline='''-1''', )
        self.navigator_t3.configure(background=colorDef)
        self.navigator_t4 = tk.Frame(self.navigator)
        self.navigator.add(self.navigator_t4, padding=3)
        self.navigator.tab(3, text='''Usuarios''', compound="left" ,underline='''-1''', )
        self.navigator_t4.configure(background=colorDef)
#========================================================
        #for new navigator Users
        self.labelUsers = tk.Label(self.navigator_t4)
        self.labelUsers.place(relx=0.046, rely=0.02, height=31, width=294)
        self.labelUsers.configure(**title_config)
        self.labelUsers.configure(text='''Usuarios Registrados''')

        self.listUsers = tk.Listbox(self.navigator_t4)
        self.listUsers.place(relx=0.031, rely=0.099, relheight=0.675, relwidth=0.47)
        self.listUsers.configure(background="white")
        self.listUsers.configure(font="TkFixedFont")
        self.listUsers.configure(foreground="#000000")
        self.listUsers.configure(selectbackground="#feffda")
        self.listUsers.configure(selectforeground="black")
        self.listUsers.bind("<ButtonRelease-1>", lambda event: self.listar_usuarios_samba())

        self.butModUser = tk.Button(self.navigator_t4)
        self.butModUser.place(relx=0.526, rely=0.296, height=26, width=167)
        self.butModUser.configure(**title_config,activebackground=_fgcolor)
        self.butModUser.configure(font="-family {Consolas} -size 10")
        self.butModUser.configure(text='''Agregar usuario''',anchor='center')
        self.butModUser.configure(command=self.add_user)
        self.listar_usuarios_samba()
        

        self.buttDelUser = tk.Button(self.navigator_t4)
        self.buttDelUser.place(relx=0.526, rely=0.375, height=26, width=167)
        self.buttDelUser.configure(**title_config,activebackground=_fgcolor)
        self.buttDelUser.configure(font="-family {Consolas} -size 10")
        self.buttDelUser.configure(text='''Eliminar usuario''',anchor='center')
        self.buttDelUser.configure(command=self.delete_samba_user)
        
        self.cuadroInicial = tk.Frame(self.navigator_t1)
        self.cuadroInicial.place(relx=0.011, rely=0.04, relheight=0.51, relwidth=0.97)
        self.cuadroInicial.configure(relief='groove',borderwidth="2",background=colorDef)

        self.textEstado = tk.Label(self.cuadroInicial)
        self.textEstado.place(relx=0.023, rely=0.163, height=21, width=150)
        self.textEstado.configure(**title_config)
        self.textEstado.configure(font="-family {Courier New} -size 12 -weight bold")
        self.textEstado.configure(text='''Estado actual:''')

        self.statusService = tk.Label(self.cuadroInicial)
        self.statusService.place(relx=0.219, rely=0.154, height=21, width=82)
        self.statusService.configure(**title_config)
        self.statusService.configure(font="-family {Consolas} -size 11")
        self.statusService.configure(text='''Inactivo''')

        self.textLaterConfig = tk.Label(self.cuadroInicial)
        self.textLaterConfig.place(relx=0.023, rely=0.246, height=20, width=220)
        self.textLaterConfig.configure(**title_config)
        self.textLaterConfig.configure(font="-family {Courier New} -size 12 -weight bold")
        self.textLaterConfig.configure(text='''Después de configurar:''')

        self.selected_option = tk.StringVar(self.cuadroInicial)
        self.selected_option.set("Seleccione una opción")  # Establece un valor predeterminado

        options = ["Reiniciar Servicio", "Detener", "Mantener estado actual", "Bloque 4"]

        self.estadoActual = tk.OptionMenu(self.cuadroInicial, self.selected_option, *options)
        self.estadoActual.place(relx=0.046, rely=0.338, relheight=0.092, relwidth=0.23)
        self.estadoActual.configure(font="-family {Consolas} -size 10")


        self.startServiceCheck = tk.Checkbutton(self.cuadroInicial)
        self.startServiceCheck.place(relx=0.046, rely=0.521, relheight=0.096, relwidth=0.105)
        self.startServiceCheck.configure(**title_config, activebackground="#d9d9d9")
        self.startServiceCheck.configure(font="-family {Consolas} -size 10")
        self.startServiceCheck.configure(text='''¿Iniciar?''')
        self.startServiceCheck.configure(variable=self.che69)

        self.Label1 = tk.Label(self.cuadroInicial)
        self.Label1.place(relx=0.023, rely=0.45, height=18, width=209)
        self.Label1.configure(**title_config)
        self.Label1.configure(font="-family {Courier New} -size 12 -weight bold")
        self.Label1.configure(text='''Después de reiniciar:''')

        self.tituloInicio = tk.Label(self.cuadroInicial)
        self.tituloInicio.place(relx=0.313, rely=0.042, height=21, width=316)
        self.tituloInicio.configure(**title_config)
        self.tituloInicio.configure(text='''Configuración del Servicio''')

        self.botonAdd = tk.Button(self.navigator_t2)
        self.botonAdd.place(relx=0.023, rely=0.433, height=26, width=57)
        self.botonAdd.configure(**title_config,activebackground=_fgcolor)
        self.botonAdd.configure(font="-family {Consolas} -size 10")
        self.botonAdd.configure(text='''Agregar''',anchor='center')
        self.botonAdd.configure(command=lambda: open_new_resource_window(self))
        
        def open_new_resource_window(self):
            new_window = tk.Toplevel(self.top)
            new_resource_window = newResource(top=new_window, parent=self)

        self.listActual = ScrolledListBox(self.navigator_t2)
        self.listActual.place(relx=0.023, rely=0.062, relheight=0.348, relwidth=0.938)
        self.listActual.configure(background="white")
        self.listActual.configure(cursor="xterm")
        self.listActual.configure(font="TkFixedFont")
        self.listActual.configure(foreground="black")
        self.listActual.configure(selectbackground="#feffda")
        self.listActual.configure(selectforeground="black")
        load_shared_resources(self.listActual)
        
        self.botonEdit = tk.Button(self.navigator_t2)
        self.botonEdit.place(relx=0.101, rely=0.433, height=26, width=57)
        self.botonEdit.configure(**title_config,activebackground=_fgcolor)
        self.botonEdit.configure(font="-family {Consolas} -size 10")
        self.botonEdit.configure(text='''Editar''',anchor="center")
        self.botonEdit.configure(command=lambda: edit(self, self.show_windows_callback))

        self.botonDel = tk.Button(self.navigator_t2)
        self.botonDel.place(relx=0.18, rely=0.433, height=26, width=57)
        self.botonDel.configure(**title_config, activebackground=_fgcolor)
        self.botonDel.configure(font="-family {Consolas} -size 10")
        self.botonDel.configure(text='''Quitar''',anchor='center')
        self.botonDel.configure(command=self.remove_selected_item)

        self.Label2 = tk.Label(self.navigator_t2)
        self.Label2.place(relx=0.023, rely=0.021, height=18, width=248)
        self.Label2.configure(**title_config)
        self.Label2.configure(text='''Recursos compartidos''')       
        
        self.frameWorkGroup = tk.Frame(self.navigator_t3)
        self.frameWorkGroup.place(relx=0.022, rely=0.102, relheight=0.399, relwidth=0.926)
        self.frameWorkGroup.configure(relief='groove',borderwidth="2",background=colorDef)

        self.labelWorkgroup = tk.Label(self.frameWorkGroup)
        self.labelWorkgroup.place(relx=0.012, rely=0.053, height=20, width=209)
        self.labelWorkgroup.configure(**title_config)
        self.labelWorkgroup.configure(font="-family {Consolas} -size 11")
        self.labelWorkgroup.configure(text='''Nombre de WorkGroup:''')
        
        self.buttonOK = tk.Button(self.frameWorkGroup, text="OK")
        self.buttonOK.place(relx=0.474, rely=0.186, height=20, width=57)
        self.buttonOK.configure(activebackground=_fgcolor,font="-family {Consolas} -size 11")
        self.buttonOK.configure(background="#d9d9d9", foreground="#000000", command=self.update_workgroup)

        self.entryWorkGroup = tk.Entry(self.frameWorkGroup)
        self.entryWorkGroup.place(relx=0.012, rely=0.186, height=20 , relwidth=0.452)
        self.entryWorkGroup.configure(background="white")
        self.entryWorkGroup.configure(font="-family {Consolas} -size 11")
        self.entryWorkGroup.configure(foreground="#000000",insertbackground="#000000")
        self.entryWorkGroup.configure(selectbackground="#d9d9d9", selectforeground="black")

        self.fill_entry_with_current_workgroup()
        
        self.Label3 = tk.Label(self.navigator_t3)
        self.Label3.place(relx=0.348, rely=0.04, height=21, width=248)
        self.Label3.configure(**title_config)
        self.Label3.configure(text='''Configuración básica''')

        self.botonCancel = tk.Button(self.top)
        self.botonCancel.place(relx=0.812, rely=0.905, height=26, width=67)
        self.botonCancel.configure(**title_config,activebackground=_fgcolor)
        self.botonCancel.configure(font="-family {Consolas} -size 10")
        self.botonCancel.configure(text='''Cancelar''',anchor='center')
        self.botonCancel.configure(command=self.cancel_and_navigate)

        self.botonAccept = tk.Button(self.top)
        self.botonAccept.place(relx=0.897, rely=0.905, height=26, width=67)
        self.botonAccept.configure(**title_config)
        self.botonAccept.configure(activebackground=_fgcolor,background="#b3af46")
        self.botonAccept.configure(font="-family {Consolas} -size 10")
        self.botonAccept.configure(text='''Aceptar''',anchor='center',command=self.save_changes)
        
    """ def add_user(self):
        add_user_dialog = AddUserDialog(self.root, self.listUsers) """
     
    def add_user(self):
        username = self.username_entry.get().strip()
        password = self.password_entry.get().strip()
        password_confirm = self.password_confirm_entry.get().strip()
        if not username or not password or not password_confirm:
            messagebox.showwarning("Advertencia", "Por favor, complete todos los campos.")
            return
        if password != password_confirm:
            messagebox.showwarning("Advertencia", "Las contraseñas no coinciden.")
            return
        try:
            # Comando para agregar usuario al sistema con directorio home
            subprocess.run(['sudo', 'useradd', '-d', f'/home/{username}', '-m', username], check=True)
            # Establecer la contraseña del usuario del sistema
            proc_passwd = subprocess.Popen(['sudo', 'passwd', username], stdin=subprocess.PIPE, stderr=subprocess.PIPE)
            proc_passwd.communicate(input=f'{password}\n{password}\n'.encode())
            if proc_passwd.returncode != 0:
                raise subprocess.CalledProcessError(proc_passwd.returncode, 'passwd')
            # Comando para agregar usuario a Samba
            proc_smbpasswd = subprocess.Popen(['sudo', 'smbpasswd', '-a', username], stdin=subprocess.PIPE, stderr=subprocess.PIPE)
            proc_smbpasswd.communicate(input=f'{password}\n{password}\n'.encode())
            if proc_smbpasswd.returncode == 0:
                messagebox.showinfo("Éxito", f"Usuario {username} agregado con éxito.")
            else:
                raise subprocess.CalledProcessError(proc_smbpasswd.returncode, 'smbpasswd')
        except subprocess.CalledProcessError as e:
            messagebox.showerror("Error", f"No se pudo agregar el usuario {username}. Error: {e}")
     
                
    def delete_user(self):
        username = self.del_username_entry.get().strip()
        if not username:
            messagebox.showwarning("Advertencia", "Por favor, complete el campo de nombre de usuario.")
            return
        try:
            # Comando para eliminar usuario de Samba
            process = subprocess.Popen(['sudo', 'smbpasswd', '-x', username], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            _, error = process.communicate()
            if process.returncode == 0:
                messagebox.showinfo("Éxito", f"Usuario {username} eliminado con éxito.")
            else:
                messagebox.showerror("Error", f"No se pudo eliminar el usuario {username}. Error: {error.decode()}")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo eliminar el usuario {username}. Error: {e}")
            
    def list_users(self):
        try:
            process = subprocess.Popen(['sudo', 'pdbedit', '-L'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            output, _ = process.communicate()
            if process.returncode == 0:
                users = output.decode().strip().split('\n')
                self.users_listbox.delete(0, tk.END)
                for user in users:
                    self.users_listbox.insert(tk.END, user)
            else:
                messagebox.showerror("Error", "No se pudieron listar los usuarios.")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudieron listar los usuarios. Error: {e}")



    
    def cancel_and_navigate(self):
        self.cancel_changes()
        self.navigate_callback()
    
    def add_new_resource(self, resource):
            formatted_line = "{:<20} {:<13} {:<27} {:<20}".format(
                resource["read only"],
                resource["Nombre"],
                resource["path"],
                resource["comment"]
            )
            self.listActual.insert(tk.END, formatted_line)
            # agregar el recurso a una lista global
            resources.append(resource)
    
    def remove_selected_item(self):
        selected_index = self.listActual.curselection()
        if selected_index:
            self.listActual.delete(selected_index)
            del resources[selected_index[0] + 1]
    
    def update_workgroup(self):
        # Obtener el valor actual del Entry
        new_workgroup = self.entryWorkGroup.get()
        for resource in resources:
            if resource['Nombre'] == 'global':
                resource['workgroup'] = new_workgroup
                break
        else:
            print("No se encontró el recurso global.")

    def fill_entry_with_current_workgroup(self):
        current_workgroup = None
        for resource in resources:
            if resource['Nombre'] == 'global':
                current_workgroup = resource.get('workgroup', '')
                break

        self.entryWorkGroup.delete(0, tk.END)  # Limpiar el Entry
        self.entryWorkGroup.insert(0, current_workgroup) #Llenarlo

    def save_changes(self):
        global resources,lines,initial_conf
        write_smb_conf(file_path,resources)
        #vuelve a leer para actualizarse
        lines = read_smb_conf(file_path)
        resources = extract_shared_resources(lines)
        initial_conf = extract_shared_resources(lines)
        load_shared_resources(self.listActual)
        messagebox.showinfo("Guardando...", "Los cambios se han guardado correctamente.")

    def cancel_changes(self):
        global resources,initial_conf
        resources = initial_conf
        messagebox.showinfo("Cancelando y saliendo...", "Los cambios han sido cancelados.")

def write_smb_conf(file_path, resources):
    with open(file_path, 'w') as file:
        file.write("# smb.conf is the main Samba configuration file. You find a full commented\n")
        file.write("# version at /usr/share/doc/packages/samba/examples/smb.conf.SUSE if the\n")
        file.write("# samba-doc package is installed.\n")
        
        for resource in resources:
            file.write(f"[{resource['Nombre']}]\n")
            for key, value in resource.items():
                if key != 'Nombre':
                    file.write(f"\t{key} = {value}\n")
   
class newResource:
    def __init__(self, top=None, parent=None):
        top.geometry("328x312+850+202")
        top.minsize(120, 1)
        top.maxsize(1924, 1061)
        top.resizable(1,  1)
        top.title("Add new Resource")
        top.configure(background="#d9d9d9")

        self.top = top
        self.parent = parent
        self.che67 = tk.IntVar()

        self.acceptNR = tk.Button(self.top)
        self.acceptNR.place(relx=0.762, rely=0.859, height=26, width=57)
        self.acceptNR.configure(activebackground=_fgcolor,background="#b3af46")
        self.acceptNR.configure(font="-family {Comic Sans MS} -size 9")
        self.acceptNR.configure(foreground="#000000",text='''Aceptar''',command=lambda: on_accept(self))
        
        self.cancelNR = tk.Button(self.top)
        self.cancelNR.place(relx=0.549, rely=0.859, height=26, width=57)
        self.cancelNR.configure(activebackground=_fgcolor,**title_config)
        self.cancelNR.configure(font="-family {Comic Sans MS} -size 9")
        self.cancelNR.configure(text='''Cancelar''',command=self.top.destroy)

        self.entryPathNR = tk.Entry(self.top)
        self.entryPathNR.place(relx=0.183, rely=0.628, height=20, relwidth=0.591)

        self.entryPathNR.configure(background="white",foreground="#000000")
        self.entryPathNR.configure(font="-family {Comic Sans MS} -size 10 -slant italic")
        self.entryPathNR.configure(insertbackground="#000000",selectbackground="#d9d9d9")

        self.labelPathNR = tk.Label(self.top)
        self.labelPathNR.place(relx=0.396, rely=0.529, height=24, width=42)
        self.labelPathNR.configure(anchor='w',background="#d9d9d9")
        self.labelPathNR.configure(compound='left',text='''Path''',foreground="#000000")
        self.labelPathNR.configure(font="-family {Comic Sans MS} -size 11 -weight bold")

        self.entryCommentNR = tk.Entry(self.top)
        self.entryCommentNR.place(relx=0.183, rely=0.429, height=20, relwidth=0.591)
        self.entryCommentNR.configure(background="white",foreground="#000000")
        self.entryCommentNR.configure(font="-family {Comic Sans MS} -size 10 -slant italic")
        self.entryCommentNR.configure(insertbackground="#000000",selectbackground="#d9d9d9")

        self.labelComment = tk.Label(self.top)
        self.labelComment.place(relx=0.366, rely=0.33, height=25, width=72)
        self.labelComment.configure(anchor='w',background="#d9d9d9",compound='left')
        self.labelComment.configure(font="-family {Comic Sans MS} -size 11 -weight bold")
        self.labelComment.configure(foreground="#000000",text='''Comment''')

        self.entryNameNR = tk.Entry(self.top)
        self.entryNameNR.place(relx=0.183, rely=0.231, height=20, relwidth=0.591)

        self.entryNameNR.configure(background="white",foreground="#000000")
        self.entryNameNR.configure(font="-family {Comic Sans MS} -size 10 -slant italic")
        self.entryNameNR.configure(insertbackground="#000000",selectbackground="#d9d9d9")

        self.labelNameNR = tk.Label(self.top)
        self.labelNameNR.place(relx=0.396, rely=0.163, height=14, width=52)
        self.labelNameNR.configure(anchor='w',background="#d9d9d9",compound='left')
        self.labelNameNR.configure(font="-family {Comic Sans MS} -size 11 -weight bold")
        self.labelNameNR.configure(foreground="#000000",text='''Name''')

        self.chechRO_NR = tk.Checkbutton(self.top)
        self.chechRO_NR.place(relx=0.305, rely=0.728, relheight=0.09, relwidth=0.338)
        self.chechRO_NR.configure(anchor='w',background="#d9d9d9",compound='left')
        self.chechRO_NR.configure(font="-family {Comic Sans MS} -size 11 -weight bold")
        self.chechRO_NR.configure(foreground="#000000",justify='left')
        self.chechRO_NR.configure(text='''Read Only''',variable=self.che67)

        self.labelNR = tk.Label(self.top)
        self.labelNR.place(relx=0.152, rely=0.032, height=25, width=224)
        self.labelNR.configure(anchor='w',background="#d9d9d9",compound='left')
        self.labelNR.configure(font="-family {Comic Sans MS} -size 13 -weight bold -slant italic")
        self.labelNR.configure(foreground="#000000",text='''Nuevo recurso compartido''')
        def on_accept(self):
            new_resource = {
                "Nombre": self.entryNameNR.get(),
                "path": self.entryPathNR.get(),
                "comment": self.entryCommentNR.get(),
                "read only": "Yes" if self.che67.get() else "No"
            }
            self.parent.add_new_resource(new_resource)
            self.top.destroy()

def read_smb_conf(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            lines = [line.strip() for line in lines]
        return lines
    except FileNotFoundError:
        print(f"Error: The file at {file_path} was not found.")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

def extract_shared_resources(lines):
    resources = []
    current_resource = {}
    for line in lines:
        line = line.strip()
        if line.startswith("[") and line.endswith("]"):
            if current_resource:
                resources.append(current_resource)
                current_resource = {}
            current_resource["Nombre"] = line[1:-1]
        elif "=" in line:
            key, value = line.split("=", 1)
            current_resource[key.strip()] = value.strip()
    if current_resource:
        resources.append(current_resource)
    return resources

file_path = "/etc/samba/smb.conf"
lines = read_smb_conf(file_path)
resources = extract_shared_resources(lines)
initial_conf = extract_shared_resources(lines) #rescatamos el original

def load_shared_resources(self):
            self.delete(0, tk.END)
            for resource in resources:
                nombre = resource.get("Nombre", "No especificado")
                if nombre.lower() == "global": #no deberia aparecer [global]
                    continue
                
                read_only = resource.get("read only", "No especificado")
                path = resource.get("path", "No especificado")
                comentario = resource.get("comment", "No especificado")
                
                formatted_line = "{:<20} {:<13} {:<27} {:<20}".format(
                    read_only,
                    nombre,
                    path,
                    comentario
                )
                self.insert(tk.END, formatted_line)

def edit(self, show_windows_callback):
    selected_index = self.listActual.curselection()
    if selected_index:
        index = selected_index[0]  # Obtener el índice del recurso seleccionado
        selected_resource = resources[index+1]  # Obtener el recurso completo usando el índice
        show_windows_callback(selected_resource)        

class AutoScroll(object):
    def __init__(self, master):
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
    def wrapped(cls, master, **kw):
        container = ttk.Frame(master)
        container.bind('<Enter>', lambda e: _bound_to_mousewheel(e, container))
        container.bind('<Leave>', lambda e: _unbound_to_mousewheel(e, container))
        return func(cls, container, **kw)
    return wrapped

class ScrolledListBox(AutoScroll, tk.Listbox):
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

def start_up_Interface(parent=None, navigate_callback=None, show_windows_callback=None):
    _w1 = Toplevel1(parent, navigate_callback, show_windows_callback)

if __name__ == '__main__':
    start_up_Interface()
""" 
import subprocess
import paramiko

class AddUserDialog:
    def __init__(self, parent, listbox):
        self.parent = parent
        self.listbox = listbox
        self.dialog = tk.Toplevel(parent)
        self.dialog.title("Agregar Usuario")
        self.dialog.geometry("300x250")
        self.dialog.configure(bg='grey')

        # Estilos
        label_bg_color = 'DarkOliveGreen1'
        label_fg_color = 'white'
        button_bg_color_accept = 'green'
        button_fg_color = 'white'
        button_bg_color_cancel = 'red'
        entry_bg_color = 'white'
        entry_fg_color = 'black'

        # Labels
        tk.Label(self.dialog, text="Nombre de usuario:", bg=label_bg_color, fg=label_fg_color).pack(pady=5)
        self.username_entry = tk.Entry(self.dialog, bg=entry_bg_color, fg=entry_fg_color)
        self.username_entry.pack(pady=5)

        tk.Label(self.dialog, text="Contraseña:", bg=label_bg_color, fg=label_fg_color).pack(pady=5)
        self.password_entry = tk.Entry(self.dialog, show='*', bg=entry_bg_color, fg=entry_fg_color)
        self.password_entry.pack(pady=5)

        # Frame para los botones
        button_frame = tk.Frame(self.dialog, bg='grey')
        button_frame.pack(pady=10)

        # Botones
        tk.Button(button_frame, text="Aceptar", command=self.add_user, bg=button_bg_color_accept, fg=button_fg_color).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Cancelar", command=self.dialog.destroy, bg=button_bg_color_cancel, fg=button_fg_color).pack(side=tk.LEFT, padx=5)

    def add_user(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        pasword_confirm = self.password_confirm_entry.get().strip()
        if username and password:
            self.save_user(username, password)
            self.listbox.insert(tk.END, username)
            self.dialog.destroy()
        else:
            messagebox.showwarning("Campos incompletos", "Por favor, complete todos los campos.")

    def save_user(self, username, password):
        try:
            print(f"Agregando usuario: {username}")
            # Ejecutar comandos para agregar el usuario localmente
            add_user_cmd = f'sudo useradd -m {username}'
            set_password_cmd = f'echo "{username}:{password}" | sudo chpasswd'
            add_samba_cmd = f'sudo smbpasswd -a {username}'

            subprocess.run(add_user_cmd, shell=True, check=True)
            subprocess.run(set_password_cmd, shell=True, check=True)
            subprocess.run(add_samba_cmd, shell=True, check=True)

            print(f"Usuario {username} añadido en el sistema Samba.")
        except subprocess.CalledProcessError as e:
            messagebox.showerror("Error", f"No se pudo agregar el usuario: {e}")

if __name__ == '__main__':
    root = tk.Tk()
    root.configure(bg='lightblue')
    listbox = tk.Listbox(root)
    listbox.pack()
    app = AddUserDialog(root, listbox)
    root.mainloop() """