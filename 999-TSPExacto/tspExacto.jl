"""
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
"""

# Importamos las dependencias que vamos a utilizar
using CSV
using DataFrames
using IterTools

# Leemos los datos
df = CSV.File("tspData.csv", header=false) |> DataFrame

# Almacenamos los nodos en un array




