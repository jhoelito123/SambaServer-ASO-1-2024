import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *
import os.path
import time
_location = os.path.dirname(__file__)
from tkinter import messagebox
import subprocess

colorDef = '#d9d9d9'
colorGrey = '#F0F0F0'
_fgcolor = '#feffda'
title_config = {
    "background": colorDef,
    "font": ("Courier New", 15, "bold"),
    "foreground": "black",
    "anchor": "w",
}

class Toplevel1:
    def __init__(self, top=None, navigate_callback=None,show_windows_callback=None, client=None):
        screen_width = top.winfo_screenwidth()
        screen_height = top.winfo_screenheight()
        x = (screen_width - 915) // 2  # El ancho de la ventana es 250
        y = (screen_height - 581) // 2  # La altura de la ventana es 116
        top.geometry(f"915x581+{x}+{y}")
        top.minsize(120, 1)
        top.maxsize(1924, 1061)
        top.resizable(1,  1)
        top.title("Configuración servicio Samba")
        top.configure(background=colorDef)

        self.client = client
        self.top = top
        self.navigate_callback = navigate_callback
        self.show_windows_callback = show_windows_callback
        
        self.che63 = tk.IntVar()
        self.cheStart = tk.BooleanVar()
        self.che64 = tk.IntVar()
                
        #Valores leidos de la configuracion anterior
        self.afterConfig = lines_start_conf[0]
        self.afterConfigValue = self.afterConfig.split("=")[1]
        self.afterReboot = lines_start_conf[1]
        self.afterRebootValue = self.afterReboot.split("=")[1]
        
        #Reinica el servicio si se estaba configurado
        if((self.afterRebootValue == "True") & (len(lines_start_conf) != 3)): 
            self.start_service()

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

        # #for new navigator Users
        # self.labelUsers = tk.Label(self.navigator_t4)
        # self.labelUsers.place(relx=0.046, rely=0.02, height=31, width=294)
        # self.labelUsers.configure(**title_config)
        # self.labelUsers.configure(text='''Usuarios Registrados''')

        # self.listUsers = tk.Listbox(self.navigator_t4)
        # self.listUsers.place(relx=0.031, rely=0.099, relheight=0.675, relwidth=0.47)
        # self.listUsers.configure(background="white")
        # self.listUsers.configure(font="TkFixedFont")
        # self.listUsers.configure(foreground="#000000")
        # self.listUsers.configure(selectbackground="#feffda")
        # self.listUsers.configure(selectforeground="black")

        # self.butModUser = tk.Button(self.navigator_t4)
        # self.butModUser.place(relx=0.526, rely=0.296, height=26, width=167)
        # self.butModUser.configure(**title_config,activebackground=_fgcolor)
        # self.butModUser.configure(font="-family {Consolas} -size 10")
        # self.butModUser.configure(text='''Agregar usuario''',anchor='center')
        # self.butModUser.configure(command=self.add_user)

        # self.buttDelUser = tk.Button(self.navigator_t4)
        # self.buttDelUser.place(relx=0.526, rely=0.375, height=26, width=167)
        # self.buttDelUser.configure(**title_config,activebackground=_fgcolor)
        # self.buttDelUser.configure(font="-family {Consolas} -size 10")
        # self.buttDelUser.configure(text='''Eliminar usuario''',anchor='center')
        
        self.create_widgets()
        self.list_users()
          
        #Configuracion usuario
        self.cuadroInicial = tk.Frame(self.navigator_t1)
        self.cuadroInicial.place(relx=0.011, rely=0.04, relheight=0.51, relwidth=0.97)
        self.cuadroInicial.configure(relief='groove',borderwidth="2",background=colorGrey)

        self.textEstado = tk.Label(self.cuadroInicial)
        self.textEstado.place(relx=0.023, rely=0.168, height=21, width=150)
        self.textEstado.configure(**title_config)
        self.textEstado.configure(background=colorGrey)
        self.textEstado.configure(font="-family {Courier New} -size 12 -weight bold")
        self.textEstado.configure(text='''Estado actual:''')

        self.statusService = tk.Label(self.cuadroInicial)
        self.statusService.place(relx=0.219, rely=0.159, height=21, width=82)
        self.statusService.configure(**title_config)
        self.statusService.configure(background=colorGrey)
        self.statusService.configure(font="-family {Consolas} -size 11")
        #Estado del servicio
        self.load_service_status()

        self.textLaterConfig = tk.Label(self.cuadroInicial)
        self.textLaterConfig.place(relx=0.023, rely=0.262, height=20, width=220)
        self.textLaterConfig.configure(**title_config)
        self.textLaterConfig.configure(background=colorGrey)
        self.textLaterConfig.configure(font="-family {Courier New} -size 12 -weight bold")
        self.textLaterConfig.configure(text='''Después de configurar:''')

        self.selected_option = tk.StringVar(self.cuadroInicial)
        if self.afterConfigValue: 
            self.selected_option.set(self.afterConfigValue)
        else:
            self.selected_option.set("Seleccione una opción")
          # Establece un valor predeterminado

        options = ["Reiniciar Servicio", "Detener", "Mantener estado actual", "Recargar"]

        self.estadoActual = tk.OptionMenu(self.cuadroInicial, self.selected_option, *options, command=self.updateLaterConfig)
        self.estadoActual.place(relx=0.046, rely=0.354, relheight=0.092, relwidth=0.23)
        
        #INICIAR ? 
        self.Label1 = tk.Label(self.cuadroInicial)
        self.Label1.place(relx=0.023, rely=0.47, height=18, width=209)
        self.Label1.configure(**title_config)
        self.Label1.configure(background=colorGrey)
        self.Label1.configure(font="-family {Courier New} -size 12 -weight bold")
        self.Label1.configure(text='''Después de reiniciar:''')
        
        self.startServiceCheck = tk.Checkbutton(self.cuadroInicial)
        self.startServiceCheck.place(relx=0.046, rely=0.55, relheight=0.096, relwidth=0.125)
        self.startServiceCheck.configure(**title_config, activebackground="#d9d9d9")
        self.startServiceCheck.configure(background=colorGrey)
        self.startServiceCheck.configure(font="-family {Consolas} -size 10")
        self.startServiceCheck.configure(text='''¿Iniciar?''')
        self.startServiceCheck.configure(variable=self.cheStart)
        self.startServiceCheck.configure(command=self.updateStartServiceCheck)
        if self.afterRebootValue == "True": self.startServiceCheck.select()


        self.tituloInicio = tk.Label(self.cuadroInicial)
        self.tituloInicio.place(relx=0.313, rely=0.047, height=21, width=316)
        self.tituloInicio.configure(**title_config)
        self.tituloInicio.configure(background=colorGrey)
        self.tituloInicio.configure(text='''Configuración del Servicio''')
        ###############################3

        self.botonAdd = tk.Button(self.navigator_t2)
        self.botonAdd.place(relx=0.023, rely=0.483, height=26, width=57)
        self.botonAdd.configure(**title_config,activebackground=_fgcolor)
        self.botonAdd.configure(font="-family {Consolas} -size 10")
        self.botonAdd.configure(text='''Agregar''',anchor='center')
        self.botonAdd.configure(command=lambda: open_new_resource_window(self))
        
        
        def open_new_resource_window(self):
            new_window = tk.Toplevel(self.top)
            new_resource_window = newResource(top=new_window, parent=self)

        self.listActual = ScrolledListBox(self.navigator_t2)
        self.listActual.place(relx=0.023, rely=0.125, relheight=0.348, relwidth=0.938)
        self.listActual.configure(background="white")
        self.listActual.configure(cursor="xterm")
        self.listActual.configure(font="TkFixedFont")
        self.listActual.configure(foreground="black")
        self.listActual.configure(selectbackground="#feffda")
        self.listActual.configure(selectforeground="black")
        load_shared_resources(self.listActual)
        
        self.botonEdit = tk.Button(self.navigator_t2)
        self.botonEdit.place(relx=0.101, rely=0.483, height=26, width=57)
        self.botonEdit.configure(**title_config,activebackground=_fgcolor)
        self.botonEdit.configure(font="-family {Consolas} -size 10")
        self.botonEdit.configure(text='''Editar''',anchor="center")
        self.botonEdit.configure(command=lambda: edit(self, self.show_windows_callback))

        self.botonDel = tk.Button(self.navigator_t2)
        self.botonDel.place(relx=0.18, rely=0.483, height=26, width=57)
        self.botonDel.configure(**title_config, activebackground=_fgcolor)
        self.botonDel.configure(font="-family {Consolas} -size 10")
        self.botonDel.configure(text='''Quitar''',anchor='center')
        self.botonDel.configure(command=self.remove_selected_item)

        self.Label2 = tk.Label(self.navigator_t2)
        self.Label2.place(relx=0.023, rely=0.021, height=18, width=248)
        self.Label2.configure(**title_config)
        self.Label2.configure(text='''Recursos compartidos''')    
        
        #Encabezado del ScrolledListBox
        self.labelRo = tk.Label(self.navigator_t2)
        self.labelRo.place(relx=0.023, rely=0.080, height=21, width=102)
        self.labelRo.configure(**title_config)
        self.labelRo.configure(background=colorDef)
        self.labelRo.configure(font="-family {Consolas} -size 11")
        self.labelRo.configure(text="Read-only")
        
        self.labelName = tk.Label(self.navigator_t2)
        self.labelName.place(relx=0.190, rely=0.080, height=21, width=82)
        self.labelName.configure(**title_config)
        self.labelName.configure(background=colorDef)
        self.labelName.configure(font="-family {Consolas} -size 11")
        self.labelName.configure(text="Nombre")
        
        self.labelPath = tk.Label(self.navigator_t2)
        self.labelPath.place(relx=0.310, rely=0.080, height=21, width=82)
        self.labelPath.configure(**title_config)
        self.labelPath.configure(background=colorDef)
        self.labelPath.configure(font="-family {Consolas} -size 11")   
        self.labelPath.configure(text="Path")

        self.labelComment = tk.Label(self.navigator_t2)
        self.labelComment.place(relx=0.530, rely=0.080, height=21, width=102)
        self.labelComment.configure(**title_config)
        self.labelComment.configure(background=colorDef)
        self.labelComment.configure(font="-family {Consolas} -size 11")   
        self.labelComment.configure(text="Comentario")
        
        #
        self.frameWorkGroup = tk.Frame(self.navigator_t3)
        self.frameWorkGroup.place(relx=0.022, rely=0.102, relheight=0.399, relwidth=0.926)
        self.frameWorkGroup.configure(relief='groove',borderwidth="2",background=colorGrey)

        self.labelWorkgroup = tk.Label(self.frameWorkGroup)
        self.labelWorkgroup.place(relx=0.012, rely=0.053, height=20, width=209)
        self.labelWorkgroup.configure(**title_config)
        self.labelWorkgroup.configure(background=colorGrey)
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
        
    def updateLaterConfig(self, *args):
        global lines_start_conf
        afterConfig = lines_start_conf[0]
        afterConfigKey = afterConfig.split("=")[0]
        lines_start_conf[0] =  f"{afterConfigKey}={self.selected_option.get()}"
        
    def updateStartServiceCheck(self):
        global lines_start_conf
        afterReboot = lines_start_conf[1]
        afterRebootKey = afterReboot.split("=")[0]
        lines_start_conf[1] =  f"{afterRebootKey}={self.cheStart.get()}"        
    
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
        self.save_start_conf()
        
        if self.selected_option.get() == "Reiniciar Servicio":
            self.reboot_service()
        elif self.selected_option.get() == "Detener":
            self.stop_service()
        self.load_service_status() #Actualiza el status 
        lines = read_smb_conf(file_path)
        resources = extract_shared_resources(lines)
        initial_conf = extract_shared_resources(lines)
        load_shared_resources(self.listActual)
            
        messagebox.showinfo("Info", "Los cambios se han guardado correctamente.")
    

    def cancel_changes(self):
        global resources,initial_conf
        resources = initial_conf
        messagebox.showinfo("Info", "Los cambios han sido cancelados.")
        
    def save_start_conf(self):
        with open(path_start_conf, "w") as file:
            file.write(f"after config={self.selected_option.get()}\n")
            file.write(f"after reboot={self.cheStart.get()}")
            
    def load_service_status(self):
        session = self.client.get_transport().open_session()
        if session.active:
            command = 'service smb status'
            session.exec_command(command)
            stdout = ''
            time.sleep(2)
            while True:
                if session.recv_ready():
                    stdout += session.recv(1024).decode()
                else:
                    if session.exit_status_ready():
                        break
            stderr = session.recv_stderr(1024).decode()
            if stderr:
                print("Error:", stderr)
                return 
            print(stdout)
            state = "Activo" if stdout.find('(running)') != -1 else "Inactivo"
            self.statusService.configure(text=state)
            session.close()
        else:
            print("La sesión no está activa")
        
    def reboot_service(self):
        session = self.client.get_transport().open_session()
        if session.active:
            command = 'service smb restart'
            session.exec_command(command)
            time.sleep(1)
            session.close()
            
    def stop_service(self):
        session = self.client.get_transport().open_session()
        if session.active:
            command = 'service smb stop'
            session.exec_command(command)
            time.sleep(1)
            session.close()
            
    def start_service(self):
        session = self.client.get_transport().open_session()
        if session.active:
            command = 'service smb start'
            session.exec_command(command)
            time.sleep(1)
            session.close()
            
    def create_widgets(self):
        # Agregar usuario
        self.add_user_frame = tk.LabelFrame(self.navigator_t4, text="Agregar Usuario")
        self.add_user_frame.pack(fill="both", expand="yes", padx=10, pady=10)

        self.add_user_button = tk.Button(self.add_user_frame, text="Agregar Usuario", command=self.open_add_user_window)
        self.add_user_button.pack(pady=5)

        # Listar usuarios
        self.list_users_frame = tk.LabelFrame(self.navigator_t4, text="Lista de Usuarios")
        self.list_users_frame.pack(fill="both", expand="yes", padx=10, pady=10)

        self.users_listbox = tk.Listbox(self.list_users_frame)
        self.users_listbox.pack(fill="both", expand="yes", padx=5, pady=5)

        # Eliminar usuario
        self.delete_user_frame = tk.LabelFrame(self.navigator_t4, text="Eliminar Usuario")
        self.delete_user_frame.pack(fill="both", expand="yes", padx=10, pady=10)

        self.delete_user_button = tk.Button(self.delete_user_frame, text="Eliminar Usuario Seleccionado", command=self.delete_user)
        self.delete_user_button.pack(pady=5)

    def open_add_user_window(self):
        screen_width = self.top.winfo_screenwidth()
        screen_height = self.top.winfo_screenheight()
        x = (screen_width - 200) // 2  # El ancho de la ventana es 250
        y = (screen_height - 200) // 2  # La altura de la ventana es 116
        
        self.add_user_window = tk.Toplevel(self.navigator_t4)
        self.add_user_window.geometry(f"340x180+{x}+{y}")
        self.add_user_window.title("Agregar Usuario")

        tk.Label(self.add_user_window, text="Nombre de usuario:").grid(row=0, column=0, padx=10, pady=5)
        self.username_entry = tk.Entry(self.add_user_window)
        self.username_entry.grid(row=0, column=1, padx=10, pady=5)
        
        tk.Label(self.add_user_window, text="Contraseña:").grid(row=1, column=0, padx=10, pady=5)
        self.password_entry = tk.Entry(self.add_user_window, show='*')
        self.password_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(self.add_user_window, text="Repetir Contraseña:").grid(row=2, column=0, padx=10, pady=5)
        self.password_confirm_entry = tk.Entry(self.add_user_window, show='*')
        self.password_confirm_entry.grid(row=2, column=1, padx=10, pady=5)

        self.accept_button = tk.Button(self.add_user_window, text="Aceptar", command=self.add_user)
        self.accept_button.grid(row=3, column=0, padx=10, pady=5)
        
        self.cancel_button = tk.Button(self.add_user_window, text="Cancelar", command=self.add_user_window.destroy)
        self.cancel_button.grid(row=3, column=1, padx=10, pady=5)

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
                self.list_users()  # Actualizar la lista de usuarios
                self.add_user_window.destroy()  # Cerrar la ventana de agregar usuario
            else:
                raise subprocess.CalledProcessError(proc_smbpasswd.returncode, 'smbpasswd')
        except subprocess.CalledProcessError as e:
            messagebox.showerror("Error", f"No se pudo agregar el usuario {username}. Error: {e}")

    def list_users(self):
        try:
            process = subprocess.Popen(['sudo', 'pdbedit', '-L'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            output, _ = process.communicate()
            if process.returncode == 0:
                users = output.decode().strip().split('\n')
                self.users_listbox.delete(0, tk.END)
                for user in users:
                    self.users_listbox.insert(tk.END, user.split(':')[0])  # Añadido solo el nombre de usuario
            else:
                messagebox.showerror("Error", "No se pudieron listar los usuarios.")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudieron listar los usuarios. Error: {e}")

    def delete_user(self):
        try:
            selected_user = self.users_listbox.get(tk.ACTIVE)
            if not selected_user:
                messagebox.showwarning("Advertencia", "Por favor, seleccione un usuario de la lista.")
                return
            # Comando para eliminar usuario de Samba
            process = subprocess.Popen(['sudo', 'smbpasswd', '-x', selected_user], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            _, error = process.communicate()
            if process.returncode == 0:
                # Comando para eliminar usuario del sistema
                subprocess.run(['sudo', 'userdel', '-r', selected_user], check=True)
                messagebox.showinfo("Éxito", f"Usuario {selected_user} eliminado con éxito.")
                self.list_users()  # Actualizar la lista de usuarios
            else:
                messagebox.showerror("Error", f"No se pudo eliminar el usuario {selected_user}. Error: {error.decode()}")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo eliminar el usuario {selected_user}. Error: {e}")
        

def read_start_conf(path_conf):
    with open(path_conf, "r") as file:
        lines = file.readlines()
        lines = [line.strip() for line in lines]
        return lines
            


path_start_conf = "configs/config_start.conf"

lines_start_conf = read_start_conf(path_start_conf)
        
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
        screen_width = top.winfo_screenwidth()
        screen_height = top.winfo_screenheight()
        x = (screen_width - 328) // 2  # El ancho de la ventana es 250
        y = (screen_height - 312) // 2  # La altura de la ventana es 116
        top.geometry(f"328x312+{x}+{y}")
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

# file_path = "C:/Users/John/Desktop/Materias/materias5/Aplicacion SO/proyectoAso/segundo/SambaServer-ASO-1-2024/Interface/smb.conf" 

# file_path = "/home/link/Escritorio/ProyectoAso/SambaServer-ASO-1-2024/Interface/smb.conf"

file_path = "/etc/samba/smb.conf"

#error al leer directo en src/smb.conf, copiar ruta completa
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
    global lines_start_conf
    selected_index = self.listActual.curselection()
    if selected_index:
        index = selected_index[0]  # Obtener el índice del recurso seleccionado
        selected_resource = resources[index+1]  # Obtener el recurso completo usando el índice
        lines_start_conf.append("is_back")
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

def start_up_Interface(parent=None, navigate_callback=None, show_windows_callback=None, client=None):
    _w1 = Toplevel1(parent, navigate_callback, show_windows_callback, client)

if __name__ == '__main__':
    start_up_Interface()
    
    
import paramiko
class AddUserDialog:
    def __init__(self, parent, listbox):
        self.parent = parent
        self.listbox = listbox
        self.dialog = tk.Toplevel(parent)
        self.dialog.title("Agregar Usuario")
        self.dialog.geometry("300x200")

        tk.Label(self.dialog, text="Nombre de usuario:").pack(pady=5)
        self.username_entry = tk.Entry(self.dialog)
        self.username_entry.pack(pady=5)

        tk.Label(self.dialog, text="Contraseña:").pack(pady=5)
        self.password_entry = tk.Entry(self.dialog, show='*')
        self.password_entry.pack(pady=5)

        tk.Button(self.dialog, text="Aceptar", command=self.add_user).pack(pady=5)
        tk.Button(self.dialog, text="Cancelar", command=self.dialog.destroy).pack(pady=5)

    def add_user(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        if username and password:
            # Guardar usuario en la lista local
            self.listbox.insert(tk.END, username)
            # Intentar guardar el usuario en el sistema Samba
            self.save_user(username, password)
            self.dialog.destroy()
        else:
            messagebox.showwarning("Campos incompletos", "Por favor, complete todos los campos.")
            
            
    def save_user(self, username, password):
        try:
            print(f"Simulando la adición del usuario: {username} con la contraseña: {password}")
            # Código para conectarse al servidor Samba y agregar el usuario
            """ ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect('samba_server_ip', username='your_username', password='your_password')
            
            # Comandos para agregar un usuario en Samba
            add_user_cmd = f'sudo useradd -m {username}'
            set_password_cmd = f'echo "{username}:{password}" | sudo chpasswd'
            add_samba_cmd = f'sudo smbpasswd -a {username}'

            stdin, stdout, stderr = ssh.exec_command(add_user_cmd)
            print(stdout.read().decode(), stderr.read().decode())
            
            stdin, stdout, stderr = ssh.exec_command(set_password_cmd)
            print(stdout.read().decode(), stderr.read().decode())
            
            stdin, stdout, stderr = ssh.exec_command(add_samba_cmd)
            print(stdout.read().decode(), stderr.read().decode())
            
            ssh.close() """
            print(f"Usuario {username} añadido en el sistema Samba (simulado).")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo agregar el usuario: {e}")


if __name__ == '__main__':
    root = tk.Tk()
    app = Toplevel1(root)
    root.mainloop()