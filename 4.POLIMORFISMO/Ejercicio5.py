class Profesiones:

    def __init__(self, nombre, apellido, ):
        self.nombre = nombre
        self.apellido = apellido
    


class Medico(Profesiones):
     def __init__(self, nombre, apellido, edad):
        super().__init__(nombre, apellido, )
        self.edad = edad
        self.nombre = nombre
        self.apellido = apellido
   

     def trabajar(self):
        print("------MEDICO-------")
        print(f"Nombre: {self.nombre}")
        print(f"Apellido: {self.apellido}")
      

def trabajar(auto):
    auto.trabajar()

    print("-----------------")


class Ingeniero(Profesiones):
     def __init__(self, nombre, apellido, edad):
        super().__init__(nombre, apellido, )
        self.edad = edad
        self.nombre = nombre
        self.apellido = apellido
   

     def trabajar(self):
        print("------Ingeniero-------")
        print(f"Nombre: {self.nombre}")
        print(f"Apellido: {self.apellido}")



    

class Docente(Profesiones):
     def __init__(self, nombre, apellido, edad):
        super().__init__(nombre, apellido, )
        self.edad = edad
        self.nombre = nombre
        self.apellido = apellido
   

     def trabajar(self):
        print("------DOCENTE-------")
        print(f"Nombre: {self.nombre}")
        print(f"Apellido: {self.apellido}")





objeto_medico = Medico("andres", "benitez", 23)
objeto_ingeniero = Ingeniero("carolina", "hernandez", 23)
objeto_docente = Docente ("laila", "narvaez", 33)

trabajar(objeto_medico)
trabajar(objeto_ingeniero)
trabajar(objeto_docente)
