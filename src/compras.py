import csv
from collections import namedtuple, Counter, defaultdict
from parsers import *

Compra = namedtuple('Compra', 'dni,supermercado,provincia,fecha_llegada,fecha_salida,total_compra')

def lee_compras(fichero):
    result = []
    with open(fichero) as f:
        lector = csv.reader(f)
        next(lector)
        for dni,supermercado,provincia,fecha_llegada,fecha_salida,total_compra in lector:
            result.append(Compra(dni,supermercado,provincia,parsea_fecha(fecha_llegada),parsea_fecha(fecha_salida),float(total_compra)))
    return result

def filtra_compras_provincia(compras, provincia):
    return [c for c in compras if c.provincia == provincia]


def compra_maxima_minima_provincia(compras, provincia):
    '''**compra_maxima_minima_provincia**: recibe una lista de tuplas de tipo `Compra` 
    y una provincia. Devuelve una tupla que contiene el importe máximo y el mínimo de
     las compras que se han realizado en la provincia dada como parámetro. 
     Si la provincia toma el valor `None`, se devuelve una tupla con el importe máximo y 
     el mínimo calculados a partir de todas las compras. _(1 punto)'''
    filtrado = compras
    if provincia != None:
        filtrado = filtra_compras_provincia(compras, provincia)

    minimo = min(filtrado, key = lambda x: x.total_compra)
    maximo = max(filtrado, key = lambda x: x.total_compra)

    return (minimo.total_compra, maximo.total_compra)

#los alumnos quieren más complejidad en el examen. Darle una vuelta con horas múltiples.
def hora_menos_afluencia(compras):
    '''**hora_menos_afluencia**: recibe una lista de tuplas de tipo 
    `Compra` y devuelve una tupla con la hora en la que llegan menos clientes y 
    el número de clientes que llegan a dicha hora. _(1,5 puntos)_'''
    horas = [c.fecha_llegada.hour for c in compras]
    contador = Counter(horas)

    return contador.most_common()[-1]

def supermercado_mas_facturacion(compras, n=3):
    '''**supermercados_mas_facturacion**: 
    recibe una lista de tuplas de tipo `Compra` y un número entero n, 
    con valor por defecto 3. Devuelve un ranking, es decir, 
    una lista de tuplas (posición_ranking, (supermercado, facturación)) 
    con las n marcas de supermercados que más facturan, en orden decreciente de facturación.
    El ranking debe empezar por la posición 1. _(1,5 puntos)_'''
    facturaciones_por_supermecado = defaultdict(float)
    for c in compras:
        facturaciones_por_supermecado[c.supermercado] += c.total_compra
    
    rankings = sorted(facturaciones_por_supermecado.items(), key = lambda x: x[1], reverse=True)
    posiciones = [i for i in range(1, n+1)]
    return list(zip(posiciones, rankings))

def clientes_itinerantes(compras, n):
    '''**clientes_itinerantes**: recibe una 
    lista de tuplas de tipo Compra y un entero n, 
    y devuelve una lista de tuplas con el dni del cliente y 
    la lista de provincias donde el cliente ha realizado sus compras, 
    ordenadas alfabéticamente. 
    Solo se devolverán aquellos clientes que hayan comprado en un número de provincias mayor que el parámetro n. _(2 puntos)_'''
    provincias_por_clientes = defaultdict(set)
    for c in compras:
        provincias_por_clientes[c.dni].add(c.provincia)
    
    return [(dni, sorted(conjunto_provincias)) for dni, conjunto_provincias in provincias_por_clientes.items() 
    if len(conjunto_provincias)>n]

def dias_estrella_r(compras, super, provincia):
    '''**dias_estrella**: recibe una lista de tuplas de tipo `Compra`, 
    un supermercado y una provincia, 
    y devuelve una lista ordenada cronológicamente con las 
    "fechas estrella" de ese supermercado en esa provincia. 
    Se consideran "fechas estrella" aquellos días en los que el supermercado 
    factura más que el día anterior y más que el día siguiente. (2 puntos)'''
    facturacion_dia = defaultdict(float)
    for c in compras:
        if c.supermercado == super and c.provincia == provincia:
            facturacion_dia[c.fecha_salida.date()] += c.total_compra
    lista_ordenada = sorted(facturacion_dia.items())
    return [lista_ordenada[i][0] for i in range(1, len(lista_ordenada)-1)
                if lista_ordenada[i-1][1]<lista_ordenada[i][1]>lista_ordenada[i+1][1]]

def dias_estrella_b(compras, super, provincia):
    '''**dias_estrella**: recibe una lista de tuplas de tipo `Compra`, 
    un supermercado y una provincia, 
    y devuelve una lista ordenada cronológicamente con las 
    "fechas estrella" de ese supermercado en esa provincia. 
    Se consideran "fechas estrella" aquellos días en los que el supermercado 
    factura más que el día anterior y más que el día siguiente. (2 puntos)'''
    facturacion_dia = defaultdict(float)
    filtrado = [c for c in filtra_compras_provincia(compras, provincia) if c.supermercado == super]
    for c in filtrado:
        facturacion_dia[c.fecha_salida.date()] += c.total_compra
    lista_ordenada = sorted(facturacion_dia.items())
    auxiliar = list(zip(lista_ordenada, lista_ordenada[1:], lista_ordenada[2:]))
    return [hoy[0] for ayer, hoy, manyana in auxiliar if ayer[1]<hoy[1]>manyana[1]] 