from conector import DataBase
from pythonrequest import PythonRequest

class posicion:
    def __init__(self, id, nombre, desc):
        self.id = id
        self.nombre = nombre
        self.desc = desc
    
    def registrarposicion(self):
        sql=f'INSERT INTO posicion (id_posicion,pos_nombre,pos_desc) VALUES ("{self.id}","{self.nombre}","{self.desc}")'
        db=DataBase()
        db.insert(sql)

    def listar_posicion(self,id):
        sql=f'Select * FROM posicion WHERE id_posicion = "{id}"'
        db=DataBase()
        return db.list_dato_uq(sql)
        
    def listartodo_posicion(self):
        tabla = ('posicion')
        db = DataBase()
        db.list(tabla)

    def modificar_posicion(self,id,atri,value):
        sql= f'Update posicion SET {atri} = {value} WHERE id_posicion = {id}'
        db=DataBase
        db.modificar(sql)
    
    def eliminar_user(id):
        sql= f'DELETE FROM posicion WHERE id_posicion = {id}'
        db=DataBase()
        db.eliminar(sql)
    
    def ver_posicion_api():
        api=PythonRequest
        api.get_posiciones()

    def ver_posiciones_api():
        pass    

    def agregar_posicion_api(nom, desc):
        data = '{"nombre": '+'"'+nom+'"'', "descripcion": '+'"'+desc+'"'+' }'
        api= PythonRequest
        api.post_posiciones(data)

    def modificar_posicion_api(id, nom, desc):
        data = '{"nombre": '+'"'+nom+'"'', "descripcion": '+'"'+desc+'"'+' }'
        api= PythonRequest
        api.put_posiciones(id,data)

    def eliminar_posicion_api(id):
        api= PythonRequest
        api.delete_posiciones(id)