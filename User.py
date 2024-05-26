import tkinter as tk
from tkinter import messagebox
import os
import subprocess

class SambaManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Samba User Manager")
        
        self.create_widgets()
        self.list_users()  # Listar usuarios al iniciar la aplicación

    def create_widgets(self):
        # Navigator tab (self.navigator_t4 needs to be defined; for example, it can be a frame or a tab in a notebook)
        self.navigator_t4 = tk.Frame(self.root)
        self.navigator_t4.pack(fill="both", expand=True)

        # Title configuration for consistency
        title_config = {"font": ("Arial", 12, "bold")}

        # For new navigator Users
        self.labelUsers = tk.Label(self.navigator_t4)
        self.labelUsers.place(relx=0.046, rely=0.02, height=31, width=294)
        self.labelUsers.configure(**title_config)
        self.labelUsers.configure(text='Usuarios Registrados')

        self.listUsers = tk.Listbox(self.navigator_t4)
        self.listUsers.place(relx=0.031, rely=0.099, relheight=0.675, relwidth=0.47)
        self.listUsers.configure(background="white")
        self.listUsers.configure(font="TkFixedFont")
        self.listUsers.configure(foreground="#000000")
        self.listUsers.configure(selectbackground="#feffda")
        self.listUsers.configure(selectforeground="black")

        self.butModUser = tk.Button(self.navigator_t4, command=self.open_add_user_window)
        self.butModUser.place(relx=0.526, rely=0.296, height=26, width=167)
        self.butModUser.configure(**title_config, activebackground="#d9d9d9")
        self.butModUser.configure(font="-family {Consolas} -size 10")
        self.butModUser.configure(text='Agregar usuario', anchor='center')

        self.buttDelUser = tk.Button(self.navigator_t4, command=self.delete_user)
        self.buttDelUser.place(relx=0.526, rely=0.375, height=26, width=167)
        self.buttDelUser.configure(**title_config, activebackground="#d9d9d9")
        self.buttDelUser.configure(font="-family {Consolas} -size 10")
        self.buttDelUser.configure(text='Eliminar usuario', anchor='center')

    def open_add_user_window(self):
        self.add_user_window = tk.Toplevel(self.root)
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
                self.listUsers.delete(0, tk.END)
                for user in users:
                    self.listUsers.insert(tk.END, user.split(':')[0])  # Añadido solo el nombre de usuario
            else:
                messagebox.showerror("Error", "No se pudieron listar los usuarios.")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudieron listar los usuarios. Error: {e}")

    def delete_user(self):
        try:
            selected_user = self.listUsers.get(tk.ACTIVE)
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

if __name__ == "__main__":
    root = tk.Tk()
    app = SambaManagerApp(root)
    root.mainloop()
