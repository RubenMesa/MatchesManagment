from conector import DataBase
class Boletas:

    def __init__(self, iva, total,ven_cod):
        self.iva = iva
        self.total = total
        self.ven_cod = ven_cod

    def insert_bol(self):
        sql = f"INSERT INTO boletas (bol_iva, bol_total, ven_cod) VALUE ({self.iva}, {self.total}, {self.ven_cod});"
        db = DataBase()
        db.insert(sql)

    def mostrar_bol():
        tabla = 'boletas' 
        col1 = "ID"
        col2 = "IVA"
        col3 = "TOTAL"
        col4 = "Código Venta"
        col5 = " "
        col6 = " "
        col7 = " "
        db = DataBase()
        db.select(tabla,col1,col2,col3,col4,col5,col6,col7)

    def mostrar_bol_uq(id):
        tabla = 'boletas'
        columna = 'bol_cod' 
        col1 = "ID"
        col2 = "IVA"
        col3 = "TOTAL"
        col4 = "Código Venta"
        col5 = " "
        col6 = " "
        col7 = " "
        db = DataBase()
        db.select_one(tabla,columna, id,col1,col2,col3,col4,col5,col6,col7)

    def mostrar_bol_usu(id):
        sql = f"SELECT * FROM boletas b JOIN ventas v ON (b.ven_cod = v.ven_cod) JOIN usuarios u ON (v.usu_cod = u.usu_cod) WHERE u.usu_cod = {id};"
         
        col1 = "ID"
        col2 = "IVA"
        col3 = "TOTAL"
        col4 = "Código Venta"
        col5 = " "
        col6 = " "
        col7 = " "
        db = DataBase()
        db.select_bol_usu(sql, col1,col2,col3,col4,col5,col6,col7)

    def mostrar_bol_cli(id):
        tabla = 'boletas'
        columna = 'cli_cod' 
        col1 = "ID"
        col2 = "IVA"
        col3 = "TOTAL"
        col4 = "Código Venta"
        col5 = " "
        col6 = " "
        col7 = " "
        db = DataBase()
        db.select_one(tabla,columna, id,col1,col2,col3,col4,col5,col6,col7)