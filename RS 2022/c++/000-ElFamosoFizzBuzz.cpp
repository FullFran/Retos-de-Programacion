//Escribe un programa que muestre por consola (con un print) los
//números de 1 a 100 (ambos incluidos y con un salto de línea entre
//cada impresión), sustituyendo los siguientes:
//- Múltiplos de 3 por la palabra "fizz".
//- Múltiplos de 5 por la palabra "buzz".
//- Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".

#include <iostream>

using namespace std;

int main(){
    
    string x = "fizz", y = "buzz", z;

    for (int i = 1; i < 101; ++i) {

        z = "";
        
        if (i % 3 == 0){

            z = z + x;
            
        }

        if (i % 5 == 0){

            z = z + y;

        }

        if (z != ""){
            cout << z + " ";
            continue;
        }

        cout << i << " ";

    }



}
