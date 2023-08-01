import random
import json
import os

class ModeloEvento:
    def __init__(self, usuario_creado):
        self.usuario_creado = usuario_creado

    def cargar_json_eventos(self, archivo):
        """Función para cargar el JSON de eventos desde el archivo"""
        with open(archivo, "r", encoding="utf-8") as f:
            return json.load(f)

    def asignar_eventos_aleatorios(self):
        """Función para asignar eventos aleatorios al usuario"""
        eventos_json = self.cargar_json_eventos("./data/historial_eventos.json")
        eventos_disponibles = eventos_json

        """Asignar eventos al usuario creado"""
        eventos_asignados = random.sample(eventos_disponibles, random.randint(1, len(eventos_disponibles)))

        """Crear un JSON personalizado para el usuario"""
        self.usuario_creado["eventos_asignados"] = eventos_asignados

        usuario_folder = f"data_{self.usuario_creado['User']}"
        if not os.path.exists(usuario_folder):
            os.makedirs(usuario_folder)

        usuario_json_file = os.path.join(usuario_folder, f"{self.usuario_creado['User']}_eventos.json")
        with open(usuario_json_file, "w") as f:
            json.dump(self.usuario_creado, f, indent=4)

        return eventos_asignados
