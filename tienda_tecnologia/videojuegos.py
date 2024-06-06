from tienda_tecnologia.producto import Producto
videojuegos = []
class Videojuegos(Producto):
    def __init__(self, marca, precio,nombre, genero, plataforma, lista = videojuegos ):
        super().__init__(marca, precio)
        self.nombre = nombre
        self.genero = genero
        self.plataforma = plataforma
        datos = super().Lista(lista)
        videojuegos_datos = {
                'Nombre': self.nombre,
                'Genero': self.genero,
                'Plataforma': self.plataforma }
        datos.update(videojuegos_datos)
        lista.append(datos)    
    def listar_videojuegos(self, lista = videojuegos):
        videojuegos = super().lista(lista)
        print(videojuegos)
        
def lista():
    return videojuegos
        

""" x = Videojuegos('Insomniac', 120, 'SpiderMan', 'Superheroes', 'PS5')
y = Videojuegos('Bethesda', 150, 'HALO', 'Accion', 'Xbox')


print(videojuegos) """
