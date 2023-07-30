import json
import os

class Historial:
    def __init__(self, nombre, artista, ubicacion, genero, fecha, latitud,longitud,direccion,hora,imagen,id=None):
        self.id = id
        self.nombre = nombre
        self.artista = artista
        self.genero = genero
        self.ubicacion = ubicacion
        self.fecha = fecha
        self.latitud = latitud
        self.longitud = longitud
        self.direccion = direccion
        self.hora = hora
        self.imagen = imagen
    
    @classmethod
    def cargar(cls):
        archivo_json = os.path.join("data", "historial_eventos.json")
        eventos = []
        if os.path.exists(archivo_json):
            with open(archivo_json, 'r') as file:
                data = json.load(file)
                for item in data:
                    evento = cls(
                        nombre=item.get('Nombre'),
                        artista=item.get('Artista'),
                        ubicacion=item.get('ubicacion'),
                        genero=item.get('Genero'),
                        fecha=item.get('Fecha'),
                        latitud=item.get("latitud"),
                        longitud=item.get("longitud"),
                        direccion=item.get("direccion"),
                        hora=item.get("hora"),
                        imagen= item.get("imagen"),
                        id=item.get('Id')
                    )
                    eventos.append(evento)
        return eventos
