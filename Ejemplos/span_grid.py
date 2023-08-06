import tkinter as tk

def mostrar_contacto():
    nombre = entry_nombre.get()
    telefono = entry_telefono.get()
    correo = entry_correo.get()
    info_contacto.config(text="Nombre: {}\nTeléfono: {}\nCorreo: {}".format(nombre, telefono, correo))

# Crear la ventana
ventana = tk.Tk()
ventana.title("Información de Contacto")

# Crear las etiquetas y las entradas de texto
label_nombre = tk.Label(ventana, text="Nombre:")
label_nombre.grid(row=0, column=0, padx=10, pady=10)
entry_nombre = tk.Entry(ventana)
entry_nombre.grid(row=0, column=1, padx=10, pady=10)

label_telefono = tk.Label(ventana, text="Teléfono:")
label_telefono.grid(row=1, column=0, padx=10, pady=10)
entry_telefono = tk.Entry(ventana)
entry_telefono.grid(row=1, column=1, padx=10, pady=10)

label_correo = tk.Label(ventana, text="Correo:")
label_correo.grid(row=2, column=0, padx=10, pady=10)
entry_correo = tk.Entry(ventana)
entry_correo.grid(row=2, column=1, padx=10, pady=10)

# El botón y la etiqueta de información de contacto se extienden a dos columnas

# Crear el botón para mostrar la información de contacto
boton_mostrar = tk.Button(ventana, text="Mostrar Contacto", command=mostrar_contacto)
boton_mostrar.grid(row=3, columnspan=2, padx=10, pady=10)

# Crear la etiqueta para mostrar la información de contacto
info_contacto = tk.Label(ventana, text="", padx=10, pady=10)
info_contacto.grid(row=4, columnspan=2)

# Iniciar el bucle de eventos
ventana.mainloop()
