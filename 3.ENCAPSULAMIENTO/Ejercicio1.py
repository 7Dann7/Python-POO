class Producto:

    def __init__(self,nombre,precio,cantidad,categoria):
        self.__nombre=nombre
        self.__precio=precio
        self.cantidad=cantidad
        self.categoria=categoria


    def obtener_nombre(self):
        return self.__nombre

    def obtener_precio(self):
        return self.__precio

    def establecer_nombre(self,nuevo_nombre):
        self.__nombre=nuevo_nombre

    def establecer_precio(self,nuevo_precio):
        self.__precio=nuevo_precio


    def mostrar_detalles(self):
        print(f"\nNombres: {self.__nombre}")
        print(f"\nPrecio: {self.__precio}")
        print(f"\nCantidad: {self.cantidad}")
        print(f"\nCategoria: {self.categoria}")

productos=Producto("Suavitel","5000","15","Limpieza")

productos.mostrar_detalles()

print("--------------------------")

productos.establecer_nombre("Fab dersa")
print(f"Nombre: {productos.obtener_nombre() }")
productos.establecer_precio("6000")
print(f"Precio: {productos.obtener_precio()}")
print(f"Cantidad: {productos.cantidad}")
print(f"Categoria: {productos.categoria}")