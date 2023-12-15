//Escribe una función que reciba dos palabras (String) y retorne
 //verdadero o falso (Bool) según sean o no anagramas.
 //- Un Anagrama consiste en formar una palabra reordenando TODAS
   //las letras de otra palabra inicial.
 //- NO hace falta comprobar que ambas palabras existan.
 //- Dos palabras exactamente iguales no son anagrama.

#include <iostream>

using namespace std;

//Declaramos la función a emplear en el ejercicio:

bool funcion(string palabra1, string palabra2){

    if(palabra1 == palabra2){
        cout << "Las palabras son iguales\n";
        exit(0);
    }

    bool son_anagramas = false;

    for(int i = 0; i < palabra1.length(); i++){

        for (int j = 0; j < palabra2.length(); j++) {

            if (palabra1[i] == palabra2[j]) {

                palabra2.erase(j);

                break;

            }
            
        }

    }

    if(palabra2 == "") son_anagramas = true;

    return son_anagramas;

}

int main(){

    string x = "asfalto", y = "asflato";

    cout << funcion(x,y) << endl;

}
