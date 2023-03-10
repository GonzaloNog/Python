'''
 * Crea una única función (importante que sólo sea una) que sea capaz
 * de calcular y retornar el área de un polígono.
 * - La función recibirá por parámetro sólo UN polígono a la vez.
 * - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
 * - Imprime el cálculo del área de un polígono de cada tipo.
'''


#Sin uso de clases 
def area(poligono: list):
    area = 0
    for index in poligono:
        print(area)
        area =area + index
    if(len(poligono) == 3):
        print('El area del triangulo es: ', area)
    elif len(poligono) == 4 and poligono.count(poligono[0]) == 4:
        print('El area del cuadrado es: ', area)
    elif len(poligono) == 4:
        print('El area del rectanguloes: ', area)
    else:
        print('Se requiere una lista de 3 a 4 numeros para determinar el area')

my_list = [1,1,1,2]
area(my_list)

#Clases 

class Poligon:
    def __init__(self):
        self.area = 0.0
    def area(self):
        pass
    def imprimir_area(self):
        pass

class Triangulo(Poligon):

    def area(self, base: float, altura: float):
        self.area = (base * altura)/2
        #return area
    def imprimir_area(self):
        print('El area del triangulo es ', self.area)

class Cuadrado(Poligon):

    def area(self, base: float):
        self.area = base * base
        #return area
    def imprimir_area(self):
        print('El area del cuadrado es ', self.area)

class Rectangulo(Poligon):

    def area(self, base: float, altura: float):
        self.area = base * altura
        #return area
    def imprimir_area(self):
        print('El area del Rectangulo es ', self.area)

cuadrado = Cuadrado()
triangulo = Triangulo()
rectangulo = Rectangulo()

cuadrado.area(4.0)
triangulo.area(5.0,7.0)
rectangulo.area(8.0,9.0)

my_poligon_list = []

#my_poligon_list.append(cuadrado)
#my_poligon_list.append(triangulo)
#my_poligon_list.append(rectangulo)

print(type(my_poligon_list))

