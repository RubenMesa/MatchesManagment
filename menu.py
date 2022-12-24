from Usuario import usuario
from Cancha import cancha 
from Bloque import bloque 
from TipoCancha import tipocancha 
from Partidos import partido
from Posicion import posicion
from Participacion import participacion
import os
import time

class Menu:
    cl = lambda: os.system("cls")
    cl()
    def __init__():
        opcion = True
        while opcion:
            print(' ')
            print('********************************** ')
            print('*                                * ')
            print('*          ¡BIENVENIDO           * ')
            print('*               A                * ')
            print('*        MATCHESMANAGMENT!       * ')
            print('*                                * ')
            print('********************************** ')
            print(' ')
            print('1.- Jugadores ')
            print('2.- Partidos ')
            print('3.- Posiciones API')
            print('4.- Configuracion ')
            print('5.- Borrar datos ')
            print('6.- Salir ')
            print(' ')
            print('********************************** ')
            print('*                                * ')
            print('* Escribe el numero de la opción * ')
            print('*                                * ')
            print('********************************** ')
            
            valor = int(input("-> : "))
            cl = lambda: os.system("cls")
            cl()

            if valor == 6:
                print("Adios .")
                time.sleep(1)
                cl()
                print("Adios ..")
                time.sleep(1)
                cl()
                print("Adios ...")
                time.sleep(1)
                cl()
                break

            elif valor == 1:
                continuar = True
                while continuar:
                    print(' ')
                    print('********************************** ')
                    print('*                                * ')
                    print('*           JUGADORES            * ')
                    print('*                                * ')
                    print('********************************** ')
                    print(' ')
                    print('1.- Registrar jugador')
                    print('2.- Consultar un jugador')
                    print('3.- Consultar todos los jugadores')
                    print('4.- Modificar jugador')
                    print('5.- Volver')
                    print(' ')
                    valorj = int(input("-> : "))     
                    cl()       
                    if valorj == 1:
                        nom = str(input("ingrese nombre: "))
                        us  = str(input("ingrese nombre de usuario: "))
                        pas =  str(input("ingrese contraseña: "))
                        pd  =(input("utiliza el pie derecho? \nPresione 1 sino presione 0 : "))
                        pi  =(input("utiliza el pie derecho?\nPresione 1 sino presione 0 : "))
                    
                        nuser = usuario(nom, us, pas, pd, pi)
                        nuser.registrarjugador()
                        input("Presione tecla ENTER para volver")
                        cl()   

                    elif valorj == 2:
                        id=int(input('ingrese por su id: '))
                        resultado =  usuario.listar_jugador(id,id)
                        if resultado == None:
                            print ("la id no coincide")
                        else:
                            print(' ')
                            input("Presione tecla ENTER para volver")
                            cl()   

                    elif valorj == 3:
                        usuario.listartodo_user(1)
                        print(" ")
                        print(" ")
                        input("Presione tecla ENTER para volver")
                        cl()

                    elif valorj == 4:
                        id=int(input('ingrese por su id: '))
                        resultado =  usuario.listar_jugador(id,id)
                        if resultado == None:
                            print ("la id no coincide")
                        else:
                            print('1.- Nombre')
                            print('2.- Usuario')
                            print('3.- Contraseña')
                            print('4.- Pie derecho')
                            print('5.- Pie izquierdo')
                            atri=int(input('Que desea modificar: '))
                            nuevovalor=input('cual es el nuevo valor: ')
                            if atri == 1:                                
                                usuario.modificar_user(id,'us_nombrereal',nuevovalor)
                            elif atri ==2:
                                usuario.modificar_user(id,'us_nombreuser',nuevovalor)
                            elif atri ==3:
                                usuario.modificar_user(id,'us_pass',nuevovalor)
                            elif atri ==4:
                                usuario.modificar_user(id,'us_pieder',int(nuevovalor))
                            elif atri ==5:
                                usuario.modificar_user(id,'us_pieizq',int(nuevovalor))
                        input("Presione tecla ENTER para volver")
                        cl()  
                    elif valorj == 5:
                        continuar=False

                    else:
                        print("Seleccione una opción valida .")
                        time.sleep(0.6)
                        cl()
                        print("Seleccione una opción valida ..")
                        time.sleep(0.6)
                        cl()
                        print("Seleccione una opción valida ...")
                        time.sleep(0.6)
                        cl()
                        continue        

            elif valor==2:
                continuar = True
                while continuar:
                    print(' ')
                    print('********************************** ')
                    print('*                                * ')
                    print('*            PARTIDOS            * ')
                    print('*                                * ')
                    print('********************************** ')
                    print(' ')
                    print('1.- Registrar Partido')
                    print('2.- Unirse a Partido')
                    print('3.- Ver Partidos')
                    print('4.- Buscar Partido ')
                    print('5.- Volver')
                    print(' ')
                    valorP = int(input("-> : "))     
                    cl()       

                    if valorP == 1:                   
                        d=str(input('ingrese dia: '))
                        m=str(input('ingrese mes: '))
                        bloque.listartodo_bloque(1)
                        blo=str(input("Bloque por la id: "))
                        cancha.listartodo_cancha(1)
                        can = str(input("cancha por la id: "))
                        print('ingrese dia y mes que se jugara este partido: ')
                        fech=str("2022"+"-"+m+"-"+d)
                        p=partido(fech,blo,can)
                        p.registrarpartido()

                    elif valorP == 2:
                        usuario.listartodo_user(1)
                        usu = str(input("usuario por la id: "))
                        posicion.listartodo_posicion(1)
                        pos= str(input("posicion por la id: "))
                        partido.listartodo_partido(1)
                        par= str(input("partido por la id: "))
                        p=participacion(usu,pos,par)
                        p.registrarparticipacion()
                    
                    elif valorP == 3:
                        partido.listartodo_partido(1)
                        print(' ')

                    elif valorP == 4:
                        print('1.- buscar por jugador')
                        print('2.- buscar por su id')
                        conpartido=int(input("-> : "))     
                        cl()
                        
                        if conpartido == 1 :
                            busc = int(input('ingrese id del jugador  '))
                            resultado =  partido.listar_partido_jugador(busc)
                            if resultado == None:
                                print ("la id no coincide")
                            
                        elif conpartido == 2 :
                            busc = int(input('ingrese id del partido '))
                            resultado =  partido.listar_partido_partido(busc)
                            if resultado == None:
                                print ("la id no coincide")
                                
                                #select en partidos y listar 
                                #alguna forma de volver al menu principal
                
                    elif valorP == 5:
                            continuar=False
                    
                    input("Presione tecla ENTER para volver")
                    cl()  

            elif valor == 3:
                continuar = True
                while continuar:
                    print(' ')
                    print('********************************** ')
                    print('*                                * ')
                    print('*        Posiciones API          * ')
                    print('*                                * ')
                    print('********************************** ')
                    print(' ')
                    print('1.- Consultar posiciones')
                    print('2.- Registrar posicion')
                    print('3.- Modificar posicion')
                    print('4.- Eliminar posicion')
                    print('5.- Volver')
                    print(' ')
                    valora = int(input("-> : "))     
                    cl()       

                    if valora == 1:
                        consultar=posicion
                        consultar.ver_posicion_api()
                        input("Presione tecla ENTER para volver")
                        cl()   

                    elif valora == 2:
                        nom = input('ingrese el nombre: ')
                        desc = input('ingrese la descripcion: ')
                        print("")
                        agregar=posicion
                        agregar.agregar_posicion_api(nom,desc)
                        print("")
                        input("Presione tecla ENTER para volver")
                        cl()   

                    elif valora == 3:
                        id = input('ingrese la id: ')
                        nom = input('ingrese el nombre: ')
                        desc = input('ingrese la descripcion: ')                        
                        mod= True
                        while mod:
                            resp= (input("Está seguro que desea modificar la posición? (s/n): ")).lower()
                            print(" ")
                            if resp == "s":
                                modificar=posicion
                                modificar.modificar_posicion_api(id,nom,desc)
                                print(" ")
                                input("Presione tecla ENTER para volver")
                                mod= False
                            elif resp == "n":
                                mod = False
                            else:
                                print("por favor seleccione una opcion valida")
                                print(" ")
                                continue
                        cl()

                    elif valora == 4:
                        id = input('ingrese la id: ')
                        elim= True
                        while elim:
                            resp= (input("Está seguro que desea eliminar la posición? (s/n): ")).lower()
                            print(" ")
                            if resp == "s":
                                eliminar=posicion
                                eliminar.eliminar_posicion_api(id)
                                print(" ")
                                input("Presione tecla ENTER para volver")
                                elim= False
                            elif resp == "n":
                                elim = False
                            else:
                                print("por favor seleccione una opcion valida")
                                print(" ")
                                continue
                        cl()

                    elif valora == 5:
                        continuar=False

                    else:
                        print("Seleccione una opción valida .")
                        time.sleep(0.6)
                        cl()
                        print("Seleccione una opción valida ..")
                        time.sleep(0.6)
                        cl()
                        print("Seleccione una opción valida ...")
                        time.sleep(0.6)
                        cl()
                        continue 

            elif valor==4:
                continuar = True
                while continuar:
                    print(' ')
                    print('********************************** ')
                    print('*                                * ')
                    print('*        CONFIGURACIONES         * ')
                    print('*                                * ')
                    print('********************************** ')
                    print(' ')
                    print('1.- BLOQUES')
                    print('2.- TIPOS DE CANCHA')
                    print('3.- POSCIONES ')
                    print('4.- Volver')
                    print(' ')
                    valorC = int(input("-> : "))     
                    cl()

                    if valorC==1:
                        bloque.listartodo_bloque(1)
                        print(' ')
                        input("Presione tecla ENTER para volver")
                        cl() 
                    elif valorC==2: 
                        tipocancha.listartodo_tipocancha(1)
                        print(' ')
                        input("Presione tecla ENTER para volver")
                        cl() 
                    elif valorC==3: 
                        posicion.listartodo_posicion(1)
                        print(' ')
                        input("Presione tecla ENTER para volver")
                        cl() 
                    elif valorC == 4:
                        continuar=False
                    else:
                        print("Seleccione una opción valida .")
                        time.sleep(0.6)
                        cl()
                        print("Seleccione una opción valida ..")
                        time.sleep(0.6)
                        cl()
                        print("Seleccione una opción valida ...")
                        time.sleep(0.6)
                        cl()
                        continue  
            
            elif valor == 5:
                continuar = True
                while continuar:
                    print(' ')
                    print('********************************** ')
                    print('*                                * ')
                    print('*            ELIMINAR            * ')
                    print('*                                * ')
                    print('********************************** ')
                    print(' ')
                    print('1.- USUARIOS')
                    print('2.- PARTIDOS')
                    print('3.- CANCHAS ')
                    print('4.- Volver')
                    print(' ')
                    valorE = int(input("-> : "))     
                    cl()

                    if valorE==1:
                        id=int(input('ingrese por su id: '))
                        resultado =  usuario.eliminar_user(id,id)
                        if resultado == None:
                            print ("la id no coincide")
                        else:
                            print(' ')
                            input("Presione tecla ENTER para volver")
                            cl()

                    elif valorE==2: 
                        id=int(input('ingrese por su id: '))
                        resultado =  partido.eliminar_partido(id,id)
                        if resultado == None:
                            print ("la id no coincide")
                        else:
                            print(' ')
                            input("Presione tecla ENTER para volver")
                            cl()

                    elif valorE==3: 
                        id=int(input('ingrese por su id: '))
                        resultado =  cancha.eliminar_cancha(id,id)
                        if resultado == None:
                            print ("la id no coincide")
                        else:
                            print(' ')
                            input("Presione tecla ENTER para volver")
                            cl()

                    elif valorE == 4:
                        continuar=False

                    else:
                        print("Seleccione una opción valida .")
                        time.sleep(0.6)
                        cl()
                        print("Seleccione una opción valida ..")
                        time.sleep(0.6)
                        cl()
                        print("Seleccione una opción valida ...")
                        time.sleep(0.6)
                        cl()
                        continue  
                           
            else:
                print("Seleccione una opción valida .")
                time.sleep(0.6)
                cl()
                print("Seleccione una opción valida ..")
                time.sleep(0.6)
                cl()
                print("Seleccione una opción valida ...")
                time.sleep(0.6)
                cl()
                continue

Menu.__init__()