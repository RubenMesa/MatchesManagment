from conector import DataBase

class cancha:
    def __init__(self, nombre, tamano, ubicacion, tipocancha):
        self.nombre = nombre
        self.tamano = tamano
        self.ubicacion= ubicacion
        self.tipocancha = tipocancha
    
    def registrarcancha(self):
        sql=f'INSERT INTO cancha (can_nombre,ubicacion,tipo_cancha_id_tipo_cancha) VALUES ("{self.nombre}","{self.tamano}","{self.ubicacion}",{self.tipocancha})'
        db=DataBase()
        db.insert(sql)

    def listar_canchar(self,id):
        sql=f'Select * FROM cancha WHERE id_cancha = "{id}"'
        db=DataBase()
        return db.list_dato_uq(sql)
            
    def listartodo_cancha(self):
        tabla = ('cancha')
        db = DataBase()
        db.list(tabla)

    def modificar_cancha(self,id,atri,value):
        sql= f'Update cancha SET {atri} = {value} WHERE id_cancha = {id}'
        db=DataBase
        db.modificar(sql)

    def eliminar_cancha(id):
        sql= f'DELETE FROM cancha WHERE id_cancha = {id}'
        db=DataBase()
        db.eliminar(sql)
