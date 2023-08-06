import tkinter as tk

def mostrar_texto():
    texto = entry.get()
    etiqueta.config(text=texto) # actualiza el texto de la etiqueta

# Crear la ventana
ventana = tk.Tk()
ventana.geometry("200x150")  # Establecer las dimensiones de la ventana

# Crear el Entry
entry = tk.Entry(ventana)

# Centrar el Entry con grid
entry.grid(row=0, column=0, padx=10, pady=10)

# Crear el botón
boton = tk.Button(ventana, text="Mostrar", command=mostrar_texto)

# Centrar el botón con grid
boton.grid(row=1, column=0, padx=10, pady=10)

# Crear una etiqueta para mostrar el texto
etiqueta = tk.Label(ventana, text="")
etiqueta.grid(row=2, column=0, padx=10, pady=10)

# Iniciar el bucle de eventos
ventana.mainloop()
