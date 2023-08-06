import tkinter as tk

def mostrar_elegido():
    opciones = {
        1: "Opción 1",
        2: "Opción 2",
        3: "Opción 3"
    }
    seleccionado = opcion.get()
    # Si no hay uno seleccionado, mostrar "N/A"
    etiqueta.config(text="Seleccionado: {}".format(opciones.get(seleccionado, "N/A")))

# Crear la ventana
ventana = tk.Tk()
ventana.geometry("200x200")  # Establecer las dimensiones de la ventana

# Crear una variable de control IntVar con valor inicial 1
opcion = tk.IntVar(value=1)

# Crear los botones de opción (Radiobutton)
opcion1 = tk.Radiobutton(ventana, text="Opción 1", variable=opcion, value=1)
opcion2 = tk.Radiobutton(ventana, text="Opción 2", variable=opcion, value=2)
opcion3 = tk.Radiobutton(ventana, text="Opción 3", variable=opcion, value=3)

# Posicionar los botones de opción en orientación vertical
opcion1.pack()
opcion2.pack()
opcion3.pack()

# Crear el botón para mostrar el elegido
boton = tk.Button(ventana, text="Mostrar elegido", command=mostrar_elegido)
boton.pack()

# Crear una etiqueta para mostrar el botón de opción seleccionado
etiqueta = tk.Label(ventana, text="")
etiqueta.pack()

# Iniciar el bucle de eventos
ventana.mainloop()

