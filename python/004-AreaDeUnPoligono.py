'''
/*
 * Crea una única función (importante que sólo sea una) que sea capaz
 * de calcular y retornar el área de un polígono.
 * - La función recibirá por parámetro sólo UN polígono a la vez.
 * - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
 * - Imprime el cálculo del área de un polígono de cada tipo.
 */
'''

class Poligono:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    

# Herencia:
class Triangulo(Poligono):
    def __init__(self, base, altura):
        super().__init__(base, altura)
    def printArea(self):
        print('El área del Triángulo es: ', self.base * self.altura / 2)


class Cuadrado(Poligono):
    def __init__(self, lado):
        super().__init__(lado, lado)
        # como lo hemos tomado de la clase polígono, ahora lado y lado son base y altura.
    
    def printArea(self): 
        print('El área del Cuadrado es:', self.base ** 2)


class Rectangulo(Poligono):
    def __init__(self, base, altura):
        super().__init__(base, altura)
    def printArea(self):
        print('El área del Rectángulo es: ', self.base * self.altura)


# Al poner que poligono es una variable de tipo Poligono, la variable poligono
# tiene que ser de tipo Poligono.
def printArea(poligono: Poligono):
    poligono.printArea()


# Polimorfismo:
# La variable poligono puede ser de tipo Triangulo, Cuadrado o Rectangulo.
# y nos va a retornar el área de ese poligono, distinta para cada uno de ellos.
printArea(Triangulo(10, 5))
printArea(Cuadrado(10))
printArea(Rectangulo(10, 5))