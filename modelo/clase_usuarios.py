import json
import os
import random

class Usuario:
    last_id = 0

    def __init__(self, name, last_name, email, password, user):
        self.id = Usuario.get_next_id()
        self.name = name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.user = user
        self.data = []

    def cargar_eventos(self, eventos):
        """Función para cargar los eventos disponibles desde el historial de eventos"""
        self.eventos = eventos

    def asignar_evento_aleatorio(self):
        """Función para asignar eventos aleatorios al usuario"""
        if hasattr(self, 'eventos') and isinstance(self.eventos, list) and len(self.eventos) > 0:
            num_eventos_asignados = random.randint(1, min(6, len(self.eventos))) 
            eventos_asignados = random.sample(self.eventos, num_eventos_asignados)
            self.eventos_asignados = eventos_asignados
        else:
            self.eventos_asignados = []

    def crear_json(self, archivo):
        """Función que crea un objeto JSON con la información del usuario y los eventos asignados"""
        if os.path.exists(archivo):
            with open(archivo, "r", encoding="utf-8") as f:
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
        """Función que retorna un diccionario con los datos del usuario y los eventos asignados"""
        if hasattr(self, 'eventos_asignados'):
            return {
                "ID": self.id,
                "Name": self.name,
                "Last_name": self.last_name,
                "Email": self.email,
                "Password": self.password,
                "User": self.user,
                "Eventos_asignados": self.eventos_asignados
            }
        else:
            return {
                "ID": self.id,
                "Name": self.name,
                "Last_name": self.last_name,
                "Email": self.email,
                "Password": self.password,
                "User": self.user
            }
