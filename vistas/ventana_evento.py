import customtkinter as ctk
ctk.set_appearance_mode("dark")

class Principal(ctk.CTkFrame):
    def __init__(self,parent):
        super().__init__(parent)
        self.parent = parent
        
        