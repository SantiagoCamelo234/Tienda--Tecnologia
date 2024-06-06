# IMPIORTACION DE CLASES POR MEDIO DE MODULOS #
from tienda_tecnologia.celulares import Celular
from tienda_tecnologia.computadores import Computadores
from tienda_tecnologia.videojuegos import Videojuegos
from tienda_tecnologia.videojuegos import lista as lista_videojuegos
from tienda_tecnologia.computadores import lista as lista_computadores
from tienda_tecnologia.celulares import lista as lista_celulares

# ESTABLECEMOS LA RUTA DEL ARCHIVO
ruta = 'C:/Users/ilvar/Desktop/Tecnologia/productos.txt'
print('---- Bienvenido a nuestra tienda ----')
while True:
    print('')
    print('---- MENU DE OPCIONES ----')
    print('[1] AGREGAR UN PRODUCTO ')
    print('[2] LISTAR POR TIPO DE PRODUCTO ')
    print('[3] EXPORTAR PRODUCTOS')
    print('SALIR [0]')
    opcion = int(input('DIGITE OPCION: '))
    if opcion == 1:
        print('--- PRODUCTOS DISPONIBLES ---')
        print('[1] CELULARES ')
        print('[2] COMPUTADORES ')
        print('[3] VIDEOJUEGOS ')
        op = int(input('Seleccione el producto que desea agregar: ').strip())
        if op == 1:
            print('----- Creando nuevo celular -----')
            marca = input('Ingrese Marca del Producto: ').strip().capitalize()
            precio = int(input('Ingrese precio del producto: ').strip())
            carga = input('Ingrese Bateria del producto: ').strip().capitalize()
            ram = int(input('Ingrese ram del producto: ').strip().capitalize())
            tamaño = float(input('Ingrese tamaño del producto').strip())
            celular = Celular(marca, precio, carga, ram, tamaño)
            
        elif op == 2:
            print('----- Creando nuevo computador -----')
            marca = input('Ingrese Marca del Producto: ').strip().capitalize()
            precio = int(input('Ingrese precio del producto: ').strip())
            cpu = input('Ingrese CPU del producto: ').strip().capitalize()
            ram = int(input('Ingrese RAM del producto: ').strip().capitalize())
            gpu = input('Ingrese GPU del producto').strip()
            pc = Computadores(marca, precio, cpu, ram, gpu)
            
        elif op == 3:
            print('----- Creando nuevo videojuego -----')
            marca = input('Ingrese Marca del videojuego: ').strip().capitalize()
            precio = int(input('Ingrese precio del videojuego: ').strip())
            nombre = input('Ingrese nombre del videojuego: ').strip().capitalize()
            genero = input('Ingrese genero del videojuego: ').strip().capitalize()
            plataforma = input('Ingrese plataforma del videojuego: ').strip()
            game = Videojuegos(marca, precio, nombre, genero, plataforma)
        else:
            print('Opcion Invalida')
    elif opcion == 2:
        print('----- Listando productos -----')
        print('[1] CELULARES ')
        print('[2] COMPUTADORES ')
        print('[3] VIDEOJUEGOS ')
        op = int(input('QUE PRODUCTOS DESEA LISTAR: ').strip())
        if op == 1:
            lista = lista_celulares()
            for i in lista:
                print(f"{i} \n")
        elif op == 2:
            lista = lista_computadores()
            for i in lista:
                print(f"{i} \n")
        elif op == 3:
            lista = lista_videojuegos()
            for i in lista:
                print(f"{i} \n")
        else:
            print('Opcion no valida')
    elif opcion == 3:
        lista_total = lista_celulares() + lista_computadores() + lista_videojuegos()
        with open(ruta, 'a') as archivo:
            for e in lista_total:
                archivo.write(f'{e} \n')
            print('LOS PRODUCTOS HAN SIDO EXPORTADOS')

