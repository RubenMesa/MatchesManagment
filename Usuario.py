from conector import DataBase

class usuario:
    pieder = False 
    pieizq = False

    def __init__(self, nombre, user, password, pieder, pieizq ):
        self.nombre = nombre
        self.user = user
        self.password =  password
        self.pieder = pieder
        self.pieizq = pieizq
    
    def registrarjugador(self):
        sql=f'INSERT INTO usuario (us_nombrereal,us_nombreuser,us_pass,us_pieder,us_pieizq) VALUES ("{self.nombre}","{self.user}","{self.password}",{self.pieder},"{self.pieizq}")'
        db=DataBase()
        db.insert(sql)

    def listar_jugador(self,id):
        sql=f'Select * FROM usuario WHERE id_usuario = "{id}"'
        db=DataBase()
        return db.list_dato_uq(sql)
         
    def listartodo_user(self):
        tabla = ('usuario')
        db = DataBase()
        db.list(tabla)

    def modificar_user(id,atri,value):
        sql= f'Update usuario SET {atri} = "{value}" WHERE id_usuario = {id}'
        db=DataBase()
        db.modificar(sql)
        
    def eliminar_user(id):
        sql= f'DELETE FROM usuario WHERE id_usuario = {id}'
        db=DataBase()
        db.eliminar(sql)

    

        
    

            