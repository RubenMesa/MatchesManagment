from conector import DataBase


class Usuario:
    pieder = False 
    pieizq = False

    def __init__(self, nombre, user, password, pieder, pieizq ):
        self.nombre = nombre
        self.user = user
        self.password =  password
        self.pieder = pieder
        self.pieizq = pieizq
    
    def registrarjugador(self):
        sql=f'INSERT INTO usuario (Us_nombre,user,US_pass,Us_pieder,US_pieizq) VALUES ("{self.nombre}","{self.user}","{self.password}",{self.pieder},"{self.pieizq}")'
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

    def modificar_user(self,id,atri,value):
        sql= f'Update usuario SET {atri} = {value} WHERE id_usuario = {id}'
        db=DataBase
        db.modificar(sql)

    

        
    

            