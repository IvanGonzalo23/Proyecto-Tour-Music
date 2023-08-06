import tkinter as tk

def mostrar_texto():
    texto = cuadro_texto.get("1.0", tk.END)
    etiqueta.config(text="Texto ingresado:\n{}".format(texto))

def cambiar_color():
    color = colores_combo.get()
    # Cambiar el color de fondo de la Ventana
    ventana.configure(bg=color)

# Crear la ventana
ventana = tk.Tk()
ventana.title("Interfaz Interactiva")
ventana.geometry("300x250")

# Crear el cuadro de texto
cuadro_texto = tk.Text(ventana, height=4, width=30)
cuadro_texto.pack(pady=10)

# Crear el botón para mostrar el texto ingresado
boton_mostrar = tk.Button(ventana, text="Mostrar texto", command=mostrar_texto)
boton_mostrar.pack()

# Crear el combo para seleccionar colores de fondo
# También se puede usar un combobox de ttk
colores = ["white", "lightblue", "lightgreen", "lightyellow"]
colores_combo = tk.StringVar()
colores_combo.set(colores[0])
combo = tk.OptionMenu(ventana, colores_combo, *colores)
combo.pack(pady=10)

# Crear el botón para cambiar el color de fondo
boton_color = tk.Button(ventana, text="Cambiar color", command=cambiar_color)
boton_color.pack()

# Crear la etiqueta para mostrar el texto ingresado
etiqueta = tk.Label(ventana, text="", bg="white", height=6, width=30)
etiqueta.pack(pady=10)

# Iniciar el bucle de eventos
ventana.mainloop()
