class Usuario :
    
    pieder = False 
    pieizq = False
    #CONSTRUCTOR
    def __init__(self, nombre='', user='', password='',  pieder= False , pieizq= False ) -> None:
        self.nombre = nombre
        self.user = user
        self.password =  password
        self.pieder = pieder
        self.pieizq = pieizq
        self.__conectar = conectar()

    #def registrarUsuario(self):
        sql = f'INSERT INTO Usuario (")'
        mensaje = self.__conectar.ejecutar(sql)
        return mensaje
        


    

