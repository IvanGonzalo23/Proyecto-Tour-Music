import tkinter as tk
import customtkinter as ctk
import os
from PIL import Image
import json




class Secundaria(ctk.CTkFrame):
    """Clase que representa el Frame de la ventana secundaria del programa"""
    def __init__(self,parent,usuario_logeado=None):
        super().__init__(parent)
        self.parent = parent
        self.usuario_logeado = usuario_logeado
        self.widgets()
        self.listbox()
        self.buttons()
        
        
    def widgets(self):
        """Funcion que crea los widgets para el programa"""
        self.frame= ctk.CTkFrame(self,width=700,height=500,fg_color="#4C333F",bg_color="#4C333F")
        self.frame.grid()
        self.frame_lateral = ctk.CTkFrame(self,width=200,height=500,fg_color="#2F1227",bg_color="#2F1227")
        self.frame_lateral.place(x=0,y=0)
        mi_fuente_titulo = ctk.CTkFont(family="Roboto", size=16, weight="bold")
        
        self.label = ctk.CTkLabel(self,text="Reseñas",text_color="yellow",font=mi_fuente_titulo,fg_color="#4C333F")
        self.label.place(x=370,y=60)
        
    def listbox(self):
        """Funcion que crea el listbox del Frame"""
        self.listbox = tk.Listbox(self,width=60,height=20,background="#131B2E",fg="yellow",font=("Open Sans",10))   
        self.listbox.place(x=260,y=100)
        self.actualizar_listbox()
        self.listbox.bind("<Double-Button-1>", self.mostrar_informacion_reseña)
          
    def actualizar_listbox(self):
        """Funcion que actualiza el listbox para ir agregando las reseñas que se iran creando"""
        try:
            with open("data/reseñas.json", "r", encoding="utf-8") as file:
                reseñas = json.load(file)

            self.listbox.delete(0, tk.END)

            for idx, reseña in enumerate(reseñas, start=1):
                nombre_usuario = reseña["usuario"]
                contenido_reseña = reseña["reseña"]
                evento = reseña["evento"]

                self.listbox.insert(tk.END, f"{idx}. {nombre_usuario.ljust(20)} | Evento: {evento.ljust(30)} | Reseña: {contenido_reseña}")

        except FileNotFoundError:
            pass
        
    def buttons(self):
        """Funcion que crea los botones"""
        self.current_path = os.path.dirname(os.path.realpath(__file__)) 
        self.image_reseña = os.path.join(self.current_path, "../img/reseña.png")
        
        self.imagen_boton_reseña = ctk.CTkImage(Image.open(self.image_reseña),size=(60,60))
        
        self.btn_reseña = ctk.CTkButton(self.frame_lateral,image=self.imagen_boton_reseña,text=None,fg_color="#2F1227",bg_color="#2F1227",cursor="hand2",hover_color="#2F1227",command=lambda:[self.reseñas()])
        self.btn_reseña.place(x=23,y=100)
        
        self.image_favorito = os.path.join(self.current_path,"../img/favoritos.png")
        self.imagen_boton_favoritos = ctk.CTkImage(Image.open(self.image_favorito),size=(60,60))
        
        self.btn_favorito = ctk.CTkButton(self.frame_lateral,image=self.imagen_boton_favoritos,text=None,fg_color="#2F1227",bg_color="#2F1227",cursor="hand2",hover_color="#2F1227",command=lambda:[self.favoritos()])
        self.btn_favorito.place(x=23,y=175)
        
        
        self.image_elegir_favorito = os.path.join(self.current_path,"../img/elegir_favorito.png")
        self.imagen_boton_elegir_favorito = ctk.CTkImage(Image.open(self.image_elegir_favorito),size=(60,60))
        
        self.btn_elegir_favorito = ctk.CTkButton(self.frame_lateral,image=self.imagen_boton_elegir_favorito,text=None,fg_color="#2F1227",bg_color="#2F1227",cursor="hand2",hover_color="#2F1227",command=lambda:[self.ventana_agregar_favoritos()])
        self.btn_elegir_favorito.place(x=23,y=280)
        
        
        self.image_retroceder = os.path.join(self.current_path,"../img/retroceder.png")
        self.imagen_boton_retroceder = ctk.CTkImage(Image.open(self.image_retroceder),size=(60,60))
        
        self.btn_volver = ctk.CTkButton(self.frame_lateral,image=self.imagen_boton_retroceder,text=None,fg_color="#2F1227",hover_color="#2F1227",cursor="hand2",command=lambda:[self.volver()])
        self.btn_volver.place(x=23,y=400)
    
    
    def mostrar_informacion_reseña(self, event):
        """Mostrar la informacion seleccionada"""
        seleccion = self.listbox.curselection()
        if seleccion:
            indice = seleccion[0]
            try:
                with open("data/reseñas.json", "r", encoding="utf-8") as file:
                    reseñas = json.load(file)

                if 0 <= indice < len(reseñas):
                    reseña_seleccionada = reseñas[indice]
                    nombre_usuario = reseña_seleccionada["usuario"]
                    contenido_reseña = reseña_seleccionada["reseña"]
                    evento = reseña_seleccionada["evento"]
                    
                    ventana_info = ctk.CTkToplevel(self)
                    """Se crea un Toplevel para mostrar la informacion"""
                    
                    ventana_info.title("Información de Reseña")
                    ventana_info.geometry("+%d+%d" % (self.winfo_rootx() + 50, self.winfo_rooty() + 50))
                    ventana_info.grab_set() 
                  
                    ventana_info.transient(self)
                    
                    ventana_info.update_idletasks()  
                    width = ventana_info.winfo_width()
                    height = ventana_info.winfo_height()
                    x = (ventana_info.winfo_screenwidth() // 2) - (width // 2)
                    y = (ventana_info.winfo_screenheight() // 2) - (height // 2)
                    ventana_info.geometry(f"+{x}+{y}")    
                    
                    
                    mi_fuente = ctk.CTkFont(family="Open Sans",size=14)
                   
                    ctk.CTkLabel(ventana_info, text="Usuario:",text_color="yellow",font=mi_fuente).grid(row=0, column=0, padx=10, pady=5)
                    ctk.CTkLabel(ventana_info, text=nombre_usuario,text_color="yellow",font=mi_fuente).grid(row=0, column=1, padx=10, pady=5)
                    ctk.CTkLabel(ventana_info, text="Evento:",text_color="yellow",font=mi_fuente).grid(row=1, column=0, padx=10, pady=5)
                    ctk.CTkLabel(ventana_info, text=evento,text_color="yellow",font=mi_fuente).grid(row=1, column=1, padx=10, pady=5)
                    ctk.CTkLabel(ventana_info, text="Reseña:",text_color="yellow",font=mi_fuente).grid(row=2, column=0, padx=10, pady=5)
                    reseña_label = ctk.CTkLabel(ventana_info, text=contenido_reseña, wraplength=400, justify=tk.LEFT,text_color="yellow",font=mi_fuente)
                    reseña_label.grid(row=2, column=1, padx=10, pady=5)
                    
            except FileNotFoundError:
                pass
    
    
        
    def ventana_agregar_favoritos(self):
        """Funcion que abre la ventana para agregar favoritos"""
        self.grid_forget()
        self.parent.show_agregar_favorito()
    
    def reseñas(self):
        """Funcion que abre la ventana de reseñas"""
        self.grid_forget()
        self.parent.show_reseña()
    
    def favoritos(self):
        """Funcion que abre la venana de favoritos"""
        self.grid_forget()
        self.parent.show_favorito()
    
    def volver(self):
        """Funcion que nos devuelve a la ventana principal"""
        self.grid_forget()
        self.parent.show_principal_frame()
        