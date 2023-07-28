import customtkinter as ctk
from vistas.ventana_login import Frame
import os
class TourMusical(ctk.CTk):
    """Clase donde representa un programa de musica"""
    def __init__(self):
        super().__init__()
        self.title("Tour Musical")
        self.geometry("500x500")
        self.resizable(False,False)
        self._set_appearance_mode("dark")
        ctk.set_default_color_theme("green")
        self.carpeta()
        self.frame = ctk.CTkFrame(self,width=500,height=569,fg_color="black",bg_color="black")
        self.frame.grid()
        
        self.label = ctk.CTkLabel(self.frame,fg_color="black",text_color="yellow",text="Bienvenido a Tour Music",font=("Open Sans",20))
        self.label.place(x=160,y=200)
        
        self.btn_iniciar = ctk.CTkButton(self.frame,text="Iniciar",text_color="black",command=self.abrir_ventana)
        self.btn_iniciar.place(x=190,y=300)
    
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
    
    
    def carpeta(self):
        """Funcion extra para crear una carpeta data si es que no existe"""
        if not os.path.exists("data"):
            os.mkdir("data")
            
        
        
        
        
        
if __name__ == "__main__":
    app = TourMusical()
    app.mainloop()
