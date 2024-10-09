class Libro:

    def __init__(self,titulo,autor,isbn,editorial):
        self.__titulo=titulo
        self.__autor=autor
        self.__isbn=isbn
        self.editorial=editorial
        


    def obtener_titulo(self):
        return self.__titulo

    def obtener_autor(self):
        return self.__autor

    def obtener_isbn(self):
        return self.__isbn

    def establecer_titulo(self,nuevo_titulo):
        self.__titulo=nuevo_titulo

    def establecer_autor(self,nuevo_autor):
        self.__autor=nuevo_autor

    



    def mostrar_detalles(self):
        print(f"\nTitulo {self.__titulo}")
        print(f"\nAutor{self.__autor}")
        print(f"\nIsbn {self.__isbn}")
        print(f"\nEditorial {self.editorial}")

libros=Libro("El_elefante","jose","7070700707","arbusto")

libros.mostrar_detalles()

print("--------------------------")

libros.establecer_titulo("El leopardo")
print(f"Titulo: {libros.obtener_titulo() }")
libros.establecer_autor("sebastian")
print(f"Autor: {libros.obtener_autor() }")
print(f"Isbn: {libros.obtener_isbn()}")
print(f"Editorial: {libros.editorial}")


