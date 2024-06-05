# IMPIORTACION DE CLASES POR MEDIO DE MODULOS #
from tienda_tecnologia.celulares import Celular
from tienda_tecnologia.computadores import Computadores
from tienda_tecnologia.videojuegos import Videojuegos

print('---- Bienvenido a nuestra tienda ----')
while True:
    print('')
    print('---- MENU DE OPCIONES ----')
    print('AGREGAR UN PRODUCTO [1]')
    print('LISTAR POR TIPO DE PRODUCTO [2]')
    print('EXPORTAR PRODUCTOS[3]')
    print('SALIR [0]')
    opcion = int(input('DIGITE OPCION: '))
    if opcion == 1:
        print('--- PRODUCTOS DISPONIBLES ---')
        print('CELULARES [1]')
        print('COMPUTADORES [2]')
        print('VIDEOJUEGOS [3]')
        op = int(input('Seleccione el producto que desea agregar: ').strip())
        if op == 1:
            marca = input('Ingrese Marca del Producto: ').strip().capitalize()
            precio = int(input('Ingrese precio del producto: ').strip())
            carga = input('Ingrese Bateria del producto: ').strip().capitalize()
            ram = int(input('Ingrese ram del producto: ').strip().capitalize())
            tamaño = float(input('Ingrese tamaño del producto').strip())
            celular = Celular(marca, precio, carga, ram, tamaño)
            celular.listar_celulares()