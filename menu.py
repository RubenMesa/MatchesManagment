from Usuario import usuario
from Cancha import cancha 
from Bloque import bloque 
from TipoCancha import tipocancha 
from Partidos import partido
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
            print('3.- Configuracion ')
            print('4.- Salir ')
            print(' ')
            print('********************************** ')
            print('*                                * ')
            print('* Escribe el numero de la opción * ')
            print('*                                * ')
            print('********************************** ')
            
            
            valor = int(input("-> : "))
            cl = lambda: os.system("cls")
            cl()
            if valor == 4:
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

                    elif valorj == 2:
                        pass

                    elif valorj == 3:
                        usuario.listartodo_user(1)


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
                        time.sleep(2)
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
                        
                        
                        
                        
                        
                    

                        

            # # elif valor==2:
            # #     print('--Partidos--')
            # #     print('1.- Registrar Partido')
            # #     print('2.- Unirse a Partido')
            # #     print('3.- Buscar Partido ')
            # #     valorP = int(input("...\n"))

            # #     if valorP == 1:
            # #         can = str(input("cancha en la que se jugara"))
            # #         date = str(input("que dia desea jugar")) #listarlos
            # #         print ('Bloque 101	00:00 - 01:00//Bloque 102	00:00 - 01:00')
            # #         print ('Bloque 103	00:00 - 01:00//Bloque 104	00:00 - 01:00')
            # #         print ('Bloque 105	00:00 - 01:00//Bloque 106	00:00 - 01:00')
            # #         print ('Bloque 107	00:00 - 01:00//Bloque 108	00:00 - 01:00')
            # #         print ('Bloque 109	00:00 - 01:00//Bloque 110	00:00 - 01:00')
            # #         print ('Bloque 111	00:00 - 01:00//Bloque 112   00:00 - 01:00')
            # #         print ('Bloque 113	00:00 - 01:00//Bloque 114	00:00 - 01:00')
            # #         print ('Bloque 115	00:00 - 01:00//Bloque 116	00:00 - 01:00')
            # #         print ('Bloque 117  00:00 - 01:00//Bloque 118	00:00 - 01:00')
            # #         print ('Bloque 119	00:00 - 01:00//Bloque 120	00:00 - 01:00')
            # #         print ('Bloque 121	00:00 - 01:00//Bloque 122	00:00 - 01:00')
            # #         print ('Bloque 123	00:00 - 01:00//Bloque 124	00:00 - 01:00')
            # #         print ('escoja un horario en que se realizara el partido')
            # #         bloque  = int(input("bloque:"))
            # #         #verificar la cancha en la BD 
            # #         # y que exista un partido con ese horario 
            # #         if todo bien :
            # #             print ("partido creado con exito")
            # #         else: 
            # #             print ("la cancha se encuentra en uso en ese horario ")
            # #             #nose como devolverlos a algun menu 
                    
            # #         #contructor de partido con la Fk de bloque y Cancha 
            # #         funcion de la clase partidos (self,can,bloque)

            # #     elif valorP == 2:
            # #         usuario=input(str('ingrese usuario'))
            # #         #consulta para buscar si el usuario coincide con alguno de la BD
            # #         passw=input(str('usuario encontrado, ingrese su contraseña'))
            # #         #guardar el id del player 
            # #         #listar partidos no terminados 
            # #         agrega=input(str('ingrese el partido por su ID, para sumarse'))
            # #         print('"PO" para portero')
            # #         print('"DEF" para defensa')
            # #         print('"MD" para mediocampista')
            # #         print('"DL" para delanterto ')
            # #         pos= input(str('ingrese su poscion'))
            # #         #en la tabla intermedia que se llamaria "PARTICIPACIONES" se agregan 
            # #         #las llaves de pos , id , la id de la cancha 
            # #         print('ya estas en la nomina')
                    
            # #     elif valorP== 3 :
            # #         print('1.- buscar por fecha')
            # #         print('2.- buscar por jugador')
            # #         conpartido=input(int('3.- buscar por cancha'))
            # #         if conpartido == 1 :
            # #             busc = input(str('ingrese fecha'))
            # #             #select en partidos y listar 
            # #         elif conpartido == 2 :
            # #             busc = input(str('ingrese nombre de jugador '))
            # #             #bucar en participaciones y con la ids del partido
            # #             # #select en partidos y listar 
            # #         elif conpartido == 3 :
            # #             busc = input(str('ingrese fecha'))
            # #             #select en partidos y listar
            # #         else:
            # #             print('nose encontro nada ')    
            # #         #quiza listar y que seleccionen uno , y mostrar todos lo jugadores

            # #          #alguna forma de volver al menu principal
            # # elif valor==2:
            # #     #loggear
            # #     #la idea que aqui el jugador comun no entre y es la forma de modificar 
            # #     #las tablas 'primarias'
            # #     print('--Configuraciones--')
            # #     print('1.- POSCIONES')
            # #     print('2.- TIPOS DE CANCHA')
            # #     print('3.- POSCIONES ')
            # #     print('4.- BLOQUES')
            # #     valorC = int(input("...\n"))
            # #     if valorC==1:
            # #         #listar las pos y preguntar valor a modificar misma manera que 
            # #         #modificamos los jugadores
            # #     elif valorC==2: 
            # #     elif valorC==3: 
            # #     elif valorC==4: 
                    
            

                                
                


                








            


Menu.__init__()



