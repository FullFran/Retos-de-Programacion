//Escribe un programa que imprima los 50 primeros números de la sucesión
//de Fibonacci empezando en 0.
//- La serie Fibonacci se compone por una sucesión de números en
////la que el siguiente siempre es la suma de los dos anteriores.
//''
//0, 1, 1, 2, 3, 5, 8, 13...

#include <iostream>

using namespace std;

void funcion(){

    long int num_1 = 0;
    long int num_2 = 1;

    printf("%li \n%li \n", num_1, num_2);

    for (int i = 0; i < 49; i++) {

        num_2 = num_1 + num_2;

        num_1 = num_2 - num_1;

        printf("%li\n", num_2);

    }
    
}

int main(){

    funcion();

}
