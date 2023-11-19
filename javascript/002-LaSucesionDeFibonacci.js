/*
 * Escribe un programa que imprima los 50 primeros números de la sucesión
 * de Fibonacci empezando en 0.
 * - La serie Fibonacci se compone por una sucesión de números en
 *   la que el siguiente siempre es la suma de los dos anteriores.
 *   0, 1, 1, 2, 3, 5, 8, 13...
 */

function Fibonacci(n) {
    const fibo = [0, 1]; // inicializamos con los dos primeros términos

    for (let i = 2; i < n; i++) {     // comenzamos desde el tercero, en js empieza en 0 y acaba en n-1
        // Se puede acabar en n cambiando la condición a i <= n
        // se añade elemento a la lista al final, la suma de los dos anteriores.
        fibo.push(fibo[i-1] + fibo[i-2]);
    }
    return fibo;
}

console.log(Fibonacci(50));
console.log(Fibonacci(50).length);

