class Producto():
    def __init__(self,marca, precio):
        self.marca = marca
        self.precio = precio
    def Lista(self, lista):
        datos = {'MARCA': self.marca,
                'PRECIO': self.precio}
        return datos
    def lista(self, lista):
        return lista
""" p = Producto('Iphone', 2000)
x = Producto('Lenovo', 3000)
p.Lista(productos)
x.Lista(productos)
print(productos) """


