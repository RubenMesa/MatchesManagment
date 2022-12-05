from mysql.connector import connect,Error
from getpass import getpass
from conector import DataBase
from Pacientes import Pacientes
from Profesionales import Profesional

#5 Cuentas de perfil paciente
pc1=Pacientes('2paciente1','1paciente123', 1,'Matias Gonzalez Perez', 18778932-6)
pc2=Pacientes('2paciente2','2paciente123', 2,'Carlos Jarpa Lopez', 15774232-1)
pc3=Pacientes('2paciente3','3paciente123', 3,'Fernando Marquez Letelier', 14776972-7)
pc4=Pacientes('2paciente4','4paciente123', 4,'Nicolas Ferrada Zabaleta', 16443567-8)
pc5=Pacientes('2paciente5','5paciente123', 5,'Tomas Ovalle Elgueta', 14112345-8)

#5 Cuentas de perfil Profesional
pr1=Profesional('1doctor1','1doctor123', 6,'Andrea Pizarro Galvez', 19887654-6)
pr2=Profesional('1doctor2','2doctor123', 7,'Carla Aedo Vielma', 15332882-5)
pr3=Profesional('1doctor3','3doctor123', 8,'Mateo Lara Villa', 16112325-5)
pr4=Profesional('1doctor4','4doctor123', 9,'Camilo Zambrano Lara', 18332946-2)
pr5=Profesional('1doctor5','5doctor123', 10,'Patricio Galaz Andrade', 18332946-3)

Inicio=getpass("Bienvenido a Clinica Inacap... Presiona una tecla para continuar")
log = input("Ingrese usuario: ")
pwd = getpass("Ingrese su contraseña: ")

if log.startswith("1"):
        while True:
            print('''
            ===== Menu de opciones (Medico)=====
            1. Listar Pacientes
            2. Listar Agendas
            3. Añadir Usuario/Profesional
            4. Agendar Paciente
            0. Salir    
                ''')
            op = input('Ingrese seleccion:\n')

            if op == '1':
                print("========Listar Pacientes========")
                input('Presione enter para continuar...')
                try:
                    with connect(
                        host="localhost",
                        user="root",
                        password="asdf",
                        database="mydb"
                    ) as connection:
                        print(connection)
                        select = ('SELECT a.Per_id, a.Per_nombrecompleto, a.Per_rut, p.Pac_usuario, p.Pac_clave FROM personas a JOIN pacientes p ON (a.Per_id = p.Pac_id)')
                        with connection.cursor() as cursor:
                            cursor.execute(select)
                            print("//ID//Nombres//////////////RUT//////Usuario//////Clave")
                            for row in cursor.fetchall():
                                print(row)
                except Error as e:
                                print(e)
                                break       
            elif op == '2':
                print("========Listar Agendas========")
                input('Presione enter para continuar...')
                try:
                    with connect(
                        host="localhost",
                        user="root",
                        password="asdf",
                        database="mydb"
                    ) as connection:
                        print(connection)
                        select = ('SELECT * from agendas')
                        with connection.cursor() as cursor:
                            cursor.execute(select)
                            print("//ID///Especialista////Paciente/////////Fecha//////Hora")
                            for row in cursor.fetchall():
                                print(row)
                except Error as e:
                                print(e)
                                break 
            elif op == '3':
                print("========Añadir Pacientes========")
                input('Presione enter para continuar...')
                newname=input("ingrese Nombre Completo de Paciente: ")
                idp= 100
                idpc= 100
                rut=(input("Ingrese Rut (sin puntos): "))
                user2=input("Ingrese nuevo usuario: ")
                psw=input("Ingrese nueva contraseña: ")
                try:
                    with connect(
                        host="localhost",
                        user="root",
                        password="asdf",
                        database="mydb"
                    ) as connection:
                        print(connection)
                        persona = (f"INSERT into personas(Per_id, Per_nombrecompleto, Per_rut) VALUES ({idp},'{newname}','{rut}');")
                        select = (f"INSERT into pacientes(Pac_id, Pac_usuario, Pac_clave) VALUES ({idpc},'{user2}','{psw}');")
                        with connection.cursor() as cursor:
                            cursor.execute(select)
                            connection.commit()
                            cursor.execute(persona)
                            connection.commit()
                            cursor.close()
                            connection.close()
                            input("Paciente creado correctamente.. pulse Enter para continuar...")                         
                            idp= idp+1
                            idpc= idpc+1
                except Error as e:
                        print(e) 
            elif op == '4':
                print("=======Agendar Paciente========")
                input('Presione enter para continuar...'),
                id = 20
                prof=input("ingrese Nombre de Especialista: ")
                npac=(input("Ingrese Nombre de Paciente: "))
                date=input("Ingrese la fecha: ")
                hora=input("Ingrese la hora: ")
                try:
                    with connect(
                        host="localhost",
                        user="root",
                        password="asdf",
                        database="mydb"
                    ) as connection:
                        print(connection)
                        agenda = (f"INSERT into agendas (Agend_id, Agend_especialista, Agend_paciente, Agend_fecha, Agend_hora) VALUES ({id},'{prof}','{npac}','{date}','{hora}');")
                        with connection.cursor() as cursor:
                            cursor.execute(agenda)
                            connection.commit()
                            cursor.close()
                            connection.close()
                            input("Paciente agendado correctamente.. pulse Enter para continuar...")                         
                            id= id+1
                except Error as e:
                        print(e) 
                
            elif op == '0':
                print("Usuario deslogeado... Correctamente...")
                break
            
