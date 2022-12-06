from conector import DataBase

class tipocancha:

    def __init__(self, id, njugadores, desc ):
            self.id=id
            self.njugadores = njugadores
            self.desc = desc
        
    def registrartipocancha(self):
        sql=f'INSERT INTO tipo_cancha (id_tipo_cancha,numero_jugadores,tcan_desc) VALUES ("{self.id}","{self.njugadores}","{self.desc}")'
        db=DataBase()
        db.insert(sql)

    def listar_tipocancha(self,id):
        sql=f'Select * FROM usuario WHERE id_tipo_cancha = "{id}"'
        db=DataBase()
        return db.list_dato_uq(sql)
        
    def listartodo_tipocancha(self):
        tabla = ('tipo_cancha')
        db = DataBase()
        db.list(tabla)

    def modificar_tipocancha(self,id,atri,value):
        sql= f'Update tipo_cancha SET {atri} = {value} WHERE id_tipo_cancha = {id}'
        db=DataBase
        db.modificar(sql)