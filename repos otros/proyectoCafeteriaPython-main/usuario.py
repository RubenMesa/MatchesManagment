from conector import DataBase
class Usuario:

    def __init__(self, nombre ,password, cli_cod):
        self.nombre = nombre
        self.password = password
        self.cli_cod = cli_cod
        



    def insertar_usu_cli(self):
        sql = f"INSERT INTO usuarios (usu_nom,usu_pass,cli_cod) VALUE ('{self.nombre}','{self.password}', {self.cli_cod});"
        db = DataBase()
        db.insert(sql)

    def insertar_usu_tra(self):
        sql = f"INSERT INTO usuarios (usu_nom,usu_pass,tra_cod) VALUE ('{self.nombre}','{self.password}', {self.tra_cod});"
        db = DataBase()
        db.insert(sql)

    def mostrar_usu():
        tabla = 'usuarios' 
        col1 = "id"
        col2 = "Nombre"
        col3 = "Password"
        col4 = "Tra_Cod"
        col5 = "Cli_Cod"
        col6 = " "
        col7 = " "
        db = DataBase()
        db.select(tabla,col1,col2,col3,col4,col5,col6,col7)

    def mostrar_usu_uq(id):
        tabla = 'usuarios'
        columna = 'usu_cod' 
        col1 = "id"
        col2 = "Nombre"
        col3 = "Password"
        col4 = "Tra_Cod"
        col5 = "Cli_Cod"
        col6 = " "
        col7 = " "
        db = DataBase()
        db.select_one(tabla,columna, id,col1,col2,col3,col4,col5,col6,col7)

    def actualizar_usu(id, nombre, password):
        sql = f"UPDATE usuarios SET usu_nom = '{nombre}', usu_pass = '{password}' WHERE usu_cod = {id};"
        db = DataBase()
        db.update(sql)

    def eliminar_usu(id):
        sql = f'DELETE FROM usuarios WHERE usu_cod = {id};'
        db = DataBase()
        db.delete(sql)

    def comprar_usu():
        pass