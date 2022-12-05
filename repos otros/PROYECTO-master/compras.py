from Productos import *

class compra:
    def __init__(self,cliente_idcliente,producto_idproducto,boleta_idboleta):
        self.idCliente=cliente_idcliente
        self.idProducto=producto_idproducto
        self.idBoleta=boleta_idboleta
    

    def ingresarCompra(self):
        
        sql=f'INSERT INTO compra (cliente_idcliente, producto_idproducto,boleta_idboleta,fecha) VALUES({self.idCliente},{self.idProducto},1,sysdate());'
        db=DataBase()
        db.insert(sql)