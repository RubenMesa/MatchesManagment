from Usuario import *
from Boleta import *
from Venta import *
from trabajador import *
from cliente import *
from Conectar import *
from compras import *
import os
    
class menu:

    def __init__():
        
        print("----------- Trabajar con Clientes---------")
        print("1.- Agregar cliente.")
        print("2.- Mostrar clientes.")
        print("3.- Modificar datos de cliente.")
        print("4.- Eliminar cliente.")
        print("5.- Regresar al MENÚ principal.")
        op=int(input("Eliga una opcion..."))
        if op ==1:
            #Agregar clientes
            os.system('cls')
            print("Solicitando datos ...\n")
            rut = int(input("Ingrese rut ..."))
            nombre= input("Ingrese el nombre...")
            apellido = input("Ingrese el apellido...")
            edad= int(input("Ingrese la edad..."))
            direccion = input("Ingrese la direccion...")
            correo = input("Ingrese el correo...")
            nuevoU =cliente(rut,nombre,apellido,edad,direccion,correo)
            nuevoU.create1()
            print("Cliente guardado exitosamente!...")
            
        elif op==2:
            #Mostrar clientes
            os.system('cls')
            cliente.mostrar()
            
        elif op==3:
            #Actualizar un cliente
            os.system('cls')
            cliente.mostrar()
            
            u=DataBase()
            u.modificarCLI()
            
        elif op==4:
            #Eliminar un cliente
            os.system('cls')
            cliente.mostrar()
            id =int(input("Ingrese id... "))
            cliente.eliminar(id)
            
        elif op==5:
            os.system('cls')
            print("Regresaste al MENÚ principal...")
            menu.menuPrincipal()
        else:
            print("error...")
            
            
    def menuProductos():
        print("-----------Productos---------")
        print("1.- Agregar producto.")
        print("2.- Mostrar producto.")
        print("3.- Modificar producto.")
        print("4.- Eliminar producto.")
        print("5.- Regresar al MENÚ principal.")
        op=int(input("Eliga una opcion..."))
        if op ==1:
            os.system('cls')
            print("Solicitando datos ...\n")
            nombre= input("Ingrese el nombre... ")
            marca=input("Ingrese la marca...")
            precio=int(input("Ingrese el precio..."))
            nuevoP = productos(nombre,marca,precio)
            nuevoP.creaP()
            print("Producto guardado exitosamente! \n")
            input('Presione enter para continuar...')
        elif op==2:
            os.system('cls')
            productos.mostrarP()
            input('Presione enter para continuar...')
        elif op==3:
            os.system('cls')
            productos.mostrarP()
            u=DataBase()
            u.modificarPRO()
            input('Presione enter para continuar...')

        if op==4:
            os.system('cls')
            id =int(input("Ingrese id..."))
            productos.eliminarP(id)
            input('Presione enter para continuar...')
    def menuEmpleado():
        print("-----------Trabajadores---------")
        print("1.- Agregar trabajadores.")
        print("2.- Mostrar trabajadores.")
        print("3.- Modificar datos de trabajadores.")
        print("4.- Eliminar trabajadores.")
        try:
            op=int(input("Eliga una opcion..."))
            if op ==1:
                os.system('cls')
                print("Solicitando datos ...\n")
                rut = int(input("Ingrese rut ..."))
                nombre= input("Ingrese el nombre...")
                apellido = input("Ingrese el apellido...")
                edad= int(input("Ingrese la edad... "))
                direccion = input("Ingrese la direccion...")
                correo = input("Ingrese el correo...")
                especialidad =input("Ingrese el cargo...")
                nuevoU = trabajador(rut,nombre,apellido,edad,direccion,correo,especialidad)
                nuevoU.creaT()
                print("Usuario guardado exitosamente! \n")
                input('Presione enter para continuar...')
            elif op==2:
                os.system('cls')
                trabajador.mostrarT()
                input('Presione enter para continuar...')
            elif op==3:
                os.system('cls')
                trabajador.mostrarT()
                id=int(input("Ingrese el id del usuario..."))
                print("Solicitando datos de usuario ...\n")
                rut = int(input("Ingrese rut ..."))
                nombre= input("Ingrese el nombre...")
                apellido = input("Ingrese el apellido...")
                edad= int(input("Ingrese la edad..."))
                direccion = input("Ingrese la direccion...")
                correo = input("Ingrese el correo...")
                
                trabajador.modificarT(id,rut,nombre,apellido,edad,direccion,correo)
                input('Presione enter para continuar...')
            if op==4:
                os.system('cls')
                id =int(input("Ingrese id..."))
                
                trabajador.eliminarT(id)
                input('Presione enter para continuar...')
        except Error as e:
            print(e)
    def menuCompras():
            os.system('cls')
            cliente.mostrar()
            idcli=int(input("Ingrese el id del cliente..."))
            print("-----------Productos---------")
            print("1.- Honda dio 125.")
            print("2.- Honda CB 300 R.")
            print("3.- Susuki Address 125.")
            print("4.- Susuki GSX-S125.")
            print("0.- Cerrar sesion...")
            idPro=int(input("Eliga un producto..."))
            c=compra(idcli,idPro,1)
            c.ingresarCompra()
            input('Presione enter para continuar...')


    def menuPrincipal():
        while True:
            os.system('cls')
            print("-----------MENÚ---------")
            print("1.- Trabajar con clientes.")
            print("2.- Trabajar con trabajadores.")
            print("3.- Trabajar con productos.")
            print("4.- Comprar productos.")
            print("0.- Cerrar sesion...")
            try:
                op=int(input("Ingrese la opcion deseada:  "))
                if op == 1:
                    os.system('cls')
                    menu.__init__()
                    input('Presione enter para continuar...')
                elif op == 2:
                    os.system('cls')
                    menu.menuEmpleado()
                    input('Presione enter para continuar...')
                elif op == 3:
                    os.system('cls')
                    menu.menuProductos()
                    input('Presione enter para continuar...')
                elif op == 4:
                    os.system('cls')
                    menu.menuCompras()
                    input('Presione enter para continuar...')
                elif op ==0:
                    os.system('cls')
                    print("Sesion cerrada....")
                    break
                else:
                    os.system('cls')
                    print("Ingrese a una de las opciones del MENÚ...")
                    input('Presione enter para continuar...')  
            except  :
                input("Eliga una de las opciones del MENÚ...")  
                continue
u=menu.menuPrincipal()