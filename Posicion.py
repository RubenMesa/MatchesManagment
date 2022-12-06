from conector import DataBase

class posicion:
    def __init__(self, id, nombre, desc):
        self.id = id
        self.nombre = nombre
        self.desc = desc
    
    def registrarbloque(self):
        sql=f'INSERT INTO posicion (id_posicion,pos_nombre,pos_desc) VALUES ("{self.id}","{self.nombre}","{self.desc}")'
        db=DataBase()
        db.insert(sql)

    def listar_bloque(self,id):
        sql=f'Select * FROM posicion WHERE id_posicion = "{id}"'
        db=DataBase()
        return db.list_dato_uq(sql)
        
    def listartodo_bloque(self):
        tabla = ('posicion')
        db = DataBase()
        db.list(tabla)

    def modificar_bloque(self,id,atri,value):
        sql= f'Update posicion SET {atri} = {value} WHERE id_posicion = {id}'
        db=DataBase
        db.modificar(sql)