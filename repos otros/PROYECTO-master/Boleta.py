class boleta :
    
    def __init__(self,codigo,nombre_emp,precio,fecha_emision,impuesto):
        self.codigo=codigo
        self.nombre_emp=nombre_emp
        self.precio=precio
        self.fechae_mision=fecha_emision
        self.impuesto=impuesto
        self.compras=[]
    def agregar(self):
        self.compras.append(b)
        self.compras.append(b2)
        
    def valor_compra(self):
        contador=0
        for i in self.compras:
            contador+=i.precio
        return print(contador)    

b=boleta(1,"numero",1000,"12/05/1995",10)
b2=boleta(2,"number",2000,"fecha",20)
b.agregar()
b.valor_compra()