class Animal:
    def __init__(self,nombre,habitat,alimento,) :
        self.nombre= nombre
        self.habitat = habitat
        self.alimento = alimento
        
    def mostrar_detalles(self):
        print("Informacion del Animal")
        print("Nombre: " +self.nombre)
        print("Habitat: " +self.habitat)
        print("Alimento: " +self.alimento)
       



#creamos los objetos a partir de instanciar la clase celular
objeto1=Animal("Elefante","Selva","Hierba",)
objeto2=Animal("Leon","Selva","Carne")
objeto3=Animal("Delfin","Mar","Peces")


objeto1.mostrar_detalles()

print("------------------")
objeto2.mostrar_detalles()
print("------------------")
objeto3.mostrar_detalles()

