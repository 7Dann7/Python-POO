class Carro:
    def __init__(self,color,placa,año,) :
        self.color = color
        self.placa = placa
        self.año = año
        
    def mostrar_detalles(self):
        print("Informacion del Carro")
        print("Color: " +self.color)
        print("placa: " +self.placa)
        print("Año: " +self.año)
       



#creamos los objetos a partir de instanciar la clase celular
objeto1=Carro("Azul","3b2-54","2011",)
objeto2=Carro("Negro","34-567","2018")
objeto3=Carro("Gris","37-214","2022")


objeto1.mostrar_detalles()

print("------------------")
objeto2.mostrar_detalles()
print("------------------")
objeto3.mostrar_detalles()

