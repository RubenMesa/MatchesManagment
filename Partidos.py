from conector import DataBase

class partido:
    def __init__(self,id, fecha ,cancha , bloque):
        self.id = id
        self.fecha = fecha
        self.cancha = cancha
        self.bloque= bloque

    def registrarpartido(self):
        sql=f'INSERT INTO partido (id_partido,par_fecha,bloques_id_bloque,cancha_id_cancha) VALUES ("{self.id}", "{self.fecha}", "{self.cancha}","{self.bloque}")'
        db=DataBase()
        db.insert(sql)

    def listar_partido_partido(self,id):
        sql=f'Select * FROM partido WHERE id_partido = "{id}"'
        db=DataBase()
        return db.list_dato_uq(sql)
        
    def listartodo_partido(self):
        tabla = ('partido')
        db = DataBase()
        db.list(tabla)

    def modificar_partido(self,id,atri,value):
        sql= f'Update partido SET {atri} = {value} WHERE id_partido = {id}'
        db=DataBase
        db.modificar(sql)

    def listar_partido_jugador(self,id):
        sql=f'Select * FROM partido WHERE id_partido = (Select id_partido from participaciones where id_usuario = {id});'
        db=DataBase()
        return db.list_dato_uq(sql)