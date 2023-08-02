import tkinter as tk
import customtkinter as ctk
import os
from PIL import Image


class Secundaria(ctk.CTkFrame):
    def __init__(self,parent):
        super().__init__(parent)
        self.parent = parent
        self.widgets()
        self.listbox()
        self.buttons()
        
        
    def widgets(self):
        self.frame= ctk.CTkFrame(self,width=700,height=500,fg_color="#4C333F",bg_color="#4C333F")
        self.frame.grid()
        self.frame_lateral = ctk.CTkFrame(self,width=200,height=500,fg_color="#2F1227",bg_color="#2F1227")
        self.frame_lateral.place(x=0,y=0)
        mi_fuente_titulo = ctk.CTkFont(family="Roboto", size=16, weight="bold")
        
        self.label = ctk.CTkLabel(self,text="Reseñas",text_color="yellow",font=mi_fuente_titulo,fg_color="#4C333F")
        self.label.place(x=370,y=60)
        
    def listbox(self):
        self.listbox = tk.Listbox(self,width=60,height=20,background="#131B2E",fg="yellow",font=("Open Sans",10))   
        self.listbox.place(x=260,y=100)
        
    def buttons(self):
        self.current_path = os.path.dirname(os.path.realpath(__file__)) #paquete donde ira los imagenes
        self.image_reseña = os.path.join(self.current_path, "../img/reseña.png")
        
        self.imagen_boton_reseña = ctk.CTkImage(Image.open(self.image_reseña),size=(60,60))
        
        self.btn_reseña = ctk.CTkButton(self.frame_lateral,image=self.imagen_boton_reseña,text=None,fg_color="#2F1227",bg_color="#2F1227",cursor="hand2",hover_color="#2F1227")
        self.btn_reseña.place(x=23,y=100)
        
        self.image_favorito = os.path.join(self.current_path,"../img/favoritos.png")
        self.imagen_boton_favoritos = ctk.CTkImage(Image.open(self.image_favorito),size=(60,60))
        
        self.btn_favorito = ctk.CTkButton(self.frame_lateral,image=self.imagen_boton_favoritos,text=None,fg_color="#2F1227",bg_color="#2F1227",cursor="hand2",hover_color="#2F1227")
        self.btn_favorito.place(x=23,y=175)
        
        
        self.image_elegir_favorito = os.path.join(self.current_path,"../img/elegir_favorito.png")
        self.imagen_boton_elegir_favorito = ctk.CTkImage(Image.open(self.image_elegir_favorito),size=(60,60))
        
        self.btn_elegir_favorito = ctk.CTkButton(self.frame_lateral,image=self.imagen_boton_elegir_favorito,text=None,fg_color="#2F1227",bg_color="#2F1227",cursor="hand2",hover_color="#2F1227")
        self.btn_elegir_favorito.place(x=23,y=280)
        
        
        self.image_retroceder = os.path.join(self.current_path,"../img/retroceder.png")
        self.imagen_boton_retroceder = ctk.CTkImage(Image.open(self.image_retroceder),size=(60,60))
        
        self.btn_volver = ctk.CTkButton(self.frame_lateral,image=self.imagen_boton_retroceder,text=None,fg_color="#2F1227",hover_color="#2F1227",cursor="hand2",command=lambda:[self.volver()])
        self.btn_volver.place(x=23,y=400)
        
        
    
    def volver(self):
        self.grid_forget()
        self.parent.show_login_frame()
        