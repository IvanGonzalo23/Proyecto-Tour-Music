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
        self.crear_widgets()
        
    def crear_widgets(self):
        """Funcion que crea widgets para el programa"""
        self.label = ctk.CTkLabel(self,text="Inicio de Sesion",font=("roboto",20),text_color="white")
        self.label.place(x=70,y=60)
        self.usuario_entry = ctk.CTkEntry(self,width=140,height=28,border_color="green")
        self.usuario_entry.place(x=68,y=120)
        self.password_entry = ctk.CTkEntry(self,width=140,height=28,border_color="green",show="*")
        self.password_entry.place(x=68,y=170)
        login = ctk.CTkButton(self,width=120,height=20,border_color="black",text="Login",fg_color="#2F242C",command=lambda:[self.login_usuario()])
        login.place(x=76,y=220)
        sign_up = ctk.CTkButton(self,width=120,height=20,border_color="black",text="Sign Up",command=lambda:[self.crear_cuenta()],fg_color="#2F242C")
        sign_up.place(x=76,y=270)
        
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
        """Funcion que importa el modulo ventana_crear y abre mediante un top level
        la ventana para crear un usuario"""
        ventana_principal = self.winfo_toplevel()
        self.pack_forget()
        ventana_principal.withdraw()
        ventana = ctk.CTkToplevel(self)
        ventana.resizable(False,False)
        ventana.title("Crear usuario")
        ventana._apply_appearance_mode("dark")
        user_app =  Createuser(ventana)
        user_app.configure(fg_color="black",height=400,width = 600)
        user_app.grid()
        
    def ventana_principal(self):
        ventana_evento = ctk.CTkToplevel(self)
        ventana_evento.resizable(False,False)
        ventana_evento.title("Eventos")
        ventana_evento._apply_appearance_mode("dark")
        user_app =  Principal(ventana_evento)
        user_app.configure(fg_color="black",height=400,width = 600)
        user_app.grid()