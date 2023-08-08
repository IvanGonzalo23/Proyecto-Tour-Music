import tkinter as tk
import customtkinter as ctk
import json

class Agregar_favoritos(ctk.CTkFrame):
    """Clase que representa el Frame para agregar favoritos"""
    def __init__(self, parent, usuario_logeado=None):
        super().__init__(parent)
        self.parent = parent
        self.usuario_logeado = usuario_logeado
        self.frame = ctk.CTkFrame(self, width=700, height=500, fg_color="#4C333F")
        self.favoritos_indices = []
        self.frame.grid()
        self.listbox()
        self.widgets()
    def widgets(self):
        """Funcion que crea los widgets para el frame"""
        mi_fuente = ctk.CTkFont(family="Roboto", size=16, weight="bold")
        self.label = ctk.CTkLabel(self, text="Favoritos", text_color="yellow", bg_color="#4C333F", fg_color="#4C333F", font=mi_fuente)
        self.label.place(x=300, y=50)

        self.btn_agregar = ctk.CTkButton(self, text="Agregar", command=self.agregar_favorito)
        self.btn_agregar.place(x=400, y=460)

        self.btn_volver = ctk.CTkButton(self, text="Volver", command=lambda: [self.volver()])
        self.btn_volver.place(x=100, y=460)

    def listbox(self):
        """Funcion que crea el listbox con la lista de eventos"""
        self.listbox = tk.Listbox(self, width=60, height=20, background="#131B2E", fg="yellow", font=("Open Sans", 10))
        self.listbox.place(x=150, y=100)

        try:
            with open("./data/historial_eventos.json", "r") as file:
                eventos_historial = json.load(file)

            for evento_data in eventos_historial:
                evento_nombre = evento_data["Nombre"]
                self.listbox.insert(tk.END, evento_nombre)

            with open("./data/favoritos.json", "r") as file:
                favoritos = json.load(file)

                for index, evento_favorito in enumerate(favoritos):
                    if evento_favorito["usuario"] == self.usuario_logeado["User"]:
                        evento = evento_favorito["evento"]
                        self.favoritos_indices.append(index)
                        try:
                            idx = self.listbox.get(0, tk.END).index(evento)
                            self.listbox.itemconfig(idx, bg="yellow", fg="black")
                        except ValueError:
                            pass
        except FileNotFoundError:
            pass
        
    def volver(self):
        """Funcion que nos regresa a la ventana secundaria"""
        self.grid_forget()
        self.parent.show_secundaria_frame()

    def manejar_favoritos(self,usuario, evento):
        """Funcion que maneja los eventos favoritos que seleccioara el usuario"""
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
    
    def agregar_favorito(self):
        """Funcion que agrega los eventos favoritos del usuario"""
        try:
            usuario = self.usuario_logeado["User"]
        except TypeError:
            print("No hay ningún usuario logeado")
            return

        evento_seleccionado = self.listbox.get(self.listbox.curselection())
        
        if evento_seleccionado:
            usuario = self.usuario_logeado["User"]
            favorito = self.manejar_favoritos(usuario, evento_seleccionado)
            index = self.listbox.curselection()[0]
            self.listbox.itemconfig(index, bg="yellow", fg="black")
            self.favoritos_indices.append(favorito)