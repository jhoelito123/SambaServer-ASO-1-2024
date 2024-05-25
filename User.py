import tkinter as tk
from tkinter import messagebox
import os
import subprocess

class SambaManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Samba User Manager")
        
        self.create_widgets()

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

        self.refresh_button = tk.Button(self.list_users_frame, text="Actualizar Lista", command=self.list_users)
        self.refresh_button.pack(pady=5)

        # Eliminar usuario
        self.delete_user_frame = tk.LabelFrame(self.root, text="Eliminar Usuario")
        self.delete_user_frame.pack(fill="both", expand="yes", padx=10, pady=10)

        tk.Label(self.delete_user_frame, text="Nombre de usuario:").grid(row=0, column=0)
        self.del_username_entry = tk.Entry(self.delete_user_frame)
        self.del_username_entry.grid(row=0, column=1)

        self.delete_user_button = tk.Button(self.delete_user_frame, text="Eliminar Usuario", command=self.delete_user)
        self.delete_user_button.grid(row=1, columnspan=2, pady=5)

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
            # Comando para agregar usuario a Samba
            process = subprocess.Popen(['sudo', 'smbpasswd', '-a', username], stdin=subprocess.PIPE, stderr=subprocess.PIPE)
            process.communicate(input=f'{password}\n{password}\n'.encode())
            if process.returncode == 0:
                messagebox.showinfo("Éxito", f"Usuario {username} agregado con éxito.")
            else:
                messagebox.showerror("Error", f"No se pudo agregar el usuario {username}.")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo agregar el usuario {username}. Error: {e}")

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

if __name__ == "__main__":
    root = tk.Tk()
    app = SambaManagerApp(root)
    root.mainloop()
