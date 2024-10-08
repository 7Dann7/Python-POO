class Celular:
    def __init__(self,modelo,marca,bateria,camara,tamaño) :
        self.modelo =modelo
        self.marca = marca
        self.bateria = bateria
        self.camara = camara
        self.tamaño = tamaño

    def mostrar_detalles(self):
        print("Informacion del celular")
        print("Modelo: " +self.modelo)
        print("Marca: " +self.marca)
        print("Bateria" +self.bateria)
        print("Camara" +self.camara)
        print("Tamaño" +self.tamaño) 
        print("Bateria del celular")

#metodo para encender el celular
    def encender(self):
        self.energia = int(input("Digite el valor de la carga: "))
        if self.energia >0:
            print("El celular "+self.modelo+" se puede encender")
            print(f"¡¡¡¡¡¡¡¡¡ {self.energia} % de carga")
            
            
        else:
            print("El celular "+self.modelo+" no se puede encender")
            

#creamos los objetos a partir de instanciar la clase celular
objeto1=Celular("Iphone 13 pro","Iphone","3095 mAh","12 MP","6.06")
objeto2=Celular("Galaxy A25","Samsung","5000 mAh","13 MP","6.06")


objeto1.mostrar_detalles()
objeto1.encender()
print("------------------")
objeto2.mostrar_detalles()

