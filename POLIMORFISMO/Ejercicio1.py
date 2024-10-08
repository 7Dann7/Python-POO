class Aprendiz:
    def __init__(self, nombres, apellidos, cedula, sexo):
        self.nombres = nombres
        self.apellidos = apellidos
        self.cedula = cedula
        self.sexo = sexo
        self.formacion = input("Programa de formacion: " )
        self.regional = input("Regional: ")

    def mostrar_info(self):
        print("Hola, soy un aaprendiz SENA")
        print(f"{self.nombres} (f{self.apellidos} )")
        print(f"CC: {self.cedula}")
        print(f"Sexo: {self.sexo}")
        print(f"Estudiante del programa: {self.formacion} de la regional {self.regional}")

class Instructor:
    def __init__(self, nombres, apellidos, cedula, area):
        self.nombres = nombres
        self.apellidos = apellidos
        self.cedula = cedula
        self.area = area

    def mostrar_info(self):
        print("Hola, soy un instructor del SENA")
        print(f"{self.nombres} {self.apellidos}")
        print(f"CC: {self.cedula}")
        print(f"Area de instruccion: {self.area}")


class Coordinador:
    def __init__(self, nombres, apellidos, cedula, departamento):
        self.nombres = nombres
        self.apellidos = apellidos
        self.cedula = cedula
        self.departamento = departamento

    def mostrar_info(self):
        print("Hola, soy el coordinador del SENA")
        print(f"{self.nombres} {self.apellidos}")
        print(f"CC: {self.cedula}")
        print(f"Departamento:  {self.departamento}")

def mostrar_informacion(persona):
    persona.mostrar_info()


objeto_aprendiz = Aprendiz("Samuel Elias", "Vega barrios", 1242424425, "Masculino")
objeto_instructor = Instructor("Laura", "Rodriguez", 89083997383, "programacion")
objeto_coordinador = Coordinador("Carlos", "Martinez", 393279237293, "Recursos Humanos")

mostrar_informacion(objeto_aprendiz)
mostrar_informacion(objeto_instructor)
mostrar_informacion(objeto_coordinador)



       



              

