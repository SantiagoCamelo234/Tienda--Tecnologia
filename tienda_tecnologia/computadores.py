from tienda_tecnologia.producto import Producto
computadores = []
class Computadores(Producto):
    def __init__(self, marca, precio,cpu, ram, gpu, lista = computadores ):
        super().__init__(marca, precio)
        self.cpu = cpu
        self.ram = ram
        self.gpu = gpu
        datos = super().Lista(lista)
        computadores_datos = {
                'CPU': self.cpu,
                'RAM': self.ram,
                'GPU': self.gpu }
        datos.update(computadores_datos)
        lista.append(datos)    
    


""" x = Computadores('Lenovo', 1200, 'Intel', '16GB', 'RTX3050')
print(computadores)
y = Computadores('Lenovo', 1200, 'Intel', '16GB', 'RTX3050')
print(computadores) """
