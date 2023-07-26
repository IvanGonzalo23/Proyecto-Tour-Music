import customtkinter as ctk
from ventana_crear import Createuser


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
        login = ctk.CTkButton(self,width=120,height=20,border_color="black",text="Login",fg_color="#2F242C")
        login.place(x=76,y=220)
        sign_up = ctk.CTkButton(self,width=120,height=20,border_color="black",text="Sign Up",command=lambda:[self.crear_cuenta()],fg_color="#2F242C")
        sign_up.place(x=76,y=270)
    
    def crear_cuenta(self):
        """Funcion que importa el modulo ventana_crear y abre mediante un top level
        la ventana para crear un usuario"""
        ventana = ctk.CTkToplevel(self)
        ventana.resizable(False,False)
        ventana._apply_appearance_mode("dark")
        user_app =  Createuser(ventana)
        user_app.configure(fg_color="black",height=400,width = 600)
        user_app.grid()
        

class Login(ctk.CTk):
    """Clase que representa a un login"""
    def __init__(self):
        super().__init__()
        self.title("Login")
        self.geometry("300x400+350+20")
        self.grid_rowconfigure(0, weight=1)  # configure grid system
        self.grid_columnconfigure(0, weight=1)
        self.configure(fg_color="black")
        self._set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")
        self.my_frame = Frame(self)
        self.my_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")



login = Login()
login.mainloop()
login.resizable(False,False)