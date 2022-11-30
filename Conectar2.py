import mysql.connector
class Conectar:
    def __init__(self):
        self.__bd = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Nokia2022',
            database='mydb'
        )

        self.__cursor = self.__bd.cursor()

    def ejecutar(self, sql):
        try:
            self.__cursor.execute(sql)
            self.__bd.commit()

            return self.__cursor.rowcount

        except mysql.connector.Error as e:
            return 'Error: '+str(e)
