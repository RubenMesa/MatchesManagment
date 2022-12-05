from Personas import *

class Profesional(Personas):
    def __init__(self, usuario, clave, id, nombrecompleto, rut):
        super().__init__(id,nombrecompleto, rut)
        self.usuario = usuario
        self.clave = clave
        