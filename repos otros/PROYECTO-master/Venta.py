from Productos import *
class Ventas:
    def __init__(self,codigo,nombre,precio):
        self.codigo=codigo
        self.nombre=nombre
        self.precio=precio
        self.venta=[]

    def agregar1(self):
        self.venta.append(Honda_dio)
        
    def agregar2(self):
        self.venta.append(Honda_CB)
    def agregar3(self):
        self.venta.append(Susuki_ADD)
    def agregar4(self):
        self.venta.append(Susuki_GSX)    
    
    def mostrar_moto(self):
        print("Vehiculos comprados:")
        for n in self.venta:
            print(f"CODIGO: {n.codigo} NOMBRE: {n.nombre} PRECIO: {n.precio} ")

