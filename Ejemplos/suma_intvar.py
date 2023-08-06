import tkinter as tk

def sumar_numeros():
    num1 = numero1.get()
    num2 = numero2.get()
    suma = num1 + num2
    etiqueta.config(text="Suma: {}".format(suma))

# Crear la ventana
ventana = tk.Tk()
ventana.geometry("200x200")  # Establecer las dimensiones de la ventana

# Crear las variables de control IntVar
numero1 = tk.IntVar()
numero2 = tk.IntVar()

# Crear los widgets Entry para ingresar números
entry1 = tk.Entry(ventana, textvariable=numero1)
entry2 = tk.Entry(ventana, textvariable=numero2)

# Centrar los Entry con grid
entry1.grid(row=0, column=0, padx=10, pady=10)
entry2.grid(row=1, column=0, padx=10, pady=10)

# Crear el botón para sumar los números
boton = tk.Button(ventana, text="Sumar", command=sumar_numeros)

# Centrar el botón con grid
boton.grid(row=2, column=0, padx=10, pady=10)

# Crear una etiqueta para mostrar la suma
etiqueta = tk.Label(ventana, text="")
etiqueta.grid(row=3, column=0, padx=10, pady=10)

# Iniciar el bucle de eventos
ventana.mainloop()
