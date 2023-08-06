import tkinter as tk

def obtener_texto():
    texto = cuadro_texto.get("1.0", tk.END)
    etiqueta.config(text=texto)

# Crear la ventana
ventana = tk.Tk()

# Crear un widget Text
cuadro_texto = tk.Text(ventana, height=5, width=30)

# Insertar texto inicial en el widget Text
cuadro_texto.insert(tk.END, "Escribe aquí...")

# Posicionar el widget Text
cuadro_texto.pack()

# Crear el botón para obtener el texto
boton = tk.Button(ventana, text="Obtener texto", command=obtener_texto)
boton.pack()

# Crear una etiqueta con wraplength para que el texto se ajuste al ancho
etiqueta = tk.Label(ventana, text="", wraplength=200)
etiqueta.pack()

# Iniciar el bucle de eventos
ventana.mainloop()
