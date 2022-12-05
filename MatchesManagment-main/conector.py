from getpass import getpass
from mysql.connector import connect, Error

class DataBase:

    def __init__(self):
        try:
            aux= connect(
                host='localhost',
                user='root',
                password="Nokia2022",
                database="mydb"
                )               
            print("Ingreso a BD..")
            self.connection=aux
        except Error as e:
            print( 'error'+ str(e))
 
    def insert(self,sql):
        try:
            cursor = self.connection.cursor()
            cursor.execute(sql)
            self.connection.commit()
            self.connection.close()
        except Error as e:
            print(e)
    
    def list(self,tabla):
        cursor =self.connection.cursor()
        cursor.execute(f"SELECT * FROM {tabla};")
        resultado=cursor.fetchall()
        for registro in resultado:
            print(registro)
        self.connection.close()

    def list_dato_uq(self,sql):
        cursor = self.connection.cursor()
        cursor.execute(sql)
        resultado=cursor.fetchone()
        print(resultado)
        self.connection.close()
        return resultado

    def modificar(sql,self):
        try:
            cursor = self.connection.cursor()
            cursor.execute(sql)
            self.connection.commit()
            self.connection.close()
        except Error as e:
            print(e)
    
 

    



    


