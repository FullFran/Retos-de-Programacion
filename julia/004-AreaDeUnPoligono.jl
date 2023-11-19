 """
 * Crea una única función (importante que sólo sea una) que sea capaz
 * de calcular y retornar el área de un polígono.
 * - La función recibirá por parámetro sólo UN polígono a la vez.
 * - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
 * - Imprime el cálculo del área de un polígono de cada tipo.
 */
"""

# Define un tipo abstracto
abstract type Poligono end

# Define un subtipo que hereda de poligono
struct Triangulo <: Poligono
    base::Float64
    altura::Float64
end
# Implementa el cálculo del área para el subtipo Triaungulo
area(poligono::Triangulo) = poligono.base * poligono.altura / 2

struct Cuadrado <: Poligono
    lado::Float64
end
# Así se hace el polimorfismo en julia
area(poligono::Cuadrado) = poligono.lado^2

struct Rectangulo <: Poligono
    base::Float64
    altura::Float64
end
area(poligono::Rectangulo) = poligono.base * poligono.altura

rectangulo = Rectangulo(2.0,3.0)
triangulo = Triangulo(2.0,3.0)
cuadrado = Cuadrado(2.0)

println("El área del rectángulo es: ",area(rectangulo))
println("El área del triángulo es: ",area(triangulo))
println("El área del cuadrado es: ",area(cuadrado))