elif log.startswith("2"):
        while True:
            print('''
            ===== Menu de opciones (Pacientes)=====
            1. Listar Medicos
            2. Listar Agendas
            3. Costos de Atencion
            4. Agendar una cita
            0. Salir    
                ''')
            op = input('Ingrese seleccion:\n')
            
            if op == '1':
                print("======Listar Medicos=======")
                input('Presione enter para continuar...')
                try:
                    with connect(
                        host="localhost",
                        user="root",
                        password="asdf",
                        database="mydb"
                    ) as connection:
                        print(connection)
                        select = ('SELECT a.Per_id, a.Per_nombrecompleto, a.Per_rut, p.Medicos_usuario FROM personas a JOIN medicos p ON (a.Per_id = p.Medicos_id)')
                        with connection.cursor() as cursor:
                            cursor.execute(select)
                            for row in cursor.fetchall():
                                print("ID - Nombres - RUT - Usuario")
                                print(row)
                except Error as e:
                                print(e)
                                break     

            elif op == '2':
                print("========Listar Agendas========")
                input('Presione enter para continuar...')
                try:
                    with connect(
                        host="localhost",
                        user="root",
                        password="asdf",
                        database="mydb"
                    ) as connection:
                        print(connection)
                        select = ('SELECT * from agendas')
                        with connection.cursor() as cursor:
                            cursor.execute(select)
                            print("//ID///Especialista////Paciente/////////Fecha//////Hora")
                            for row in cursor.fetchall():
                                print(row)
                except Error as e:
                                print(e)
                                break
            elif op == '3':
                print("======Costos de atencion=======")
                input('Presione enter para continuar...')
                try:
                    with connect(
                        host="localhost",
                        user="root",
                        password="asdf",
                        database="mydb"
                    ) as connection:
                        print(connection)
                        select = ('SELECT valor_especialista, valor_precio FROM valores')
                        with connection.cursor() as cursor:
                            cursor.execute(select)
                            for row in cursor.fetchall():
                                print("Especialista ---- Precio")
                                print(row)
                except Error as e:
                                print(e)
                                break    
                            
            elif op == '4':
                print("=======Agendar una cita========")
                input('Presione enter para continuar...'),
                id = 20
                prof=input("ingrese Nombre de Especialista: ")
                npac=(input("Ingrese su Nombre: "))
                date=input("Ingrese la fecha: ")
                hora=input("Ingrese la hora: ")
                try:
                    with connect(
                        host="localhost",
                        user="root",
                        password="asdf",
                        database="mydb"
                    ) as connection:
                        print(connection)
                        agenda = (f"INSERT into agendas (Agend_id, Agend_especialista, Agend_paciente, Agend_fecha, Agend_hora) VALUES ({id},'{prof}','{npac}','{date}','{hora}');")
                        with connection.cursor() as cursor:
                            cursor.execute(agenda)
                            connection.commit()
                            cursor.close()
                            connection.close()
                            input("Paciente agendado correctamente.. pulse Enter para continuar...")                         
                            id= id+1
                except Error as e:
                        print(e) 
                        
            elif op == '0':
                print("Usuario deslogeado... Correctamente...")
                break
else:
    print ("Usuario no registrado...")
        
#db = DataBase(input("Ingrese nombre "),getpass("Ingrese Password "))
#db.conectar()