class Motos:
    def __init__(self,color,placa,año) :
        self.color = color
        self.placa = placa
        self.año = año
        
    def mostrar_detalles(self):
        print("Informacion de la moto")
        print("Color: " +self.color)
        print("Placa: " +self.placa)
        print("Año: " +self.año)
       
       



#creamos los objetos a partir de instanciar la clase celular
objeto1= Motos("Blanco","312-4A","2007")
objeto2= Motos("Negro","AFT-H2","2023")
objeto3= Motos("Verde","HWX-YZ","2022")


objeto1.mostrar_detalles()

print("------------------")
objeto2.mostrar_detalles()
print("------------------")
objeto3.mostrar_detalles()

