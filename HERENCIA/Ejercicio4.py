class Electronico:
    #constructor
    def __init__(self, marca,modelo,tipo_procesador):
        self.marca = marca
        self.modelo = modelo
        self.tipo_procesador = tipo_procesador
        self.cantidad_memoria = str(input("Ingrese la cantidad de memoria Ram en GB: "))

    #metodo publico
    def registrar(self):
        print("---------------------------")
        print("ELECTRONICO REGISTRADO")
        print("---------------------------")
        print("Marca: ", self.marca)
        print("modelo: ", self.modelo)
        print("Tipo de procesador :", self.tipo_procesador)
       


class Laptop(Electronico):

    def __init__(self,marca,modelo,tipo_procesador,tipo_disco_duro):
        super().__init__(marca,modelo,tipo_procesador)
        self.tipo_disco_duro = tipo_disco_duro
        self.duracion_bateria = str(input("Ingrese la duracion de bateria en horas : "))
        self.bateria = int(input("Ingrese la bateria actual del la laptop: "))
        
        

    def encender(self):
        print("Tipo del disco duro: ", self.tipo_disco_duro)
        print("Duracion de la bateria:", self.duracion_bateria)
        

        if self.bateria > 0:
            print("------------------")
            print(f" La laptop de marca{self.marca}, y de modelo{self.modelo} con tipo de procesador {self.tipo_procesador} se puede encender!.")
        else:
            print("------------------")
            print(f" La laptop de marca{self.marca}, y de modelo{self.modelo} con tipo de procesador {self.tipo_procesador} no se puede encender!")
            
#instanciando
objeto_laptop = Laptop('Lenovo','IdeaPad Slim 3i', '8va Gen','Intel')
objeto_laptop.registrar()
objeto_laptop.encender()



