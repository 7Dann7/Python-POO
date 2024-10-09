from abc import ABC, abstractmethod
import math

class TareaEmpleado(ABC):
    @abstractmethod
    def calcular_salario(self):
        pass

class Ingeniero(TareaEmpleado):
   
    def __init__(self, hora):
        self.hora = hora

    def realizar_tarea(self):
        return self.hora * 50000
    

class Doctor(TareaEmpleado):
   
    def __init__(self, hora):
        self.hora = hora

    def  realizar_tarea(self):
        return self.hora * 20000
    




EmpleadoTiempoCompleto(24)
print(f"su tarea esta en una empresa : {empleadoTiempoCompleto.calcular_salario()}")


empleadoPorHoras = EmpleadoPorHoras(3)
print(f"su tarea esta en la clinica :  {empleadoPorHoras.calcular_salario()}")
    

