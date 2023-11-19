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


'''
# Intento corrigiendo:
def EsAnagrama(palabra1,palabra2):
    if len(palabra1) == len(palabra2):
        # sorted devuelve una lista ordenada, en este caso lo hacemos con un string
        # casefold para que no distinga mayúsculas de minúsculas
        return sorted(palabra1.casefold()) == sorted(palabra2.casefold())
    else:
        return False
'''
# Más eficiente:
def EsAnagrama(palabra1,palabra2):
    return sorted(palabra1.casefold()) == sorted(palabra2.casefold())



p1 = input('Palabra1: ')
p2 = input('Palabra2: ')

print(f'Es un anagrama: {EsAnagrama(p1, p2)}') 
