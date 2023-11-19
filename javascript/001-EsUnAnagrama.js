/*
 * Escribe una función que reciba dos palabras (String) y retorne
 * verdadero o falso (Bool) según sean o no anagramas.
 * - Un Anagrama consiste en formar una palabra reordenando TODAS
 *   las letras de otra palabra inicial.
 * - NO hace falta comprobar que ambas palabras existan.
 * - Dos palabras exactamente iguales no son anagrama.
 */

function esAnagrama(palabra1, palabra2) {
    // Aquí lo pasamos a minúsculas, lo separamos por letras, lo ordenamos y volvemos a unirlo para comprobar si tienen las mismas letras
    return palabra1.toLowerCase().split("").sort().join("") === palabra2.toLowerCase().split("").sort().join("");
}


console.log("Es un anagrama: ", esAnagrama("Hola", "laoh"));
