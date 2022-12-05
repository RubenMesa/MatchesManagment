from getpass import getpass
from mysql.connector import connect, Error

class DataBase:

    def __init__(self):
        try:
            aux= connect(
                host='localhost',
                user='root',
                password="Nokia2022",
                database="mydb1"
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
            self.close()
        except Error as e:
            print(e)
    
    def list(self,tabla):
        cursor =self.connection.cursor()
        cursor.execute(f"SELECT * FROM {tabla};")
        resultado=cursor.fetchall()
        for registro in resultado:
            print(registro)
        self.connection.close()
    
    def modific(self,sql):
        try:
            cursor = self.connection.cursor()
            cursor.execute(sql)
            self.connection.commit()
            self.close()
        except Error as e:
            print(e)

    def Eliminar(self,sql):
        try:
            cursor = self.connection.cursor()
            cursor.execute(sql)
            self.connection.commit()
            self.close()
        except Error as e:
            print(e)
    
    def modificarCLI(self):
        try:
            id1=int(input("Ingrese el id..."))
            cursor =self.connection.cursor()
            cursor.execute(f"SELECT idcliente FROM cliente WHERE idcliente={id1};")
            resultado=cursor.fetchone()
            print(resultado)
            if resultado:
                
                print("-----------MENÚ---------")
                print("1.- cambiar rut...")
                print("2.- cambiar nombre...")
                print("3.- cambiar apellido...")
                print("0.- cambiar edad...")
                print("5.- cambiar direccion...")
                print("6.- cambiar correo...")
                op=int(input("Ingrese la opcion deseada"))
                if op==1:
                        rut=int(input("Ingrese el nuevo rut..."))
                        cursor.execute(f"UPDATE cliente SET rut={rut};")
                        self.connection.commit()
                        self.close()
                elif op ==2:
                        nombre=input("Ingrese el nuevo nombre...")
                        cursor.execute(f"UPDATE cliente SET nombre='{nombre}';")
                        self.connection.commit()
                        self.close()
                elif op ==3:
                        apellido=input("Ingrese el nuevo apellido...")
                        cursor.execute(f"UPDATE cliente SET apellido='{apellido}';")
                        self.connection.commit()
                        self.close()
                elif op ==4:
                        edad=int(input("Ingrese la nueva edad..."))
                        cursor.execute(f"UPDATE cliente SET edad={edad};")
                        self.connection.commit()
                        self.close()
                elif op ==5:
                        direccion=input("Ingrese la nueva direccion...")
                        cursor.execute(f"UPDATE cliente SET direccion= '{direccion}';")
                        self.connection.commit()
                        self.close()
                elif op ==6:
                        correo=input("Ingrese el nuevo correo...")
                        cursor.execute(f"UPDATE cliente SET correo='{correo}';")
                        self.connection.commit()
                        self.close()
                else:
                        print("Error.....................")
        except Error as e:
                print(e)
    def modificarTRA(self):
        try:
            id1=int(input("Ingrese el id......:)"))
            cursor =self.connection.cursor()
            cursor.execute(f"SELECT idtrabajador FROM trabajador WHERE idproducto={id1};")
            resultado=cursor.fetchone()
            print(resultado)
            if resultado:
                print("-----------MENÚ---------")
                print("1.- cambiar rut...")
                print("2.- cambiar nombre...")
                print("3.- cambiar apellido...")
                print("0.- cambiar edad...")                
                print("5.- cambiar direccion...")
                print("6.- cambiar correo...")
                print("7.- cambiar especialidad")
                op=int(input("Ingrese la opcion deseada"))
                if op==1:
                        rut=int(input("Ingrese el nuevo rut..."))
                        cursor.execute(f"UPDATE cliente SET rut={rut};")
                        self.connection.commit()
                        self.close()
                elif op ==2:
                        nombre=input("Ingrese el nuevo nombre...")
                        cursor.execute(f"UPDATE cliente SET nombre='{nombre}';")
                        self.connection.commit()
                        self.close()
                elif op ==3:
                        apellido=input("Ingrese el nuevo apellido...")
                        cursor.execute(f"UPDATE cliente SET apellido='{apellido}';")
                        self.connection.commit()
                        self.close()
                elif op ==4:
                        edad=int(input("Ingrese la nueva edad..."))
                        cursor.execute(f"UPDATE cliente SET edad={edad};")
                        self.connection.commit()
                        self.close()
                elif op ==5:
                        direccion=input("Ingrese la nueva direccion...")
                        cursor.execute(f"UPDATE cliente SET direccion= '{direccion}';")
                        self.connection.commit()
                        self.close()
                elif op ==6:
                        correo=input("Ingrese el nuevo correo...")
                        cursor.execute(f"UPDATE cliente SET correo='{correo}';")
                        self.connection.commit()
                        self.close()
                elif op ==7:
                        especialidad=input("Ingrese el nuevo correo...")
                        cursor.execute(f"UPDATE cliente SET correo='{especialidad}';")
                        self.connection.commit()
                        self.close()
                else:
                        print("Error.....................")
        except Error as e:
            print(e)  
    def modificarPRO(self):
            try:
                id1=int(input("Ingrese el id......:)"))
                cursor =self.connection.cursor()
                cursor.execute(f"SELECT idproducto FROM producto WHERE idproducto={id1};")
                resultado=cursor.fetchone()
                print(resultado)
                if resultado:
                    print("-----------MENÚ---------")
                    print("1.- cambiar nombre...")
                    print("2.- cambiar marca...")
                    print("3.- cambiar precio...")
                    op=int(input("Ingrese la opcion deseada"))
                    if op==1:
                            nombre=int(input("Ingrese el nuevo nombre..."))
                            cursor.execute(f"UPDATE producto SET nombre={nombre};")
                            self.connection.commit()
                            self.close()
                    elif op ==2:
                            marca=input("Ingrese el nuevo marca...")
                            cursor.execute(f"UPDATE producto SET marca='{marca}';")
                            self.connection.commit()
                            self.close()
                    elif op ==3:
                            precio=input("Ingrese el nuevo precio...")
                            cursor.execute(f"UPDATE producto SET precio={precio};")
                            self.connection.commit()
                            self.close()
                    
                    else:
                            print("Error.....................")
            except Error as e:
                print(e)    
    def close(self):
        self.connection.close()
        print("la conexion fue cerrada...")
