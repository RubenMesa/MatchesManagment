from conector import DataBase

class Usuario:
    pieder = False 
    pieizq = False

    def __init__(self, nombre, user, password, poscision, pieder, pieizq ):
        self.nombre = nombre
        self.user = user
        self.password =  password
        self.poscision = poscision
        self.pieder = pieder
        self.pieizq = pieizq
    def save(self):
        sql = f'INSERT INTO Usuario (nombre) VALUES ("{self.nombre}")'
        db = DataBase()
        db.insert(sql)

    def list_all():
        db = DataBase()
        db.list()       