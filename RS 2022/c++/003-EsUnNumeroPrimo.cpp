//
// Escribe un programa que se encargue de comprobar si un número es o no primo.
// Hecho esto, imprime los números primos entre 1 y 100.
//

#include <iostream>

using namespace std;

void funcion(int cantidad_a_imprimir){

    cout << 1 << endl << 2 << endl;

    for (int i = 3; i < cantidad_a_imprimir; ++i) {

        int puntero1 = 2, puntero2 = i-1;

        bool es_primo = true;


        while(puntero1 != puntero2){

            if((i % puntero1 == 0) || (i % puntero2 == 0)){

                es_primo = false;

                break;

            } 

            ++puntero1;
            --puntero2;

        }

        if (es_primo == true) {

            cout << i << endl;
            
        }
        
    }

}

int main(){

    funcion(100);
    
}
