from conector import DataBase
class Productos: 

    def __init__(self,nombre,descripcion, stock, precio):
        self.nombre= nombre
        self.descripcion= descripcion
        self.precio = precio
        self.stock = stock

    def insertar_pro(self):
        sql = f"INSERT INTO productos (pro_nombre,pro_descripcion,pro_stock,pro_precio) VALUE ('{self.nombre}','{self.descripcion}', {self.stock},{self.precio});"
        db = DataBase()
        db.insert(sql)

    def mostrar_pro():
        tabla = 'productos' 
        col1 = "id"
        col2 = "Nombre"
        col3 = "Descipcion"
        col4 = "Stock"
        col5 = "Precio"
        col6 = " "
        col7 = " "
        db = DataBase()
        db.select(tabla,col1,col2,col3,col4,col5,col6,col7)

    def mostrar_pro_uq(id):
        tabla = 'productos'
        columna = 'pro_cod' 
        col1 = "id"
        col2 = "Nombre"
        col3 = "Descipcion"
        col4 = "Stock"
        col5 = "Precio"
        col6 = " "
        col7 = " "
        db = DataBase()
        db.select_one(tabla,columna, id,col1,col2,col3,col4,col5,col6,col7)

    def actualizar_pro(id,nombre,descripcion,stock,precio):
        sql = f"UPDATE productos SET pro_nombre = '{nombre}', pro_descripcion = '{descripcion}', pro_stock = {stock}, pro_precio = {precio} WHERE pro_cod = {id};"
        db = DataBase()
        db.update(sql)
        
    def eliminar_pro(id):
        sql = f'DELETE FROM productos WHERE pro_cod = {id};'
        db = DataBase()
        db.delete(sql)