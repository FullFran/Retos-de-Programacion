"""
/*
 * Escribe un programa que se encargue de comprobar si un número es o no primo.
 * Hecho esto, imprime los números primos entre 1 y 100.
"""


function EsPrimo(num)
    # con isqrt obtenemos el entero más cercano a la raiz cuadrada.
    for i in 2:isqrt(num)
        if num % i == 0
            return false
        end
    end
    return true
end

num = 67

println(EsPrimo(num))

# Se puede tipar el tipo de elementos de arreglo
primos = Int[]
for i in 1:100
    if EsPrimo(i)
        push!(primos,i)
    end
end

print(primos)