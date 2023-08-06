import tkinter as tk

def login():
    username = entry_username.get()
    password = entry_password.get()
    if username == "admin" and password == "academia":
        label_status.config(text="Inicio de sesión exitoso", fg="green")
    else:
        label_status.config(text="Nombre de usuario o contraseña incorrectos", fg="red")

# Crear la ventana
ventana = tk.Tk()
ventana.title("Login Screen")

# Configurar padding uniforme para todos los widgets
padding = 10

# Crear etiqueta de nombre de usuario
label_username = tk.Label(ventana, text="Nombre de usuario:")
label_username.grid(row=0, column=0, padx=padding, pady=padding)

# Crear entrada de nombre de usuario
entry_username = tk.Entry(ventana)
entry_username.grid(row=0, column=1, padx=padding, pady=padding)

# Crear etiqueta de contraseña
label_password = tk.Label(ventana, text="Contraseña:")
label_password.grid(row=1, column=0, padx=padding, pady=padding)

# Crear entrada de contraseña
entry_password = tk.Entry(ventana, show="*")
entry_password.grid(row=1, column=1, padx=padding, pady=padding)

# Crear botón de inicio de sesión
button_login = tk.Button(ventana, text="Iniciar sesión", command=login)
button_login.grid(row=2, columnspan=2, padx=padding, pady=padding)

# Crear etiqueta de estado
label_status = tk.Label(ventana, text="")
label_status.grid(row=3, columnspan=2, padx=padding, pady=padding)

# Iniciar el bucle de eventos
ventana.mainloop()
