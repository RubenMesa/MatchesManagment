from personas import Personas
from conector import DataBase

class Trabajador:

    def __init__(self,  inicio_turno, termino_turno, fcontr, run,perf_cod):

        self.inicio_turno = inicio_turno
        self.termino_turno = termino_turno
        self.fcontr = fcontr
        self.perf_cod = perf_cod
        self.run = run 

    def insertar_tra(self):
        sql = f"INSERT INTO trabajadores (tra_inicio_turno, tra_termino_turno, tra_fcontr, per_run, perf_cod) VALUE ('{self.inicio_turno}', '{self.termino_turno}', '{self.fcontr}', {self.run}, {self.perf_cod});"
        db = DataBase()
        db.insert(sql)
    
    def mostrar_tra():
        tabla = 'trabajadores' 
        col1 = "id"
        col2 = "Inicio Turno"
        col3 = "Termino Turno"
        col4 = "Fecha de Contratación"
        col5 = "Contrato"
        col6 = "Perfil"
        col7 = "Run"
        db = DataBase()
        db.select(tabla,col1,col2,col3,col4,col5,col6,col7)

    def mostrar_tra_uq(id):
        tabla = 'trabajadores'
        columna = 'tra_cod' 
        col1 = "id"
        col2 = "Inicio Turno"
        col3 = "Termino Turno"
        col4 = "Fecha de Contratación"
        col5 = "Contrato"
        col6 = "Perfil"
        col7 = "Run"
        db = DataBase()
        db.select_one(tabla,columna, id,col1,col2,col3,col4,col5,col6,col7)
    
    def actualizar_tra(id,inicio_turno,termino_turno,perf_cod):
        sql = f"UPDATE trabajadores SET tra_inicio_turno = '{inicio_turno}', tra_termino_turno = '{termino_turno}', perf_cod = {perf_cod} WHERE tra_cod = {id};"
        db = DataBase()
        db.update(sql)

    def eliminar_tra(id):
        sql = f'DELETE FROM trabajadores WHERE tra_cod = {id};'
        db = DataBase()
        db.delete(sql)