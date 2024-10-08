class Instrumento:
    #constructor
    def __init__(self, tipo_instrumento, marca, material_fabricacion):
        self.tipo_instrumento = tipo_instrumento
        self.marca = marca
        self.material_fabricacion = material_fabricacion
        self.precio = int(input("Ingrese el precio del instrumento"))

    #metodo publico
    def registrar(self):
        print("---------------------------")
        print("INSTRUMENTO REGISTRADO")
        print("---------------------------")
        print("Tipo de instrumento: ", self.tipo_instrumento)
        print("Marca: ", self.marca)
        print("material de fabricacion :", self.material_fabricacion)
       


class Guitarra(Instrumento):

    def __init__(self,tipo_instrumento,marca,material_fabricacion,numero_cuerdas):
        super().__init__(tipo_instrumento,marca, material_fabricacion,)
        self.numero_cuerdas = numero_cuerdas
        self.acordes_basicos = input("Ingrese los acordes basicos que conoce: ")
        
        

    def tocar(self):
        print("Numero de cuerdas: ", self.numero_cuerdas)
        print("Acordes basicos:", self.acordes_basicos)
        

        if self.acordes_basicos == "Do":
            print("------------------")
            print(f"el instrumento de tipo {self.tipo_instrumento}, de marca {self.marca} con material de fabricacion {self.material_fabricacion} puede tocar esta cancion!.")
        else:
            print("------------------")
            print(f"el instrumento de tipo {self.tipo_instrumento}, de marca {self.marca} con material de fabricacion {self.material_fabricacion} no puede tocar esta cancion")
            
#instanciando
objeto_guitarra = Guitarra('Cuerda pulsada','Fender','Madera','6')
objeto_guitarra.registrar()
objeto_guitarra.tocar()



