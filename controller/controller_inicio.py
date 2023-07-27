
class Controlador:
    def __init__(self,app):
        self.app = app 


    def volver_login(self):
            self.app.grid(row=0, column=0, sticky="ns")
