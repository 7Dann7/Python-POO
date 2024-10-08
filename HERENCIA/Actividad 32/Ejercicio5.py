class Reloj:
    #constructor
    def __init__(self, marca,tipo_reloj,material):
        self.marca = marca
        self.tipo_reloj = tipo_reloj
        self.material = material
        self.precio_reloj = str(input("Ingrese el precio del reloj: "))

    #metodo publico
    def registrar(self):
        print("---------------------------")
        print("RELOJ REGISTRADO")
        print("---------------------------")
        print("Marca: ", self.marca)
        print("Material: ", self.material)
       
       


class Reloj_inteligente(Reloj):

    def __init__(self,marca,tipo_reloj,material,tipo_pantalla):
        super().__init__(marca,tipo_reloj,material)
        self.tipo_pantalla = tipo_pantalla
        self.sistema_operativo = (input("Ingrese el sistema operativo del reloj : "))
        self.bateria = int(input("Ingrese la bateria actual del reloj: "))
        
        

    def encender(self):
        print(":Tipo de la pantalla ", self.tipo_pantalla)
        print("Sistema operativo del reloj:", self.sistema_operativo)
        

        if self.bateria > 0:
            print("------------------")
            print(f" El reloj de marca{self.marca}, y de material[{self.material} de tipo de pantalla{self.tipo_pantalla} y con sistema operativo {self.sistema_operativo} se puede encender!.")
        else:
            print("------------------")
            print(f" El reloj de marca{self.marca}, y de material[{self.material} y de tipo de pantalla{self.tipo_pantalla} y con sistema operativo {self.sistema_operativo} no se puede encender!.")
            
#instanciando
objeto_reloj_inteligente = Reloj_inteligente('Samsung','Acero inoxidable','cristal', 'WearOS')
objeto_reloj_inteligente.registrar()
objeto_reloj_inteligente.encender()



