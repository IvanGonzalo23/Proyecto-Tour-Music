import customtkinter as ctk
from vistas.ventana_login import Frame
from vistas.ventana_principal import Principal
from vistas.ventana_secundaria import Secundaria
import os
from PIL import Image
class TourMusical(ctk.CTk):
    """Clase donde representa un programa de musica"""
    def __init__(self):
        super().__init__()
        self.title("Tour Musical")
        self.geometry("700x500")
        self.resizable(False,False) 
        self._set_appearance_mode("dark")
        self.iconbitmap("img/logo.ico")
        ctk.set_default_color_theme("green")
        self.carpeta()
        self.frame = ctk.CTkFrame(self,width=700,height=500,fg_color="black",bg_color="black")
        self.frame.grid()
        
        self.paquete_imagenes = os.path.dirname(os.path.realpath(__file__))
        self.imagen = os.path.join(self.paquete_imagenes,"img/boton-de-encendido.png")
        self.imagen_boton_encendido = ctk.CTkImage(Image.open(self.imagen),size=(60,60))
        
        mi_fuente_titulo = ctk.CTkFont(family="Roboto", size=20, weight="bold")
        texto = "''La musica constituye una revelacion mas alta que ninguna filosofia''\nLudwig Van Beethoven"
        
        fuente_frase = ctk.CTkFont(family="Franklin Gothic Book",size=12,weight="bold")
        self.label = ctk.CTkLabel(self.frame,fg_color="black",text_color="yellow",text="Bienvenido a Tour Musical",font=mi_fuente_titulo)
        self.label.place(x=210,y=130)
        
        self.label_frase = ctk.CTkLabel(self.frame,fg_color="black",text_color="yellow", text=texto,font=fuente_frase)
        self.label_frase.place(x=134,y=200)
        
        self.btn_iniciar = ctk.CTkButton(self.frame,text=None,fg_color="black",bg_color="black",hover_color="black",cursor="hand2",command=self.abrir_ventana,image=self.imagen_boton_encendido)
        self.btn_iniciar.place(x=250,y=300)
        
    
    def abrir_ventana(self):
        """Funcion donde abre mediante un boton la ventana del login"""
        self.frame.grid_forget()
        self.frame = Frame(self)
        self.frame.grid()
    
    
    def show_login_frame(self):
        """Función para mostrar la ventana de inicio de sesión"""
        if hasattr(self, 'login_frame'):
            self.login_frame.destroy()
        self.login_frame = Frame(self)
        self.login_frame.grid()    
    
    
    def show_principal_frame(self):
        """Funcion para mostrar la ventana principal"""
        if hasattr(self,"principal_frame"):
            self.principal_frame.destroy()
        self.principal_frame = Principal(self)
        self.principal_frame.grid()
    
    def carpeta(self):
        """Funcion extra para crear una carpeta data si es que no existe"""
        if not os.path.exists("data"):
            os.mkdir("data") 
    
    def show_secundaria_frame(self):
        """Funcion para mostrar la ventana principal"""
        if hasattr(self,"secundaria_frame"):
            self.secundaria_frame.destroy()
        self.secundaria_frame = Secundaria(self)
        self.secundaria_frame.grid()
    
        
               
if __name__ == "__main__":
    app = TourMusical()
    app.mainloop()
