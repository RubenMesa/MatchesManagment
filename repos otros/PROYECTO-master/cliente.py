from Usuario import *
from Conectar import *

class cliente(usuario):
    def __init__(self,rut,nombre,apellido,edad,direccion,correo):
        super().__init__(rut,nombre,apellido,edad,direccion,correo)
        
        self.rut = rut
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.direccion = direccion        
        self.correo = correo
    
    def create1(self):
        sql=f'INSERT INTO cliente (rut,nombre,apellido,edad,direccion,correo) VALUES ({self.rut},"{self.nombre}","{self.apellido}",{self.edad},"{self.direccion}","{self.correo}")'
        db=DataBase()
        db.insert(sql)
    def mostrar():
        tabla='cliente'
        db=DataBase()
        db.list(tabla)
        
    def modificar(id,rut,nombre,apellido,edad,direccion,correo):
        cliente.buscador(id)
        sql=f'UPDATE cliente SET rut={rut},nombre="{nombre}",apellido="{apellido}",edad={edad},direccion="{direccion}",correo="{correo}" Where idusuario={id};'
        db=DataBase()
        db.modific(sql)

    def eliminar(id):
        sql=f'DELETE FROM cliente WHERE idcliente={id};'
        db=DataBase()
        db.Eliminar(sql)
    
    
        