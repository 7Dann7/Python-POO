from abc import ABC, abstractmethod
import math

class Empleado(ABC):
    @abstractmethod
    def calcular_salario(self):
        pass

class EmpleadoTiempoCompleto(Empleado):
   
    def __init__(self, hora):
        self.hora = hora

    def calcular_salario(self):
        return self.hora * 50000
    

class EmpleadoPorHoras(Empleado):
   
    def __init__(self, hora):
        self.hora = hora

    def calcular_salario(self):
        return self.hora * 20000
    




empleadoTiempoCompleto=EmpleadoTiempoCompleto(24)
print(f"si un empleado trabajo 50000 pesos por hora por 24 horas su salario es de : {empleadoTiempoCompleto.calcular_salario()}")


empleadoPorHoras = EmpleadoPorHoras(3)
print(f"si un empleado trabajo 20000 pesos por 5 su salario es de :  {empleadoPorHoras.calcular_salario()}")
    

