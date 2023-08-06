import tkinter as tk

def mostrar_seleccion():
    indice = lista.curselection()
    if indice:
        seleccionado = lista.get(indice)
        etiqueta.config(text="Seleccionado: {}".format(seleccionado))
    else:
        etiqueta.config(text="Seleccionado: N/A")

# Crear la ventana
ventana = tk.Tk()
ventana.geometry("200x250")  # Establecer las dimensiones de la ventana

titulo = tk.Label(ventana, text="Selecciona una fruta")
titulo.pack()

# Crear un ListBox
lista = tk.Listbox(ventana, selectmode=tk.SINGLE)

# Agregar elementos a la lista
elementos = ["Manzana", "Banana", "Naranja", "Pera", "Uva"]
for elemento in elementos:
    lista.insert(tk.END, elemento)

# Posicionar el ListBox
lista.pack()

# Crear el botón para mostrar la selección
boton = tk.Button(ventana, text="Mostrar selección", command=mostrar_seleccion)
boton.pack()

# Crear una etiqueta para mostrar la selección
etiqueta = tk.Label(ventana, text="")
etiqueta.pack()

# Iniciar el bucle de eventos
ventana.mainloop()
