from getpass import getpass
from mysql.connector import connect, Error


class DataBase:

    def __init__(self, user, password):
        self.user = user
        self.password = password

    def conectar(self):
        try:
            with connect(
                host="localhost",
                user="root",
                password="asdf",
                database="mydb"
            ) as connection:
                print(connection)
                select = "SELECT * FROM personas"
                with connection.cursor() as cursor:
                    cursor.execute(select)
                    for row in cursor.fetchall():
                        print(row)
        except Error as e:
            print(e)

#db = DataBase(input("Ingrese nombre "),getpass("Ingrese Password "))
#db.conectar()