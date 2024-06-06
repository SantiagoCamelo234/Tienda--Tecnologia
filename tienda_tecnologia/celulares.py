from tienda_tecnologia.producto import Producto
celulares = []
class Celular(Producto):
    def __init__(self, marca, precio,carga, ram, tamaño, lista = celulares ):
        super().__init__(marca, precio)
        self.carga = carga
        self.ram = ram
        self.tamaño = tamaño
        datos = super().Lista(lista)
        computadores_datos = {
                'CARGA': '5000mA',
                'RAM': self.ram,
                'Tamaño': self.tamaño }
        datos.update(computadores_datos)
        lista.append(datos)    
    def listar_celulares(self, lista = celulares):
        celulares = super().lista(lista)
        print(celulares)
def lista():
    return celulares
""" x = Celular('Xiaomi', 200, 'SnapDragon', 8, 5.9)
print(celulares) """