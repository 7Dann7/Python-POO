class Empleado:
    def __init__(self,nombre,edad,genero,numero_telefono,altura) :
        self.nombre = nombre
        self.edad = edad
        self.genero =genero
        self.numero_telefono = numero_telefono
        self.altura = altura
        
    def mostrar_detalles(self):
        print("Informacion del Empleado")
        print("Edad: " +self.edad)
        print("Genero: " +self.genero)
        print("Numero_telefono: " +self.numero_telefono)
        print("Altura: " +self.altura)
       



#creamos los objetos a partir de instanciar la clase celular
objeto1= Empleado("David","33","Masculino","314 2457321","1.83")
objeto2= Empleado("Estefany","24","Fememino","301 4763210","1.72")
objeto3= Empleado("Fabian","26","Fememino","310 2457321","1.80")


objeto1.mostrar_detalles()

print("------------------")
objeto2.mostrar_detalles()
print("------------------")
objeto3.mostrar_detalles()

