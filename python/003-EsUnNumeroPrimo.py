'''
/*
 * Escribe un programa que se encargue de comprobar si un número es o no primo.
 * Hecho esto, imprime los números primos entre 1 y 100.
 */
'''
import math
def EsPrimo(num):
    for i in range(2,int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True

num = input("Introduce un número: ")
# Se pueden poner condicionales dentro de los prints!!!
print("Es primo" if EsPrimo(int(num)) else "No es primo")

primos = []
for i in range(1,101):
    if EsPrimo(i):
        primos.append(i)

print(primos)