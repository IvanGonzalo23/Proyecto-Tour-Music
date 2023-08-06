import tkinter as tk

def mostrar_valor():
    valor = opcion.get()
    etiqueta.config(text="Valor seleccionado: {}".format(valor))

# Crear la ventana
ventana = tk.Tk()

# Crear una variable de control IntVar
opcion = tk.IntVar()

# Crear el botón de selección (checkbutton)
checkbutton = tk.Checkbutton(ventana, text="Opción", variable=opcion)

# Centrar el checkbutton con grid
checkbutton.grid(row=0, column=0, padx=10, pady=10)

# Crear el botón para mostrar el valor
boton = tk.Button(ventana, text="Mostrar valor", command=mostrar_valor)

# Centrar el botón con grid
boton.grid(row=1, column=0, padx=10, pady=10)

# Crear una etiqueta para mostrar el valor seleccionado
etiqueta = tk.Label(ventana, text="")
etiqueta.grid(row=2, column=0, padx=10, pady=10)

# Iniciar el bucle de eventos
ventana.mainloop()
