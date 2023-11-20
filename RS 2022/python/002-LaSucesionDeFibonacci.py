''' 
* Escribe un programa que imprima los 50 primeros números de la sucesión
 * de Fibonacci empezando en 0.
 * - La serie Fibonacci se compone por una sucesión de números en
 *   la que el siguiente siempre es la suma de los dos anteriores.
 *   0, 1, 1, 2, 3, 5, 8, 13...
 '''


def Fibonacci(n):
    """
    Generate the Fibonacci sequence up to the n-th term.

    Args:
        n (int): The number of terms to generate in the Fibonacci sequence.

    Returns:
        list: The Fibonacci sequence up to the n-th term.
    """
    fibo = [0, 1]  # Initialize the Fibonacci sequence with the first two terms
    for i in range(n - 2):  # Generate the remaining terms in the sequence
        fibo.append(fibo[i] + fibo[i + 1])
    return fibo

print(Fibonacci(50))
print(len(Fibonacci(50)))