from getpass import getpass
from mysql.connector import connect, Error

class DataBase:

    def __init__(self):
        self.username = "root"
        self.password = "Nokia2022"

    def conectar(self):
        try:
            with connect(
                host="localhost",
                user=self.username,
                password=self.password,
                database="mydb"
            ) as connection:
                print(connection)
                with connection.cursor() as cursor:
                    cursor.execute("SELECT * FROM usuario")
                    for row in cursor.fetchall():
                        print(row)
        except Error as e:
            print(f'ha ocurrido un error ...{e}...')

db = DataBase()
db.conectar()