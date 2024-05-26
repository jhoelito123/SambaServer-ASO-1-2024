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
        # Agregar usuario
        self.add_user_frame = tk.LabelFrame(self.root, text="Agregar Usuario")
        self.add_user_frame.pack(fill="both", expand="yes", padx=10, pady=10)

        tk.Label(self.add_user_frame, text="Nombre de usuario:").grid(row=0, column=0)
        self.username_entry = tk.Entry(self.add_user_frame)
        self.username_entry.grid(row=0, column=1)
        
        tk.Label(self.add_user_frame, text="Contraseña:").grid(row=1, column=0)
        self.password_entry = tk.Entry(self.add_user_frame, show='*')
        self.password_entry.grid(row=1, column=1)

        tk.Label(self.add_user_frame, text="Repetir Contraseña:").grid(row=2, column=0)
        self.password_confirm_entry = tk.Entry(self.add_user_frame, show='*')
        self.password_confirm_entry.grid(row=2, column=1)

        self.add_user_button = tk.Button(self.add_user_frame, text="Agregar Usuario", command=self.add_user)
        self.add_user_button.grid(row=3, columnspan=2, pady=5)

        # Listar usuarios
        self.list_users_frame = tk.LabelFrame(self.root, text="Lista de Usuarios")
        self.list_users_frame.pack(fill="both", expand="yes", padx=10, pady=10)

        self.users_listbox = tk.Listbox(self.list_users_frame)
        self.users_listbox.pack(fill="both", expand="yes", padx=5, pady=5)

        # Eliminar usuario
        self.delete_user_frame = tk.LabelFrame(self.root, text="Eliminar Usuario")
        self.delete_user_frame.pack(fill="both", expand="yes", padx=10, pady=10)

        self.delete_user_button = tk.Button(self.delete_user_frame, text="Eliminar Usuario Seleccionado", command=self.delete_user)
        self.delete_user_button.pack(pady=5)

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

if __name__ == "__main__":
    root = tk.Tk()
    app = SambaManagerApp(root)
    root.mainloop()
