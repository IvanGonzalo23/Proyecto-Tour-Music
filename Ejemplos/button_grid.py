import tkinter as tk

def mostrar_mensaje():
    print("Hola Tkinter")

# Crear la ventana
ventana = tk.Tk()
ventana.geometry("100x100")  # Establecer las dimensiones de la ventana

# Crear el botón
boton = tk.Button(ventana, text="Haz clic", command=mostrar_mensaje)

# Centrar el botón con grid
boton.grid(row=0, column=0, padx=25, pady=25)

# Iniciar el bucle de eventos
ventana.mainloop()
