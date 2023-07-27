import json
import os

class Usuario:
    """Clase que representa un usuario"""
    def __init__(self, name, last_name, email, password, user):
        self.name = name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.user = user
        self.data = [] 

    def crear_json(self, archivo):
        """Funcion que crea un objeto JSON"""
        if os.path.exists(archivo):
            with open(archivo, "r") as f:
                self.data = json.load(f)
        
        if len(self.password) > 8:
            self_dict = self.to_dict()
            self.data.append(self_dict)

            with open(archivo, "w") as f:
                json.dump(self.data, f, indent=4)
            

    def to_dict(self):
        """Funcion que retorna un diccionario"""
        return {
            "Name": self.name,
            "Last_name": self.last_name,
            "Email": self.email,
            "Password": self.password,
            "User": self.user
        }
