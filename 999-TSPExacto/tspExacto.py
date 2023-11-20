'''
Problema del Viajante de Comercio (TSP)

Se tiene un conjunto de 10 ciudades, identificadas 
por las letras A, B, C, D, E, F, G, H, I y J. 
Cada ciudad está representada por sus coordenadas (x, y) 
en un plano bidimensional. 

El objetivo es encontrar la ruta más corta que visite cada ciudad 
exactamente una vez y regrese al punto de partida.

Las coordenadas de cada ciudad están proporcionadas en un archivo CSV 
llamado tspData.csv, siguiendo el formato estándar de notación para 
coordenadas. Cada línea del archivo representa una ciudad y tiene el siguiente formato:

nombre,x,y

nombre es el identificador de la ciudad (por ejemplo, A, B, C).
x y y son las coordenadas en el plano bidimensional.
El archivo ciudades.csv contiene la información de las 11 ciudades.

Se busca encontrar la secuencia de ciudades que minimice la distancia total recorrida, 
considerando todas las conexiones posibles entre ciudades. 
La solución debe presentarse indicando la secuencia de ciudades visitadas 
y la distancia total del recorrido.

Añade también el tiempo de ejecución a la salida.
'''


import pandas as pd
import numpy as np

from itertools import permutations
from time import time
# Leemos los datos
df = pd.read_csv('tspData.csv', header=None)
# Almacenamos los nodos en un array para hacer 
# Cálculos de forma más eficiente
nodes = df.to_numpy()

# Definimos la distancia entre 2 nodos
def dist(xi, xj):
    return np.linalg.norm(xi[1:] - xj[1:])

# Definimos la distancia total para un camino
def H(x):
    d=0
    for i, elem in enumerate(x):
        try:
            d += dist(elem, x[i+1])
        except:
            d += dist(elem, x[0])
    return d


# Función para resolver de forma exacta
def TSP(x):
    # Eliminamos el primer elemento
    perm = x[1:]
    caminos = list(permutations(perm))
    optimo = None
    dist_optima = float('inf')
    for i, c in enumerate(caminos):
        c = np.vstack([x[0], c, x[0]])
        d = H(c)
        if d < dist_optima:
            optimo = c

            dist_optima = d
    return optimo[:,0], dist_optima

inicio = time()

camino, distancia = TSP(nodes[:-1])

tEjecucion = time() - inicio

print(f'Camino: {camino} \n Distancia: {distancia}\n Tiempo de ejecución: {tEjecucion:.6f}s')