class Dispositivo:
    #constructor
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.capacidad_de_bateria = int(input("Capacidad de bateria en mAh"))

    #metodo publico
    def registrar(self):
        print("---------------------------")
        print("DISPOSITIVO REGISTRADO")
        print("---------------------------")
        print("Marca: ", self.marca)
        print("Modelo: ", self.modelo)
        print("Año :", self.año)
       


class Smartphone(Dispositivo):

    def __init__(self,marca, modelo, año, sistema_operativo):
        super().__init__(marca, modelo, año,)
        self.sistema_operativo = sistema_operativo
        self.tipo_conectividad = input("Ingrese el tipo de conectividad: ")
        self.bateria = int(input("Ingrese la el porcentaje de bateria actual del celular"))
        

    def encender(self):
        print("sistema_operativo: ", self.sistema_operativo)
        print("tipo_conectividad:", self.tipo_conectividad)
        

        if self.bateria > 0:
            print("------------------")
            print(f"El smartphone {self.marca}, modelo {self.modelo} de año {self.año} se puede encender!.")
        else:
            print("------------------")
            print(f"El smartphone ){self.marca}, modelo {self.modelo} de año {self.año} no se puede encender!.")
            
#instanciando
objeto_smartphone = Smartphone('Oppo','Reno11','2024','5G')
objeto_smartphone.registrar()
objeto_smartphone.encender()



