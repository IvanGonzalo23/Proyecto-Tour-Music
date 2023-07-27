import os
current_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.dirname(current_dir)
import sys
sys.path.append(project_dir)
from tkinter import messagebox
from modelo.clase_usuarios import Usuario
import customtkinter as ctk


class Createuser(ctk.CTkFrame):
    """Clase que representa el Frame de la ventana"""
    def __init__(self,parent):
        super().__init__(parent)
        self.parent = parent
        self.labels()
        self.entrys()
        self.buttons()

    def labels(self):
        """Funcion donde ingresa se pone los Labels de la ventana"""    
        label_name = ctk.CTkLabel(self,text="Name:",font=("roboto",14,),text_color="white")
        label_name.place(x=130,y=75)
        label_last_name = ctk.CTkLabel(self,text="Last Name:",font=("roboto",14),text_color="white")
        label_last_name.place(x=130,y=125)
        label_email= ctk.CTkLabel(self,text="Correo electronico",font=("roboto",14),text_color="white")
        label_email.place(x=130,y=175)
        label_password = ctk.CTkLabel(self,text="Password: ",font=("roboto",14),text_color="white")
        label_password.place(x=130,y=225)
        label_user_name = ctk.CTkLabel(self,text="User Name",font=("roboto",14),text_color="white")
        label_user_name.place(x=130,y=275)
    
    def entrys(self):
        """Funcion donde se pone los Entrys de la ventana"""
        self.name_entry = ctk.CTkEntry(self,width=140,height=28)
        self.name_entry.place(x=250,y=75)
        self.last_name_entry= ctk.CTkEntry(self,width=140,height=28)
        self.last_name_entry.place(x=250,y=125)
        self.email_entry = ctk.CTkEntry(self,width=140,height=28)
        self.email_entry.place(x=250,y=175)
        self.password_entry = ctk.CTkEntry(self,width=140,height=28,show="*")
            
        self.password_entry.place(x=250,y=225)
        self.user_name_entry = ctk.CTkEntry(self,width=140,height=28)
        self.user_name_entry.place(x=250,y=275)
        
    def a_json(self):
        """Funcion donde toma los parametros de la clase Usuario del archivo clase_usuario y le da los valores 
        ingresado en los Entrys correspondientes. Para luego ponerlos en un JSON"""
        usuario = Usuario(self.name_entry.get(), self.last_name_entry.get(), self.email_entry.get(), self.password_entry.get(), self.user_name_entry.get())
        usuario.crear_json("./data/usuarios.json")
        if len(self.password_entry.get()) <= 8:
            messagebox.showerror("Error", "La contraseña debe tener más de 8 caracteres.")
            return
        self.parent.destroy()

    def buttons(self):
        """Botones del Frame"""
        button_create = ctk.CTkButton(self,text="Crear",command=self.a_json)
        button_create.place(x=200,y=375)
        button_cancel = ctk.CTkButton(self,text="Cancelar",command=self.parent.destroy)
        button_cancel.place(x=350,y=375)

        