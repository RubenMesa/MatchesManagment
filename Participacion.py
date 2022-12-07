from conector import DataBase
from Usuario import usuario
from Posicion import posicion
from Partidos import partido

class participacion:
    def __init__(self,id_usuario, id_posicion ,id_partido):
        self.id_usuario = id_usuario
        self.id_posicion = id_posicion
        self.id_partido = id_partido

    def registrarparticipacion(self):
        sql=f'INSERT INTO participacion (usuario_id_usuario,posicion_id_posicion,partido_id_partido) VALUES ("{self.id_usuario}","{self.id_posicion}","{self.id_partido}")'
        db=DataBase()
        db.insert(sql)

    def listar_participacion_partido(self,id):
        sql=f'Select * FROM participacion WHERE id_partido = "{id}"'
        db=DataBase()
        return db.list_dato_uq(sql)
        
    def listartodo_participacion(self):
        tabla = ('participacion')
        db = DataBase()
        db.list(tabla)

    def modificar_participacion(self,id,atri,value):
        sql= f'Update participacion SET {atri} = {value} WHERE id_partido = {id}'
        db=DataBase
        db.modificar(sql)
