class Animales:

    def __init__(self, nombre, habitat, alimento,):
        self.nombre = nombre
        self.habitat = habitat
        self.alimento = alimento


class Perro(Animales):
   def __init__(self, nombre, habitat, alimento, edad):
        super().__init__(nombre, habitat, alimento,)
        self.edad = edad
        self.nombre = nombre
        self.habitat = habitat
        self.alimento = alimento

   
   def sonido(self):
        print("------Perro-------")
        print(f"nombre: {self.nombre}")
        print(f"Placa: {self.placa}")
        print(f"Color:{self.color}")

   def sonido(animall):
    animall.sonido()


objeto_animal = Perro("toby", "casa", "galletas", 2)

sonido(objeto_animal)
