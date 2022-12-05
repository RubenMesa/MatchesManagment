# decidimos separar las clases por archivo
# por eso usamos este metodo para importar lo que esta en personas.py
# from personas import Personas
from conector import DataBase
# nuestra clase Clientes heredando () lo que venga de Personas
class Clientes:
    # esta funcion agrega o redefine el constructor agregando
    # "puntos" como nuevo parametro    
    def __init__(self, puntos, descto, cli_frecuente, run):
    #def __init__(self, run, nombre, app, apm, tel, email, fnac, cod, puntos, descto, cli_frecuente):
        # super().__init__(toma en consideracion estos parametros originales)
        # del constructor en personas
        # super().__init__(self, run, nombre, app, apm, tel, email, fnac)
        # define el self para puntos en este caso quedo igual
       
        self.puntos = puntos
        self.descto = descto
        self.cli_frecuente = cli_frecuente
        self.run = run
        

    def insert_cli(self):
        sql = f"INSERT INTO clientes (cli_puntos, cli_descto, cli_frecuente, per_run) VALUE ({self.puntos}, {self.descto}, {self.cli_frecuente}, {self.run});"
        db = DataBase()
        db.insert(sql)

    def mostrar_cli():
        tabla = 'clientes' 
        col1 = "id"
        col2 = "Puntos"
        col3 = "Descuento"
        col4 = "Cli_Frecuente"
        col5 = "Run"
        col6 = " "
        col7 = " "
        db = DataBase()
        db.select(tabla,col1,col2,col3,col4,col5,col6,col7)

    def mostrar_cli_uq(id):
        tabla = 'clientes'
        columna = 'cli_cod' 
        col1 = "id"
        col2 = "Puntos"
        col3 = "Descuento"
        col4 = "Cli_Frecuente"
        col5 = "Run"
        col6 = " "
        col7 = " "
        db = DataBase()
        db.select_one(tabla,columna, id,col1,col2,col3,col4,col5,col6,col7)

    def actualizar_cli(id,puntos,descto):
        sql = f"UPDATE clientes SET cli_puntos = {puntos}, cli_descto = {descto} WHERE cli_cod = {id};"
        db = DataBase()
        db.update(sql)

    def eliminar_cli(id):
        sql = f'DELETE FROM clientes WHERE cli_cod = {id};'
        db = DataBase()
        db.delete(sql)
    
