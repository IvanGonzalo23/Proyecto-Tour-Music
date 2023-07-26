import json 

class Usuario:
    def __init__(self,name,last_name,email,password,user):
        self.name = name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.user = user
        
    def crear_json(self,archivo):
        diccionario = {
            "Name":self.name,
            "Last_name":self.last_name,
            "Email":self.email,
            "Password":self.password,
            "User":self.user
        }
        with open(archivo, "w") as f:
            json.dump(diccionario, f)