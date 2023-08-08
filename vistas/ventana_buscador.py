import tkinter as tk
import customtkinter as ctk
from modelo.clase_eventos_disponibles import Eventos_disponibles
from tkinter import messagebox
from PIL import Image,ImageTk
import tkintermapview
import os

class Buscador(ctk.CTkFrame):
    """Clase que representa un buscador de eventos"""
    def __init__(self,parent):
        super().__init__(parent)
        self.parent = parent
        self.frame= ctk.CTkFrame(self,width=700,height=500,fg_color="#4C333F",bg_color="#4C333F")
        self.frame.grid()
        
        """Label del Frame"""
        self.label_nombre_evento = ctk.CTkLabel(self,text="Nombre del evento",text_color="yellow",fg_color="#4C333F")
        self.label_nombre_evento.place(x=100,y=100)
        
        self.label_artista = ctk.CTkLabel(self, text="Nombre del Artista", text_color="yellow",fg_color="#4C333F")
        self.label_artista.place(x=100,y=200)
        
        self.label_genero = ctk.CTkLabel(self,text="Genero Musical",text_color="yellow",fg_color="#4C333F")
        self.label_genero.place(x=100,y=300)
        
        self.label_hora = ctk.CTkLabel(self,text="Horario de inicio",text_color="yellow",fg_color="#4C333F")
        self.label_hora.place(x=100,y=400)
        
        self.label_direccion = ctk.CTkLabel(self,text="Direccion del evento",text_color="yellow",fg_color="#4C333F")
        self.label_direccion.place(x=100,y=500)
        
        """Iconos de los botones"""
        
        self.current_path = os.path.dirname(os.path.realpath(__file__))
        self.image_buscador = os.path.join(self.current_path, "../img/busqueda.png")
        self.imagen_boton_buscador = ctk.CTkImage(Image.open(self.image_buscador),size=(40,40))
        
        self.image_retroceder = os.path.join(self.current_path,"../img/retroceder.png")
        self.imagen_boton_retroceder = ctk.CTkImage(Image.open(self.image_retroceder),size=(40,40))
        
        """Entry del Frame"""
        self.entry_nombre_evento = ctk.CTkEntry(self,width=140,height=28,border_color="#38ad7e")
        self.entry_nombre_evento.place(x=250,y=100)
        
        self.entry_nombre_artista = ctk.CTkEntry(self,width=140,height=28,border_color="#38ad7e")
        self.entry_nombre_artista.place(x=250,y=200)
        
        self.entry_genero = ctk.CTkEntry(self,width=140,height=28,border_color="#38ad7e")
        self.entry_genero.place(x=250,y=300)
        
        self.entry_hora = ctk.CTkEntry(self,width=140,height=28,border_color="#38ad7e")
        self.entry_hora.place(x=250,y=400)
        
        self.entry_ubicacion = ctk.CTkEntry(self,width=140,height=28,border_color="#38ad7e")
        self.entry_ubicacion.place(x=250,y=500)
        
        """Botones del Frame"""
        self.btn_volver = ctk.CTkButton(self,image=self.imagen_boton_retroceder,text=None,fg_color="#4C333F",hover_color="#4C333F",cursor="hand2",command=lambda:[self.volver()])
        self.btn_volver.place(x=0,y=450)
        
        self.btn_buscador = ctk.CTkButton(self,image=self.imagen_boton_buscador,text=None,fg_color="#4C333F",hover_color="#4C333F",cursor="hand2",command=lambda:[self.evento_encontrado()])
        self.btn_buscador.place(x=570,y=450)
        
    def volver(self):
        """Funcion para volver a la ventana principal"""
        self.grid_forget()
        self.parent.show_principal_frame()
        
    def evento_encontrado(self):
        """Funcion donde compara lo ingresado en los entrys con el historial de eventos
        Si encuentra una similitud se mostrara la informacion del evento"""
        self.nombre_ingresado = self.entry_nombre_evento.get()
        self.artista_ingresado = self.entry_nombre_artista.get()
        self.genero_ingresado = self.entry_genero.get()
        self.hora_ingresado = self.entry_hora.get()
        self.ubicacion_ingresado = self.entry_ubicacion.get()
        
        self.eventos = Eventos_disponibles.cargar()
        self.eventos_encontrados = []
        
        for self.evento in self.eventos:
            if self.evento.nombre == self.nombre_ingresado or self.evento.artista == self.artista_ingresado or self.evento.genero == self.genero_ingresado or self.evento.hora == self.hora_ingresado or self.evento.ubicacion == self.ubicacion_ingresado:
               self.eventos_encontrados.append(self.evento)
        
        if len(self.eventos_encontrados) > 0: 
            messagebox.showinfo("Evento encontrado","Se encontraron los siguientes eventos:")
            self.mostrar_evento_encontrado()
            
        else:
            messagebox.showerror("No se encontro el evento","No se encontro similitud con lo ingresado")
            
        self.entry_nombre_evento.delete(0,tk.END)
        self.entry_nombre_artista.delete(0,tk.END)
        self.entry_genero.delete(0,tk.END)
        self.entry_hora.delete(0,tk.END)
        self.entry_ubicacion.delete(0,tk.END)
        
    def mostrar_frame(self):
        """Funcion que abre la ventana que muestra el evento encontrado"""
        self.grid_forget()
        self.mostrar_evento_encontrado()

    
    def mostrar_evento_encontrado(self):
        """Funcion que muestra una ventana mediante Toplevel en donde esta tiene
        la informacion del evento encontrado"""
        if len(self.eventos_encontrados) > 0:
            for eventos in self.eventos_encontrados: 

                top = tk.Toplevel(self)
                top.title("Evento Encontrado")
                top.geometry("700x500")
                frame = ctk.CTkFrame(top,width=700,height=500,fg_color="black")
                frame.grid()

                label_nombre = ctk.CTkLabel(frame, text=eventos.nombre)
                label_nombre.place(x=0,y=60)

                label_artista = ctk.CTkLabel(frame, text=eventos.artista)
                label_artista.place(x=0,y=120)

                label_genero = ctk.CTkLabel(frame, text=eventos.genero)
                label_genero.place(x=0,y=180)

                label_hora = ctk.CTkLabel(frame, text=eventos.hora)
                label_hora.place(x=0,y=240)

                label_ubicacion = ctk.CTkLabel(frame, text=eventos.ubicacion)
                label_ubicacion.place(x=0,y=300)

                label_fecha = ctk.CTkLabel(frame, text=eventos.fecha)
                label_fecha.place(x=0,y=360)

                label_direccion = ctk.CTkLabel(frame, text=eventos.direccion)
                label_direccion.place(x=0,y=420)

                info_mapa=f"{eventos.direccion} - {eventos.ubicacion}"
                latitud = eventos.latitud 
                longitud = eventos.longitud 
               
            
                mapa = tkintermapview.TkinterMapView(frame, width=700, height=500, corner_radius=0)
                mapa.set_position(-24.790383333333335, -65.41429999999999723)
                mapa.set_zoom(16)
                mapa.place(x=200,y=0)
                mapa.set_tile_server("https://mt1.google.com/vt/lyrs=m@221097413&x={x}&y={y}&z={z}")
                mapa.set_marker(latitud, longitud, info_mapa,)
                
                
                if  latitud and longitud is not None:
                    mapa.set_position(latitud,longitud)
                    mapa.set_zoom(18)
                else:
                    messagebox.showerror("No se encontro el evento", "No se encontro similitud con lo ingresado")


        
        