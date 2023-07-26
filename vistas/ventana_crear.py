import customtkinter as ctk


class Createuser(ctk.CTkFrame):
    """Clase que representa el Frame de la ventana"""
    def __init__(self,parent):
        super().__init__(parent)
        self.parent = parent
        """Label del Frame"""
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
        
        """Entry del Frame"""
        name_entry = ctk.CTkEntry(self,width=140,height=28)
        name_entry.place(x=250,y=125)
        last_name_entry= ctk.CTkEntry(self,width=140,height=28)
        last_name_entry.place(x=250,y=175)
        email_entry = ctk.CTkEntry(self,width=140,height=28)
        email_entry.place(x=250,y=225)
        password_entry = ctk.CTkEntry(self,width=140,height=28)
        password_entry.place(x=250,y=275)
        user_name_entry = ctk.CTkEntry(self,width=140,height=28)
        user_name_entry.place(x=250,y=325)
