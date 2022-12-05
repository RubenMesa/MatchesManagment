from Personas import *

class Pacientes(Personas):
    def __init__(self, usuario, clave, id, nombrecompleto, rut):
        super().__init__(id,nombrecompleto, rut)
        self.usuario = usuario
        self.clave = clave
    
    def descripciontotal(self):
        print("Usuario: ", self.usuario, "Clave: ", self.clave, "ID: ", self.id, "Nombre: ", self.nombrecompleto, "RUT: ", self.rut)