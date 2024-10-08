class Vehiculos:

    def __init__(self, marca, placa, color,):
        self.marca = marca
        self.placa = placa
        self.color = color


class Carro(Vehiculos):
    def __init__(self, marca, placa, color, año):
        super().__init__(marca, placa, color)
        self.año = año
        self.marca = marca
        self.placa = placa
        self.color = color

    def descripcion(self):
        print("------CARRO-------")
        print(f"Marca: {self.marca}")
        print(f"Placa: {self.placa}")
        print(f"Color:{self.color}")

def descripcion(auto):
    auto.descripcion()

    print("-----------------")

class Moto(Vehiculos):
    def __init__(self, marca, placa, color, año):
        super().__init__(marca, placa, color)
        self.año = año
        self.marca = marca
        self.placa = placa
        self.color = color
    
    def descripcion(self):
        print("------MOTO-------")
        print(f"Marca: {self.marca}")
        print(f"Placa: {self.placa}")
        print(f"Color:{self.color}")

def descripcion(motoo):
    motoo.descripcion()

    print("-----------------")

class Bicicleta(Vehiculos):
    def __init__(self, marca, placa, color, año):
        super().__init__(marca, placa, color)
        self.año = año
        self.marca = marca
        self.placa = placa
        self.color = color

    def descripcion(self):
        print("------Bicicleta-------")
        print(f"Marca: {self.marca}")
        print(f"Placa: {self.placa}")
        print(f"Color:{self.color}")




objeto_carro = Carro("Ford", "647b6", "Azul", 2023)
objeto_moto = Moto("Suzuki", "733h3", "Verde", 2022)
objeto_bicicleta = Bicicleta ("Suzuki", "733h3", "Verde", 2022)

descripcion(objeto_carro)
descripcion(objeto_moto)
descripcion(objeto_bicicleta)
