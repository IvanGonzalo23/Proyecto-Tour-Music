import customtkinter as ctk
import tkinter as tk
import json
from tkinter import messagebox
from tkinter import ttk
from PIL import Image
import os

class Reseña(ctk.CTkFrame):
    """Clase que representa el Frame para crear una reseña"""
    def __init__(self, parent, usuario_logeado=None):
        super().__init__(parent)
        self.usuario_logeado = usuario_logeado
        self.parent = parent
        self.widgets()
        print("usuario: ",self.usuario_logeado["User"]," ingreso a reseñas")

    def widgets(self):
        """Funcion que crea los widgets del programa"""
        self.frame = ctk.CTkFrame(self, width=700, height=500,fg_color="#4C333F",bg_color="#4C333F")
        self.frame.grid()
        
        self.current_path = os.path.dirname(os.path.realpath(__file__)) 

        with open("data/historial_eventos.json", "r",encoding="utf-8") as file:
            eventos_historial = json.load(file)

        eventos_artistas = [f"{evento['Nombre']} - {evento['Artista']}" for evento in eventos_historial]

        self.combobox_evento = ctk.CTkComboBox(self, values=eventos_artistas)
        self.combobox_evento.place(x=300, y=20)

        self.text_resena = tk.Text(self, height=23,width=40, wrap=tk.WORD,background="#131B2E",font=("Open Sans",10),fg="yellow")
        self.text_resena.place(x=200, y=70)
        
        self.guardar_image = os.path.join(self.current_path, "../img/guardar.png")
        self.btn_imagen_guardar = ctk.CTkImage(Image.open(self.guardar_image),size=(60,60))
        
        self.btn_guardar = ctk.CTkButton(self, text=None, command=self.guardar_resena,image=self.btn_imagen_guardar,fg_color="#4C333F",bg_color="#4C333F",hover_color="#4C333F",cursor="hand2")
        self.btn_guardar.place(x=540, y=420)
        
        self.volver_image = os.path.join(self.current_path, "../img/retroceder.png")
        self.btn_imagen_volver = ctk.CTkImage(Image.open(self.volver_image),size=(60,60))
        
        self.btn_volver = ctk.CTkButton(self,text=None,command=self.volver,image=self.btn_imagen_volver,fg_color="#4C333F",bg_color="#4C333F",hover_color="#4C333F",cursor="hand2")
        self.btn_volver.place(x=15,y=420)

    
    def guardar_resena(self):
        """Funcion que guarda la reseña ingresada"""
        try:
            evento_seleccionado = self.combobox_evento.get()
            try:
                evento, artista = evento_seleccionado.split(" -")
            
            except:
                messagebox.showerror("Error","Por favor, escoga una opcion")

            resenia = self.text_resena.get("1.0", tk.END).strip()
            if not resenia:
                messagebox.showerror("Error", "Por favor, ingresa una reseña.")
                return

            nombre_usuario = self.usuario_logeado["User"]  # Obtener el nombre del usuario

            nueva_reseña = {
                "usuario": nombre_usuario,
                "evento": evento,
                "artista": artista,
                "reseña": resenia
            }

            try:
                with open("data/reseñas.json", "r",encoding="utf-8") as file:
                    reseñas = json.load(file)
            except FileNotFoundError:
                reseñas = []

            reseñas.append(nueva_reseña)
            
            with open("data/reseñas.json", "w",encoding="utf-8") as file:
                json.dump(reseñas, file,indent=4,ensure_ascii=False)

            messagebox.showinfo("Éxito", "Reseña guardada correctamente.")
            self.text_resena.delete("1.0", tk.END)
        except:
            pass

    
    def volver(self):
        """Funcion para volver a la ventana anterior"""
        self.grid_forget()
        self.parent.show_secundaria_frame()