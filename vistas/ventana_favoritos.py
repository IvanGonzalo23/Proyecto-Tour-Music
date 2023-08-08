import tkinter as tk
import customtkinter as ctk
import json
from PIL import Image
import os

class Favoritos(ctk.CTkFrame):
    """Clase que representa el Frame para la ventana de favoritos"""
    def __init__(self, parent, usuario_logeado):
        super().__init__(parent)
        self.parent = parent
        self.usuario_logeado = usuario_logeado
        self.frame = ctk.CTkFrame(self, width=700, height=500, fg_color="#4C333F")
        self.frame.grid()
        self.listbox()
        self.widgets()

    def widgets(self):
        """Funcion que crea los widgets del Frame"""
        mi_fuente = ctk.CTkFont(family="Roboto", size=16, weight="bold")
        self.label = ctk.CTkLabel(self, text="Favoritos", text_color="yellow", bg_color="#4C333F", fg_color="#4C333F", font=mi_fuente)
        self.label.place(x=300, y=50)
        self.current_path = os.path.dirname(os.path.realpath(__file__))
        
        self.image_volver = os.path.join(self.current_path,"../img/retroceder.png")
        self.imagen_boton_volver = ctk.CTkImage(Image.open(self.image_volver),size=(40,40))
        self.btn_volver = ctk.CTkButton(self, text=None, command=lambda: [self.volver()],image=self.imagen_boton_volver,fg_color="#4C333F",bg_color="#4C333F",hover_color="#4C333F",cursor="hand2")
        self.btn_volver.place(x=12, y=440)

    def listbox(self):
        """Funcion que crea un listbox con los eventos favoritos del usuario logeado"""
        self.listbox = tk.Listbox(self, width=60, height=20, background="#131B2E", fg="yellow", font=("Open Sans", 10))
        self.listbox.place(x=150, y=100)
        try:
            with open("./data/favoritos.json", "r") as file:
                fav = json.load(file)
           
            # Filtrar eventos favoritos del usuario logeado
            eventos_favoritos_usuario = [evento_data["evento"] for evento_data in fav if evento_data["usuario"] == self.usuario_logeado["User"]]
            
            # Agregar eventos favoritos al Listbox
            for evento_nombre in eventos_favoritos_usuario:
                self.listbox.insert(tk.END, evento_nombre)
        except FileNotFoundError:
            
            pass

    def volver(self):
        """Funcion que nos devuelve a la ventana secundaria"""
        self.grid_forget()
        self.parent.show_secundaria_frame()

  