import json
import os

class Usuario:
    last_id = 0
    """Clase que representa un usuario"""
    def __init__(self,name, last_name, email, password, user):
        self.id = Usuario.get_next_id()
        self.name = name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.user = user
        self.data = [] 

    def crear_json(self, archivo):
        """Funcion que crea un objeto JSON"""
        if os.path.exists(archivo):
            with open(archivo, "r",encoding="utf-8") as f:
                self.data = json.load(f)
        
        if len(self.password) > 8 and len(self.name) > 0 and len(self.last_name) > 0 and len(self.email) > 0 and len(self.user) > 0:
            self_dict = self.to_dict()
            self.data.append(self_dict)
            

            with open(archivo, "w") as f:
                json.dump(self.data, f, indent=4)
    @classmethod
    def get_next_id(cls):
        """Función que obtiene el siguiente ID autoincrementado"""
        if cls.last_id == 0:
            if os.path.exists("./data/usuarios.json"):
                # Si hay un archivo de usuarios, obtenemos el ID más grande
                with open("./data/usuarios.json", "r", encoding="utf-8") as f:
                    usuarios = json.load(f)
                    cls.last_id = max(usuario["ID"] for usuario in usuarios) if usuarios else 0
            else:
                # Si no hay archivo de usuarios, el ID comienza desde 1
                cls.last_id = 0

        cls.last_id += 1
        return cls.last_id
            

    def to_dict(self):
        """Funcion que retorna un diccionario"""
        return {
            "ID": self.id,
            "Name": self.name,
            "Last_name": self.last_name,
            "Email": self.email,
            "Password": self.password,
            "User": self.user
        }
