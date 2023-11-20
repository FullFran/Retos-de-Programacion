 # * Escribe una función que reciba dos palabras (String) y retorne
 # * verdadero o falso (Bool) según sean o no anagramas.
 # * - Un Anagrama consiste en formar una palabra reordenando TODAS
 # *   las letras de otra palabra inicial.
 # * - NO hace falta comprobar que ambas palabras existan.
 # * - Dos palabras exactamente iguales no son anagrama.



# Más eficiente:
function EsAnagrama(palabra1,palabra2)
    return sort(collect(lowercase(palabra1))) == sort(collect(lowercase(palabra2)))
end


p1 = "hola"
p2 = "laoh"

print("Es un anagrama: ", EsAnagrama(p1,p2)) 


