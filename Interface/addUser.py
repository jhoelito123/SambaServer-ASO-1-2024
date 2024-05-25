import tkinter as tk
from tkinter import ttk
import paramiko

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Main Window")

        self.navigator_t4 = tk.Frame(root)
        self.navigator_t4.pack(fill='both', expand=True)

        self.labelUsers = tk.Label(self.navigator_t4)
        self.labelUsers.place(relx=0.046, rely=0.02, height=31, width=294)
        self.labelUsers.configure(text='Usuarios Registrados', font=("Arial", 12))

        self.listUsers = tk.Listbox(self.navigator_t4)
        self.listUsers.place(relx=0.031, rely=0.099, relheight=0.675, relwidth=0.47)
        self.listUsers.configure(background="white", font="TkFixedFont", foreground="#000000", 
                                 selectbackground="#feffda", selectforeground="black")

        self.butModUser = tk.Button(self.navigator_t4, text='Agregar usuario', font="-family {Consolas} -size 10", 
                                    command=self.open_add_user_window)
        self.butModUser.place(relx=0.526, rely=0.296, height=26, width=167)

        self.buttDelUser = tk.Button(self.navigator_t4, text='Eliminar usuario', font="-family {Consolas} -size 10")
        self.buttDelUser.place(relx=0.526, rely=0.375, height=26, width=167)

        self.navigator_t1 = tk.Frame(root)
        self.navigator_t1.pack(fill='both', expand=True)

        self.cuadroInicial = tk.Frame(self.navigator_t1)
        self.cuadroInicial.place(relx=0.011, rely=0.04, relheight=0.51, relwidth=0.97)
        self.cuadroInicial.configure(relief='groove', borderwidth="2", background="#d9d9d9")

    def open_add_user_window(self):
        add_user_window = tk.Toplevel(self.root)
        add_user_window.title("Agregar Usuario")

        tk.Label(add_user_window, text="Nombre de Usuario:").grid(row=0, column=0, padx=10, pady=10)
        username_entry = tk.Entry(add_user_window)
        username_entry.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(add_user_window, text="Contraseña:").grid(row=1, column=0, padx=10, pady=10)
        password_entry = tk.Entry(add_user_window, show="*")
        password_entry.grid(row=1, column=1, padx=10, pady=10)

        tk.Button(add_user_window, text="Guardar", command=lambda: self.save_user(username_entry.get(), password_entry.get())).grid(row=2, column=0, columnspan=2, pady=10)

    def save_user(self, username, password):
        print(f"Simulando la adición del usuario: {username} con la contraseña: {password}")
        # Simulación de la lógica para agregar un usuario en Samba utilizando paramiko
        # Aquí en realidad sólo imprimimos los valores para demostrar que se recibirán los datos correctamente.

        # Código simulado para mostrar cómo se utilizaría paramiko
        """
        ssh = paramiko.SSHClient()
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
        
        ssh.close()
        """
        # Aquí, en lugar de ejecutar los comandos, imprimimos un mensaje de simulación
        print(f"Usuario {username} añadido en el sistema Samba (simulado).")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
