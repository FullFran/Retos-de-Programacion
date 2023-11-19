 # * Escribe una función que reciba dos palabras (String) y retorne
 # * verdadero o falso (Bool) según sean o no anagramas.
 # * - Un Anagrama consiste en formar una palabra reordenando TODAS
 # *   las letras de otra palabra inicial.
 # * - NO hace falta comprobar que ambas palabras existan.
 # * - Dos palabras exactamente iguales no son anagrama.


# Primer intento mío:
# def EsAnagrama(palabra1, palabra2):
    # if palabra1 == palabra2 :
        # return False
    # c = 0
    # if len(palabra1) == len(palabra2):
        # for l in palabra1:
            # if l in palabra2:
                # c+=1
        # if c == len(palabra1):
            # return True
    # else:
        # return False


# Más eficiente:
function EsAnagrama(palabra1,palabra2)
    return sort(collect(lowercase(palabra1))) == sort(collect(lowercase(palabra2)))
end


p1 = "hola"
p2 = "laoh"

print("Es un anagrama: ", EsAnagrama(p1,p2)) 


