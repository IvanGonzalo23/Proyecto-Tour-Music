import customtkinter as ctk
import os
import tkinter as tk
from PIL import Image
from .ventana_eventos import Eventos
from .ventana_buscador import Buscador
from .ventana_historial import Historial_ventana


class Principal(ctk.CTkFrame):
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
        
        
    def listbox(self):
        self.listbox = tk.Listbox(self,width=60,height=20,background="#131B2E")   
        self.listbox.place(x=260,y=100)
        
        
    def buttons(self):
        """funcion que crea los botones del Frame"""
        self.current_path = os.path.dirname(os.path.realpath(__file__)) #paquete donde ira los imagenes
        self.image_path = os.path.join(self.current_path, "../img/evento.png")
        """Se toma las imagenes del directorio img para usarlas como botones"""
        self.bg_image = ctk.CTkImage(
            Image.open(self.image_path),
            size=(60,60)
        )
        self.btn_indice = ctk.CTkButton(self.frame_lateral,image=self.bg_image,text=None,fg_color="#2F1227",hover_color="#2F1227",cursor="hand2",command=lambda:[self.evento_disponibles()])
        self.btn_indice.place(x=23,y=75)
        
        self.image_buscador = os.path.join(self.current_path, "../img/busqueda.png")
        
        self.imagen_boton_buscador = ctk.CTkImage(Image.open(self.image_buscador),size=(60,60))
        
        self.btn_buscador = ctk.CTkButton(self.frame_lateral,image=self.imagen_boton_buscador,text=None,fg_color="#2F1227",hover_color="#2F1227",cursor="hand2",command=lambda:[self.buscador()])
        self.btn_buscador.place(x=23,y=150)
        
        self.image_historial =  os.path.join(self.current_path, "../img/historial.png")
        
        self.imagen_boton_historial = ctk.CTkImage(Image.open(self.image_historial),size=(60,60))
        
        self.btn_historial = ctk.CTkButton(self.frame_lateral,image=self.imagen_boton_historial,text=None,fg_color="#2F1227",hover_color="#2F1227",cursor="hand2",command=lambda:[self.historial()])
        self.btn_historial.place(x=23,y=225)
        
        self.image_retroceder = os.path.join(self.current_path,"../img/retroceder.png")
        self.imagen_boton_retroceder = ctk.CTkImage(Image.open(self.image_retroceder),size=(60,60))
        
        self.btn_volver = ctk.CTkButton(self.frame_lateral,image=self.imagen_boton_retroceder,text=None,fg_color="#2F1227",hover_color="#2F1227",cursor="hand2",command=lambda:[self.volver()])
        self.btn_volver.place(x=23,y=400)
    
    
    def evento_disponibles(self):
        self.grid_forget()
        self.fram = Eventos(self.parent)
        self.fram.grid()
    
    
    def buscador(self):
        self.grid_forget()
        self.frame = Buscador(self.parent)
        self.frame.grid()
        
    def historial(self):
        self.grid_forget()
        self.fra = Historial_ventana(self.parent)
        self.fra.grid()
    
    def volver(self):
        self.grid_forget()
        self.parent.show_login_frame()
