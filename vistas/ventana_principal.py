import customtkinter as ctk
import os
import tkinter as tk
from PIL import Image
from .ventana_eventos import Eventos
from .ventana_buscador import Buscador
from .ventana_historial import Historial_ventana
from .ventana_secundaria import Secundaria


class Principal(ctk.CTkFrame):
    usuario_logeado = None
    def __init__(self,parent):
        super().__init__(parent)
        self.parent = parent
        self.widgets()
        self.listbox()
        self.buttons()
        
        
        if Principal.usuario_logeado is not None:
            self.actualizar_listbox()
        
        
    def widgets(self):
        self.frame= ctk.CTkFrame(self,width=700,height=500,fg_color="#4C333F",bg_color="#4C333F")
        self.frame.grid()
        self.frame_lateral = ctk.CTkFrame(self,width=200,height=500,fg_color="#2F1227",bg_color="#2F1227")
        self.frame_lateral.place(x=0,y=0)
        mi_fuente_titulo = ctk.CTkFont(family="Roboto", size=16, weight="bold")
        
        self.label = ctk.CTkLabel(self,text="Eventos asistidos",text_color="yellow",font=mi_fuente_titulo,fg_color="#4C333F")
        self.label.place(x=370,y=60)
        
    def listbox(self):
        self.listbox = tk.Listbox(self,width=60,height=20,background="#131B2E",fg="yellow",font=("Open Sans",10))   
        self.listbox.place(x=260,y=100)
        
    def actualizar_listbox(self):
        """Función para mostrar los eventos asociados al usuario logeado en el listbox"""
        self.listbox.delete(0, tk.END)  # Limpiamos el listbox

        if Principal.usuario_logeado.get("Eventos_asignados"):
            eventos_asignados = Principal.usuario_logeado["Eventos_asignados"]
            for evento in eventos_asignados:
                nombre = evento.get("Nombre", "")
                artista = evento.get("Artista", "")
                ubicacion = evento.get("ubicacion", "")
                self.listbox.insert(tk.END, f"{nombre} - {artista} - {ubicacion}")

        
        
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
        
        self.image_siguiente = os.path.join(self.current_path,"../img/siguiente.png")
        self.imagen_boton_siguiente = ctk.CTkImage(Image.open(self.image_siguiente),size=(60,60))
        
        self.btn_siguiente = ctk.CTkButton(self.frame_lateral,image=self.imagen_boton_siguiente,text=None,fg_color="#2F1227",hover_color="#2F1227",cursor="hand2",command=lambda:[self.ventana_secundaria()])
        self.btn_siguiente.place(x=23,y=320)
        
    
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
    
    
    def ventana_secundaria(self):
        self.grid_forget()
        self.frame_secundario = Secundaria(self.parent)
        self.frame_secundario.grid()
    
    def volver(self):
        self.grid_forget()
        self.parent.show_login_frame()
