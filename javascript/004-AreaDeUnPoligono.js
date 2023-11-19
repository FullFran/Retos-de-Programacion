
/*
 * Crea una única función (importante que sólo sea una) que sea capaz
 * de calcular y retornar el área de un polígono.
 * - La función recibirá por parámetro sólo UN polígono a la vez.
 * - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
 * - Imprime el cálculo del área de un polígono de cada tipo.
 */

class Poligono {
    constructor(base, altura) {
        this.base = base;
        this.altura = altura;
    }
}


class Triangulo extends Poligono {
    constructor(base, altura) {
        super(base, altura);
    }

    printArea() {
        console.log('El área del triángulo es: ', (this.base * this.altura) / 2);
    }
}


class Cuadrado extends Poligono {
    constructor(lado) {
        super(lado, lado);
    }

    printArea() {
        console.log('El área del cuadrado es: ',  this.base * this.altura);
    }
}


class Rectangulo extends Poligono {
    constructor(base, altura) {
        super(base, altura);
    }

    printArea() {
        console.log('El área del rectángulo es: ', this.base * this.altura);
    }
}


function printArea(poligono) { 
    poligono.printArea();
}


printArea(new Triangulo(10, 5));
printArea(new Cuadrado(10));
printArea(new Rectangulo(10, 5));
