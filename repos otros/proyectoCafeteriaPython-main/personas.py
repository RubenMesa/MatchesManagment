from conector import DataBase

#La class Personas contiene los elementos run, nombre, etc
class Personas:
    # constructor 
    def __init__(self, run, nombre, app, apm, tel, email, fnac):

        self.run = run
        self.nombre = nombre
        self.app = app
        self.apm = apm
        self.tel = tel
        self.email = email
        self.fnac = fnac
    
    def insertar_per(self):
        sql = f"INSERT INTO personas (per_run, per_nombre, per_app, per_apm, per_tel, per_email, per_fnac) VALUE ({self.run},'{self.nombre}', '{self.app}','{self.apm}','{self.tel}','{self.email}','{self.fnac}' )"
        db = DataBase()
        db.insert(sql)

    def mostrar_per():
        tabla = 'personas' 
        col1 = "RUN (ID)"
        col2 = "Nombre"
        col3 = "Apellido Paterno"
        col4 = "Apellido Materno"
        col5 = "Teléfono"
        col6 = "Email"
        col7 = "Fecha Nacimiento"
        db = DataBase()
        db.select(tabla,col1,col2,col3,col4,col5,col6,col7)

    def mostrar_per_uq(id):
        tabla = 'personas'
        columna = 'per_run'
        col1 = "RUN (ID)"
        col2 = "Nombre"
        col3 = "Apellido Paterno"
        col4 = "Apellido Materno"
        col5 = "Teléfono"
        col6 = "Email"
        col7 = "Fecha Nacimiento"
        db = DataBase()
        db.select_one(tabla,columna, id,col1,col2,col3,col4,col5,col6,col7)
    
    def actualizar_per(run,nombre,apellido,apellido_materno,telefono,email,fecha_nacimiento):
        sql = f"UPDATE personas SET per_nombre = '{nombre}', per_app = '{apellido}', per_apm = '{apellido_materno}', per_tel = '{telefono}', per_email = '{email}', per_fnac = '{fecha_nacimiento}' WHERE per_run = {run};"
        db = DataBase()
        db.update(sql)

    def eliminar_per(run):
        sql = f'DELETE FROM personas WHERE per_run = {run};'
        db = DataBase()
        db.delete(sql)
        
        

