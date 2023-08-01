import os
current_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.dirname(current_dir)
import sys
sys.path.append(project_dir)
from tkinter import messagebox
from modelo.clase_usuarios import Usuario
from PIL import Image
import customtkinter as ctk
from modelo.clase_evento_usuario import ModeloEvento
import json

class Createuser(ctk.CTkFrame):
    """Clase que representa el Frame de la ventana"""
    def __init__(self,parent):
        super().__init__(parent)
        self.parent = parent
        self.configure(fg_color="black")
        self.crear_widgets()
        
    def crear_widgets(self):
        """Funcion que crea widgets"""
        ventana = ctk.CTkFrame(self,width=700,height=500,fg_color="black",bg_color="black") # tamaño del frame
        ventana.grid()

        """Imagenes de los buttons"""
        self.current_path = os.path.dirname(os.path.realpath(__file__)) #paquete donde ira los imagenes
        self.creacion_image = os.path.join(self.current_path, "../img/creacion.png")
        self.icono_creacion = ctk.CTkImage(Image.open(self.creacion_image),size=(60,60))
        
        self.retroceso_image = os.path.join(self.current_path,"../img/atras.png")
        self.icono_retroceso = ctk.CTkImage(Image.open(self.retroceso_image),size=(60,60))
        
        
        """Label del Frame"""
        label_name = ctk.CTkLabel(self,text="Name:",font=("roboto",14,),text_color="yellow")
        label_name.place(x=130,y=75)
        label_last_name = ctk.CTkLabel(self,text="Last Name:",font=("roboto",14),text_color="yellow")
        label_last_name.place(x=130,y=125)
        label_email= ctk.CTkLabel(self,text="Correo electronico",font=("roboto",14),text_color="yellow")
        label_email.place(x=130,y=175)
        label_password = ctk.CTkLabel(self,text="Password: ",font=("roboto",14),text_color="yellow")
        label_password.place(x=130,y=225)
        label_user_name = ctk.CTkLabel(self,text="User Name",font=("roboto",14),text_color="yellow")
        label_user_name.place(x=130,y=275)

        """Entry del Frame"""
        self.name_entry = ctk.CTkEntry(self,width=140,height=28,border_color="#461959")
        self.name_entry.place(x=250,y=75)
        self.last_name_entry= ctk.CTkEntry(self,width=140,height=28,border_color="#461959")
        self.last_name_entry.place(x=250,y=125)
        self.email_entry = ctk.CTkEntry(self,width=140,height=28,border_color="#461959")
        self.email_entry.place(x=250,y=175)
        self.password_entry = ctk.CTkEntry(self,width=140,height=28,show="*",border_color="#461959")
        self.password_entry.place(x=250,y=225)
        self.user_name_entry = ctk.CTkEntry(self,width=140,height=28,border_color="#461959")
        self.user_name_entry.place(x=250,y=275)

        """Button del Frame"""
        self.btn_volver = ctk.CTkButton(self,text=None,command=self.volver,image=self.icono_retroceso,fg_color="black",hover_color="black",cursor="hand2")
        self.btn_volver.place(x=0,y=400)
        self.btn_crear = ctk.CTkButton(self,text=None,command=self.crear_usuario,image=self.icono_creacion,fg_color="black",hover_color="black",cursor="hand2")
        self.btn_crear.place(x=450,y=400)


    def crear_usuario(self):
        """Funcion donde toma los parametros de la clase Usuario del archivo clase_usuario y le da los valores 
        ingresado en los Entrys correspondientes. Para luego ponerlos en un JSON"""
        usuario = Usuario(self.name_entry.get(), self.last_name_entry.get(), self.email_entry.get(), self.password_entry.get(), self.user_name_entry.get())
        usuario.crear_json("./data/usuarios.json")
        if len(self.password_entry.get()) <= 8:
            messagebox.showerror("Error", "La contraseña debe tener más de 8 caracteres.")
            return
        
        if len(self.name_entry.get()) == 0 or len(self.last_name_entry.get()) == 0 or len(self.email_entry.get()) == 0 or len(self.password_entry.get()) == 0 or len(self.user_name_entry.get()) == 0:
            messagebox.showerror("Error", "Por favor llene todos los campos.")
            return
        
        modelo_evento = ModeloEvento(usuario.to_dict()) 
        modelo_evento.asignar_eventos_aleatorios()
        
        messagebox.showinfo("Usuario creado", "El usuario ha sido creado con éxito.")
        self.volver()
        
    def volver(self):
        """Funcion para volver a la ventana anterior"""
        self.grid_forget()
        self.parent.show_login_frame()  