from Conectar import *
class productos:
    def __init__(self,nombre,marca,precio):
        self.marca = marca
        self.nombre = nombre
        self.precio = precio
        

    def creaP(self):
        sql=f'INSERT INTO producto (nombre,marca,precio) VALUES ("{self.nombre}","{self.marca}",{self.precio})'
        db=DataBase()
        db.insert(sql)
    
    def mostrarP():
        tabla='producto'
        db=DataBase()
        db.list(tabla)
        
    def modificarP(id,rut,nombre,apellido,edad,direccion,correo):

        sql=f'UPDATE producto SET rut={rut},nombre="{nombre}",apellido="{apellido}",edad={edad},direccion="{direccion}",correo="{correo}" Where idusuario={id};'
        db=DataBase()
        db.modific(sql)

    

    def eliminarP(id):
        sql=f'DELETE FROM producto WHERE idusuario={id};'
        db=DataBase()
        db.Eliminar(sql)


