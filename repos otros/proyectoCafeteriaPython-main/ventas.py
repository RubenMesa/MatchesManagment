from conector import DataBase

class Ventas:
    def __init__(self, descripcion, fecha,  subtotal,usu_cod):
        self.fecha = fecha
        self.descripcion = descripcion
        self.subtotal = subtotal
        self.usu_cod = usu_cod

    def insert_ven_usu(self):
        sql = f"INSERT INTO ventas (ven_descrip, ven_fecha, ven_subtotal,usu_cod) VALUE ('{self.descripcion}', '{self.fecha}', {self.subtotal}, {self.usu_cod});"
        db = DataBase()
        db.insert(sql)

    def insert_ven_cli(self):
        sql = f"INSERT INTO ventas (ven_descrip, ven_fecha, ven_subtotal,cli_cod) VALUE ('{self.descripcion}', '{self.fecha}', {self.subtotal}, {self.usu_cod});"
        db = DataBase()
        db.insert(sql)

    def mostrar_ven():
        tabla = 'ventas' 
        col1 = "ID"
        col2 = "Descripcion"
        col3 = "Fecha"
        col4 = "Subtotal"
        col5 = "Codigo Usuario"
        col6 = "Codigo Cliente"
        col7 = " "
        db = DataBase()
        db.select(tabla,col1,col2,col3,col4,col5,col6,col7)

    def mostrar_ven_uq(id):
        tabla = 'ventas'
        columna = 'ven_cod' 
        col1 = "ID"
        col2 = "Descripcion"
        col3 = "Fecha"
        col4 = "Subtotal"
        col5 = "Codigo Usuario"
        col6 = "Codigo Cliente"
        col7 = " "
        db = DataBase()
        db.select_one(tabla,columna, id,col1,col2,col3,col4,col5,col6,col7)