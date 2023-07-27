import customtkinter as ctk
from vistas.ventana_login import Frame
import os
class TourMusical(ctk.CTk):
    """Clase donde representa un programa de musica"""
    def __init__(self):
        super().__init__()
        self.title("Tour Musical")
        self.geometry("330x300")
        self.resizable(False,False)
        self._set_appearance_mode("dark")
        ctk.set_default_color_theme("green")
        self.carpeta()
        self.frame = ctk.CTkFrame(self,width=330,height=300,fg_color="black",bg_color="black")
        self.frame.grid()
        
        self.label = ctk.CTkLabel(self.frame,fg_color="black",text_color="yellow",text="Bienvenido a Tour Music",font=("Open Sans",20))
        self.label.place(x=60,y=70)
        
        self.btn_iniciar = ctk.CTkButton(self.frame,text="Iniciar",text_color="black",command=self.abrir_ventana)
        self.btn_iniciar.place(x=90,y=200)
    
    def abrir_ventana(self):
        
        """Funcion donde abre mediante un boton la ventana del login"""
        ventana = ctk.CTkToplevel(self)
        ventana.title("Login")
        ventana.geometry("300x400+350+20")
        ventana.grid_rowconfigure(0, weight=1)
        ventana.grid_columnconfigure(0, weight=1)
        ventana.configure(fg_color="black")
        app = Frame(ventana)
        app.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        
    
        
    def carpeta(self):
        """Funcion extra para crear una carpeta data si es que no existe"""
        if not os.path.exists("data"):
            os.mkdir("data")
        
        
        
        
if __name__ == "__main__":
    app = TourMusical()
    app.mainloop()
