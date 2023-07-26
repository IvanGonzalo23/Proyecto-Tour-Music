import customtkinter as ctk
from modelo.clase_usuarios import Usuario


class Createuser(ctk.CTkFrame):
    """Clase que representa el Frame de la ventana"""
    def __init__(self,parent):
        super().__init__(parent)
        self.parent = parent
        self.labels()
        self.entrys()
        """Label del Frame"""
    def labels(self):    
        label_name = ctk.CTkLabel(self,text="Name:",font=("roboto",14,),text_color="white")
        label_name.place(x=130,y=125)
        label_last_name = ctk.CTkLabel(self,text="Last Name:",font=("roboto",14),text_color="white")
        label_last_name.place(x=130,y=175)
        label_email= ctk.CTkLabel(self,text="Correo electronico",font=("roboto",14),text_color="white")
        label_email.place(x=130,y=225)
        label_password = ctk.CTkLabel(self,text="Password: ",font=("roboto",14),text_color="white")
        label_password.place(x=130,y=275)
        label_user_name = ctk.CTkLabel(self,text="User Name",font=("roboto",14),text_color="white")
        label_user_name.place(x=130,y=325)
    
    def entrys(self):
        """Entry del Frame"""
        self.name_entry = ctk.CTkEntry(self,width=140,height=28)
        self.name_entry.place(x=250,y=125)
        self.last_name_entry= ctk.CTkEntry(self,width=140,height=28)
        self.last_name_entry.place(x=250,y=175)
        self.email_entry = ctk.CTkEntry(self,width=140,height=28)
        self.email_entry.place(x=250,y=225)
        self.password_entry = ctk.CTkEntry(self,width=140,height=28)
        self.password_entry.place(x=250,y=275)
        self.user_name_entry = ctk.CTkEntry(self,width=140,height=28)
        self.user_name_entry.place(x=250,y=325)
        
    def a_json(self):
        usuario = Usuario(self.name_entry.get(), self.last_name_entry.get(), self.email_entry.get(), self.password_entry.get(), self.user_name_entry.get())
        usuario.crear_json("./data/usarios.json")
        