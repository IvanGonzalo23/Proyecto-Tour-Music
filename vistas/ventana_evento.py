import customtkinter as ctk
import os

from PIL import Image
ctk.set_appearance_mode("dark")

class Principal(ctk.CTkFrame):
    def __init__(self,parent):
        super().__init__(parent)
        self.parent = parent