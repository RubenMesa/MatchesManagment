from conector import DataBase

class Comandas:

    def __init__(self, cantidad, hora, pro_cod, ven_cod):
        self.cantidad = cantidad
        self.hora = hora
        self.pro_cod = pro_cod
        self.ven_cod = ven_cod

    def insert_com(self):
        sql = f"INSERT INTO comandas (com_cant, com_hora, pro_cod, ven_cod) VALUE ('{self.cantidad}', '{self.hora}', {self.pro_cod}, {self.ven_cod});"
        db = DataBase()
        db.insert(sql)

    def mostrar_com():
        tabla = 'comandas' 
        col1 = "ID"
        col2 = "Cantidad"
        col3 = "Hora"
        col4 = "Código Producto"
        col5 = "Código Venta"
        col6 = " "
        col7 = " "
        db = DataBase()
        db.select(tabla,col1,col2,col3,col4,col5,col6,col7)

    def mostrar_com_uq(id):
        tabla = 'comandas'
        columna = 'com_cod' 
        col1 = "ID"
        col2 = "Cantidad"
        col3 = "Hora"
        col4 = "Código Producto"
        col5 = "Código Venta"
        col6 = " "
        col7 = " "
        db = DataBase()
        db.select_one(tabla,columna, id,col1,col2,col3,col4,col5,col6,col7)