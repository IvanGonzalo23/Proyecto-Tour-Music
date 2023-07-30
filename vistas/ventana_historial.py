import customtkinter as ctk
import tkinter as tk
from tkintermapview import TkinterMapView
from modelo.clase_historial import Historial
from PIL import Image
import os

class Historial_ventana(ctk.CTkFrame):
    """Clase que representa la ventana de eventos"""
    def __init__(self,parent):
        super().__init__(parent)
        self.parent = parent
        self.widgets()
        
    def widgets(self):
        """Funcion que sirve para poner los widgets del Frame"""
        
        self.frame = ctk.CTkFrame(self, width=700, height=500, fg_color="black") #Frame
        self.frame.grid()
        
        self.current_path = os.path.dirname(os.path.realpath(__file__))
        self.image_retroceder = os.path.join(self.current_path,"../img/atras.png")
        self.imagen_boton_retroceder = ctk.CTkImage(Image.open(self.image_retroceder),size=(60,60))
        

        
        
        
        
        mi_fuente_titulo = ctk.CTkFont(family="Roboto", size=16, weight="bold")
        """Titulo del historial"""
        self.titulo_label = ctk.CTkLabel(self.frame,text="Historial",text_color="yellow",font=mi_fuente_titulo)
        self.titulo_label.place(x=0,y=40)
        
        """Listbox"""
        self.listbox = tk.Listbox(self.frame, justify="left", width=30, height=20,fg="yellow",bg="black",cursor="hand2")
        self.listbox.place(x=0, y=70)
        
        """Evento del listbox"""
        self.listbox.bind("<<ListboxSelect>>", self.mostrar_evento)
        self.listbox.bind("<Double-Button-1>", self.ver_info_evento)
        """Botones del frame"""
        self.btn = ctk.CTkButton(self,text=None,image=self.imagen_boton_retroceder,fg_color="black",hover_color="black",cursor="hand2",bg_color="black",command=lambda:[self.volver()])
        self.btn.place(x=0,y=400)
        
        """Mapa con tkintermapview"""
        self.mapa = TkinterMapView(self.frame, width=700, height=500, corner_radius=0)
        self.mapa.set_position(-24.790383333333335, -65.41429999999999723)
        self.mapa.set_zoom(16)
        self.mapa.place(x=200,y=0)
        self.mapa.set_tile_server("https://mt1.google.com/vt/lyrs=m@221097413&x={x}&y={y}&z={z}")

        
        """Se cargan los eventos musicales del json eventos_disponibles"""
        self.eventos = Historial.cargar()        
        
        """Se hace un recorrido para insertar los nombres en el listbox y en el marcador del map"""
        for self.evento in self.eventos:
            info_evento = f"{self.evento.nombre} - {self.evento.artista}"
            self.listbox.insert(tk.END, info_evento)
            info_mapa=f"{self.evento.direccion} - {self.evento.ubicacion}"
            latitud = self.evento.latitud 
            longitud = self.evento.longitud 
            self.mapa.set_marker(latitud, longitud, info_mapa)
            
            
    def mostrar_evento(self, event):
        """Funcion que muestra los eventos marcados en el map"""
        index = self.listbox.curselection()[0]
        evento = self.eventos[index]
        self.mapa.set_position(evento.latitud, evento.longitud)
        self.mapa.set_zoom(18)
    
    def volver(self):
        """Funcion para volver a la ventana anterior"""
        self.grid_forget()
        self.parent.show_principal_frame()
        
        
    def ver_info_evento(self, event):
        """Funcion que toma la informacion seleccionada del evento"""
        
        index = self.listbox.curselection()[0]
        
        evento = self.eventos[index]
       
        info_toplevel = ctk.CTkToplevel(self.frame)
        info_toplevel.geometry("500x520")
        info_toplevel.resizable(False,False)
        
        mi_fuente = ctk.CTkFont(family="Open Sans", size=12, weight="bold")
        
        nombre_label = ctk.CTkLabel(info_toplevel, font=mi_fuente , text=f"Evento: {evento.nombre}")
        nombre_label.place(x=0,y=25)
       
        artista_label = ctk.CTkLabel(info_toplevel, font=mi_fuente, text=f"Artista: {evento.artista}")
        artista_label.place(x=0,y=75)
        
        fecha_label = ctk.CTkLabel(info_toplevel, font=mi_fuente, text=f"Fecha: {evento.fecha}")
        fecha_label.place(x=0,y=125)
        
        hora_label = ctk.CTkLabel(info_toplevel, font=mi_fuente, text=f"Hora: {evento.hora}")
        hora_label.place(x=0,y=175)
        
        hora_label = ctk.CTkLabel(info_toplevel, font=mi_fuente, text=f"Edificio: {evento.ubicacion}")
        hora_label.place(x=0,y=225)
        
        direccion_label = ctk.CTkLabel(info_toplevel, font=mi_fuente ,text=f"Direccion {evento.direccion}")
        direccion_label.place(x=0,y=275)
        
        self.current_path = os.path.dirname(os.path.realpath(__file__))
        self.imagen_encontrada = evento.imagen
        self.image_path = os.path.join(self.current_path, self.imagen_encontrada)
        self.bg_image = ctk.CTkImage(
            Image.open(self.image_path),
            size=(200,200)
        )
        
        imagen_label = ctk.CTkLabel(info_toplevel,image=self.bg_image,text=None)
        imagen_label.place(x=100,y=300)
