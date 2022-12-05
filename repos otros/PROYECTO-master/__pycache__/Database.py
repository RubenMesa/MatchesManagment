from getpass import getpass
from mysql.connector import connect, Error

class Database:

    def __init__(self):
        try:
            aux = connect(
                host='localhost',
                user='test',
                password=getpass("Ingrese pass"),
                database='new_schema'
            )
            self.connection = aux 
        except Error as e:
            print("Eror "+ e)

    def insert(self, sql):
        try:
            cursor = self.connection.cursor()
            cursor.execute(sql)
            self.connection.commit()
            self.close()
        except Error as e:
            print(e)

    def list(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM movies;")
        resultado = cursor.fetchall()
        for registro in resultado:
            print(registro)
        self.close()

    
    def close(self):
        self.connection.close()
        print("La conexion fue cerrada")
