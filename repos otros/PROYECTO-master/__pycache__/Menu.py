from Movie import Movie

class Menu:

    def __init__():

        print("Seleccione una opcion ...")
        print("1 para listar las peliculas.. ")
        print("2 para agregar pelicula")
        print("0 para salir del sistema")

        valor = int(input("...\n"))

        if valor == 0:
            print("Adios ...")
        elif valor == 1:
            print("Listando peliculas")
            Movie.list_all()
        elif valor == 2:
            print("Solicitando datos de pelicula ...\n")
            rut = int(input("Ingrese titulo de la pelicula "))
            nombre= input("Ingrese titulo de la pelicula ")
            apellido = input("Ingrese titulo de la pelicula ")
            edad= int(input("Ingrese titulo de la pelicula "))
            direccion = input("Ingrese titulo de la pelicula ")
            correo = input("Ingrese titulo de la pelicula ")
            nuevoU = Movie(rut,nombre,apellido,edad,direccion,correo)
            nuevoU.create()
            print("Usuario guardado exitosamente! \n")
        else:
            print("No se reconoce el comando ... :s")
            Menu.__init()

Menu.__init__()

