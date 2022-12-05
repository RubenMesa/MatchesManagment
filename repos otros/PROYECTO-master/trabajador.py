from Usuario import *
from Conectar import *

class trabajador(usuario):
    def __init__(self, rut, nombre, apellido, edad, direccion, correo,especialidad):
        super().__init__(rut, nombre, apellido, edad, direccion, correo)
        self.especialidad=especialidad

    def creaT(self):
        sql=f'INSERT INTO trabajador (rut,nombre,apellido,edad,direccion,correo,cargo) VALUES ({self.rut},"{self.nombre}","{self.apellido}",{self.edad},"{self.direccion}","{self.correo}","{self.especialidad}")'
        db=DataBase()
        db.insert(sql)
    
    def mostrarT():
        tabla='trabajador'
        db=DataBase()
        db.list(tabla)
        
    def modificarT(id,rut,nombre,apellido,edad,direccion,correo):

        sql=f'UPDATE usuario SET rut={rut},nombre="{nombre}",apellido="{apellido}",edad={edad},direccion="{direccion}",correo="{correo}" Where idusuario={id};'
        db=DataBase()
        db.modific(sql)

    

    def eliminarT(id):
        sql=f'DELETE FROM usuario WHERE idusuario={id};'
        db=DataBase()
        db.Eliminar(sql)