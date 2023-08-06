import tkinter as tk
import customtkinter as ctk
import json

class Agregar_favoritos(ctk.CTkFrame):
    def __init__(self, parent, usuario_logeado=None):
        super().__init__(parent)
        self.parent = parent
        self.usuario_logeado = usuario_logeado
        self.frame = ctk.CTkFrame(self, width=700, height=500, fg_color="#4C333F")
        self.frame.grid()
        self.listbox()
        self.widgets()

    def widgets(self):
        mi_fuente = ctk.CTkFont(family="Roboto", size=16, weight="bold")
        self.label = ctk.CTkLabel(self, text="Favoritos", text_color="yellow", bg_color="#4C333F", fg_color="#4C333F", font=mi_fuente)
        self.label.place(x=300, y=50)

        self.btn_agregar = ctk.CTkButton(self, text="Agregar", command=self.agregar_favorito)
        self.btn_agregar.place(x=400, y=460)

        self.btn_volver = ctk.CTkButton(self, text="Volver", command=lambda: [self.volver()])
        self.btn_volver.place(x=100, y=460)

    def listbox(self):
        self.listbox = tk.Listbox(self, width=60, height=20, background="#131B2E", fg="yellow", font=("Open Sans", 10))
        self.listbox.place(x=150, y=100)

        try:
            with open("./data/historial_eventos.json", "r") as file:
                eventos_historial = json.load(file)

           
            for evento_data in eventos_historial:
                evento_nombre = evento_data["Nombre"]
                self.listbox.insert(tk.END, evento_nombre)
        except FileNotFoundError:
            
            pass

    def volver(self):
        self.grid_forget()
        self.parent.show_secundaria_frame()

    def manejar_favoritos(self,usuario, evento):
       
        evento_favorito = {
            "usuario": usuario,
            "evento": evento,
            "favorito": True
        }

        
        try:
            with open("./data/favoritos.json", "r") as file:
                favoritos = json.load(file)
                
                if not isinstance(favoritos, list):
                    favoritos = [favoritos]
        except FileNotFoundError:
            favoritos = []

        
        favoritos.append(evento_favorito)

       
        with open("./data/favoritos.json", "w") as file:
            json.dump(favoritos, file, indent=4)

        
        return favoritos
    
    
    
    favoritos_indices = []
    

    
    def agregar_favorito(self):
        
        try:
            usuario = self.usuario_logeado["User"] # Intentar acceder al usuario logeado
        except TypeError: # Si ocurre un error de tipo
            print("No hay ningún usuario logeado") # Mostrar un mensaje de error
            return # Salir de la función
   
        evento_seleccionado = self.listbox.get(self.listbox.curselection())

        if evento_seleccionado:
            
            usuario = self.usuario_logeado["User"]

            
            self.manejar_favoritos(usuario, evento_seleccionado)

        
            index = self.listbox.curselection()[0]
            self.listbox.itemconfig(index, bg="yellow")


            self.favoritos_indices
            self.favoritos_indices.append(index)
