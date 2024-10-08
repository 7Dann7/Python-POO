class Figuras_geomtricas:
    def __init__(self,largo,ancho,aristas) :
        self.largo = largo
        self.ancho = ancho
        self.aristas = aristas
        
    def mostrar_detalles(self):
        print("Informacion de la figura")
        print("Largo: " +self.largo)
        print("Ancho: " +self.ancho)
        print("Aristas: " +self.aristas)
       
       



#creamos los objetos a partir de instanciar la clase celular
objeto1= Figuras_geomtricas("23 cm","10 cm","40")
objeto2= Figuras_geomtricas("30 cm","25 cm","35 ")
objeto3= Figuras_geomtricas("22 cm","40 cm", "0")


objeto1.mostrar_detalles()

print("------------------")
objeto2.mostrar_detalles()
print("------------------")
objeto3.mostrar_detalles()

