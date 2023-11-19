 # * Escribe una función que reciba dos palabras (String) y retorne
 # * verdadero o falso (Bool) según sean o no anagramas.
 # * - Un Anagrama consiste en formar una palabra reordenando TODAS
 # *   las letras de otra palabra inicial.
 # * - NO hace falta comprobar que ambas palabras existan.
 # * - Dos palabras exactamente iguales no son anagrama.



def EsAnagrama(palabra1,palabra2):
    return sorted(palabra1.casefold()) == sorted(palabra2.casefold())



p1 = input('Palabra1: ')
p2 = input('Palabra2: ')

print(f'Es un anagrama: {EsAnagrama(p1, p2)}') 
