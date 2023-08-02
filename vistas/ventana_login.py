import customtkinter as ctk
import os
from PIL import Image
current_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.dirname(current_dir)
import sys
sys.path.append(project_dir)
from tkinter import messagebox
import json
from .ventana_crear import Createuser
from .ventana_principal import Principal

class Frame(ctk.CTkFrame):
    """Clase que representa el Frame de la ventana login"""
    def __init__(self,parent):
        super().__init__(parent)
        self.parent = parent
        self.configure(fg_color="black")
        ctk.set_appearance_mode("dark")
        """Frame del programa"""
        self.frame =ctk.CTkFrame(self,width=700,height=500,fg_color="black",bg_color="black")
        self.frame.grid()
        """Icono del programa"""
        self.current_path = os.path.dirname(os.path.realpath(__file__))
        self.image_path = os.path.join(self.current_path, "../img/usuario.png")
        self.bg_image = ctk.CTkImage(
            Image.open(self.image_path),
            size=(100,100)
        )
        self.imagen_inferior = os.path.join(self.current_path,"../img/icono_inferior.png")
        self.icono_inferior = ctk.CTkImage(Image.open(self.imagen_inferior),size=(40,40))
        """Label del Frame"""
        self.label = ctk.CTkLabel(self,image=self.bg_image,text=None)
        self.label.place(x=250,y=40)
        self.label_inferior = ctk.CTkLabel(self,image=self.icono_inferior,text=None)
        self.label_inferior.place(x=0,y=450)
        """Entrys del Frame"""
        self.usuario_entry = ctk.CTkEntry(self,width=140,height=28,border_color="green")
        self.usuario_entry.place(x=230,y=150)
        self.password_entry = ctk.CTkEntry(self,width=140,height=28,border_color="green",show="*")
        self.password_entry.place(x=230,y=220)
        """Botones del Frame"""
        self.login = ctk.CTkButton(self,width=120,height=20,border_color="black",text="Login",fg_color="#2F242C",command=lambda:[self.login_usuario()])
        self.login.place(x=240,y=270)
        self.sign_up = ctk.CTkButton(self,width=120,height=20,border_color="black",text="Sign Up",command=self.crear_cuenta,fg_color="#2F242C")
        self.sign_up.place(x=240,y=330)
        
        
    def login_usuario(self):
            """Función que verifica si el usuario y la contraseña coinciden con los datos del archivo JSON"""
            usuario_ingresado = self.usuario_entry.get()
            password_ingresado = self.password_entry.get()
            with open("./data/usuarios.json", "r") as f:
                usuarios_json = json.load(f)  
            for usuario in usuarios_json:
                if usuario_ingresado == usuario["User"] and password_ingresado == usuario["Password"]:
                    Principal.usuario_logeado = usuario
                    self.ventana_principal()
                    return
            messagebox.showerror("Error de inicio de sesión", "Usuario o contraseña incorrectos")
            
    def crear_cuenta(self): 
        """Funcion para ir al Frame donde se crea los usuarios"""
        self.grid_forget()
        self.fram = Createuser(self.parent)
        self.fram.grid()
        
    def ventana_principal(self):
        """Funcion que crea una ventana para ir a la ventana principal"""
        self.grid_forget()
        self.fram = Principal(self.parent)
        self.fram.grid()