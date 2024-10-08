class Electrodomestico:
    #constructor
    def __init__(self, marca, color, capacidad):
        self.marca = marca
        self.color = color
        self.capacidad = capacidad
        self.consumo_electrico = int(input("Consumo electrico"))

    #metodo publico
    def registrar(self):
        print("---------------------------")
        print("ELECTRODOMESTICO REGISTRADO")
        print("---------------------------")
        print("Marca: ", self.marca)
        print("Color: ", self.color)
        print("Capacidad ", self.capacidad)
        print("Consumo electrico: ", self.consumo_electrico)


class Refrigerador(Electrodomestico):

    def __init__(self,marca, color, capacidad, tipo_refrigerador):
        super().__init__(marca, color, capacidad)
        self.tipo_refrigerador = tipo_refrigerador
        self.temperatura_inicial = int(input("Temperatura inicial en grados centigrados: "))

    def ajustartemperatura(self):
        print("tipo_refrigerador: ", self.tipo_refrigerador)

        if self.temperatura_inicial > 6:
            print("------------------")
            print(f"El refrigerador {self.marca}, de color {self.color} con capacidad {self.capacidad} tiene una temperatura alta, usted debe bajar la temperatura.")
        else:
            print("------------------")
            print(f"El refrigerador {self.marca}, de color {self.color} con capacidad {self.capacidad} tiene una temperatura esta<ble para congelar.")
            
#instanciando
objeto_refrigerador = Refrigerador ('Mabe','Gris','250','frost')
objeto_refrigerador.registrar()
objeto_refrigerador.ajustartemperatura()



