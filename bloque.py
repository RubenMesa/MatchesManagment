from conector import DataBase

class bloque:
    def __init__(self, id, numero, desc):
        self.id = id
        self.numero = numero
        self.desc = desc
    
    def registrarbloque(self):
        sql=f'INSERT INTO bloques (id_bloque,blo_num,blo_desc) VALUES ("{self.id}","{self.numero}","{self.desc}")'
        db=DataBase()
        db.insert(sql)

    def listar_bloque(self,id):
        sql=f'Select * FROM bloques WHERE id_bloques = "{id}"'
        db=DataBase()
        return db.list_dato_uq(sql)
        
    def listartodo_bloque(self):
        tabla = ('bloques')
        db = DataBase()
        db.list(tabla)

    def modificar_bloque(self,id,atri,value):
        sql= f'Update bloques SET {atri} = {value} WHERE id_bloques = {id}'
        db=DataBase
        db.modificar(sql)