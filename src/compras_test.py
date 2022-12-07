from compras import *
from parsers import *


def test_dias_estrellas(datos):
    print('EJERCICIO 6')
    print('Los días estrella del supermercado Aldi de la provincia de Huelva son: ', 
    [fecha_to_string(fecha) for fecha in dias_estrella_b(datos, 'Aldi', 'Huelva')]
    )
    print('Los días estrella del supermercado Aldi de la provincia de Huelva son: ', 
    [fecha_to_string(fecha) for fecha in dias_estrella_r(datos, 'Aldi', 'Huelva')]
    )

def test_supermercados_mas_facturacion(datos, n):
    print('Los 2 supermercados con más facturación son: ', supermercado_mas_facturacion(datos, n))

def test_hora_menos_afluencia(datos):
    hora, clientes = hora_menos_afluencia(datos)
    print('La hora con menos afluencia es: ', hora ,' h. con ',clientes, ' llegadas de clientes')

def test_compra_maxima_minima_provincia(datos):
    minimo, maximo = compra_maxima_minima_provincia(datos, 'Huelva')
    print("Importe máximo de la provincia de Huelva:",  maximo, 'Importe mínimo:',  minimo)


def test_lee_compras(datos):
    print('Tres primeros', datos[:3])
    print('Tres últimos', datos[-3:])
    print(len(datos))

if __name__ == '__main__':
    COMPRAS = lee_compras('data/compras.csv')
    print('EJERCICIO 1---------------------------------------------------------------------')
    test_lee_compras(COMPRAS)
    print('EJERCICIO 2---------------------------------------------------------------------')
    test_compra_maxima_minima_provincia(COMPRAS)
    print('EJERCICIO 3---------------------------------------------------------------------')
    test_hora_menos_afluencia(COMPRAS)
    print('EJERCICIO 4---------------------------------------------------------------------')
    test_supermercados_mas_facturacion(COMPRAS, 2)
    test_dias_estrellas(COMPRAS)

