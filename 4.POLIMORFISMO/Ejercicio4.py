class InstrumentosMuicales:

    def __init__(self, nombre, marca, color):
        self.nombre = nombre
        self.marca = marca
        self.color = color


class Guitarra(InstrumentosMuicales):
    def __init__(self, marca, nombre, color, año):
        super().__init__(marca, nombre, color)
        self.año = año
        self.nombre = nombre
        self.marca = marca
        self.color = color


        
    def tocar(self):
        print("------GUITARRA-------")
        print(f"Marca: {self.marca}")
        print(f"Nombre: {self.nombre}")
        print(f"Color:{self.color}")

def tocar(instrumento):
    instrumento.tocar()

    print("-----------------")

class Piano(InstrumentosMuicales):
    def __init__(self, marca, nombre, color, año):
        super().__init__(marca, nombre, color)
        self.año = año
        self.nombre = nombre
        self.marca = marca
        self.color = color


        
    def tocar(self):
        print("------PIANO-------")
        print(f"Marca: {self.marca}")
        print(f"Nombre: {self.nombre}")
        print(f"Color:{self.color}")

def tocar(instrumento):
    instrumento.tocar()






objeto_guitarra = Guitarra("Fender", "dess", "Azul", 2023)
objeto_piano = Piano ("TATT","ABEL", "Verde",2022 )


tocar(objeto_guitarra)
tocar(objeto_piano)