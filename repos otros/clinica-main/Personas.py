class Personas:
    #CONSTRUCTOR
    def __init__(self, id, nombrecompleto, rut):

        self.id = id
        self.nombrecompleto = nombrecompleto
        self.rut = rut

    def id(self):
        return self.id
        
    def nombrecompleto(self):
        return self.nombrecompleto

    def rut(self):
        return self.rut
    
    def descripcion(self):
        print("ID: ", self.id, "Nombre: ", self.nombrecompleto, "RUT: ", self.rut)