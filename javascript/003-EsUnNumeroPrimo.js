/*
 * Escribe un programa que se encargue de comprobar si un número es o no primo.
 * Hecho esto, imprime los números primos entre 1 y 100.
 */

function EsPrimo(num) {
    for (let i = 2; i < Math.sqrt(num); i++) {
        if (num % i === 0) {
            return false;
        }
    }
    return true;
}
    
num = 5

console.log(num, 'Es primo: ' + EsPrimo(num))

primos = []

for (let i = 1; i <= 100; i++) {
    if (EsPrimo(i)) {
        primos.push(i)
    }
}

console.log(primos)