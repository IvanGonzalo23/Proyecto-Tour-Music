import customtkinter as ctk
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.dirname(current_dir)
import sys
sys.path.append(project_dir)
from tkinter import messagebox
import json
from .ventana_crear import Createuser
from .ventana_evento import Principal

class Frame(ctk.CTkFrame):
    """Clase que representa el Frame de la ventana login"""
    def __init__(self,parent):
        super().__init__(parent)
        self.parent = parent
        self.configure(fg_color="black")
        """Frame del programa"""
        self.frame =ctk.CTkFrame(self,width=500,height=500,fg_color="black",bg_color="black")
        self.frame.grid()
        """Label del Frame"""
        self.label = ctk.CTkLabel(self,text="Inicio de Sesion",font=("roboto",20),text_color="white")
        self.label.place(x=170,y=80)
        """Entrys del Frame"""
        self.usuario_entry = ctk.CTkEntry(self,width=140,height=28,border_color="green")
        self.usuario_entry.place(x=170,y=120)
        self.password_entry = ctk.CTkEntry(self,width=140,height=28,border_color="green",show="*")
        self.password_entry.place(x=170,y=170)
        """Botones del Frame"""
        self.login = ctk.CTkButton(self,width=120,height=20,border_color="black",text="Login",fg_color="#2F242C",command=lambda:[self.login_usuario()])
        self.login.place(x=175,y=220)
        self.sign_up = ctk.CTkButton(self,width=120,height=20,border_color="black",text="Sign Up",command=self.crear_cuenta,fg_color="#2F242C")
        self.sign_up.place(x=175,y=270)
        
    def login_usuario(self):
            """Función que verifica si el usuario y la contraseña coinciden con los datos del archivo JSON"""
            usuario_ingresado = self.usuario_entry.get()
            password_ingresado = self.password_entry.get()
            with open("./data/usuarios.json", "r") as f:
                usuarios_json = json.load(f)  
            for usuario in usuarios_json:
                if usuario_ingresado == usuario["User"] and password_ingresado == usuario["Password"]:
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
        ventana_evento = ctk.CTkToplevel(self)
        ventana_evento.resizable(False,False)
        ventana_evento.title("Eventos")
        user_app =  Principal(ventana_evento)
        user_app.configure(fg_color="#060047",height=400,width = 600)
        user_app.grid()