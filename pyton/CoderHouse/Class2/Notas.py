#Listas y array 

int_list = [1,2,3,4]
str_list = ['hola','como','estas','?']

datos = [1,-2,300,'hola','chau',1.0]

pares = [0,2,4,5,8,10]
pares[3] = 6

print(pares)

pares.reverse() #invertir lista

print(pares)

pares[:3] = [100,200,300]

print(pares)

pares[:3] = [1]

print(pares)

print(len(pares))

#append agrega elemento al final de la lista

numeros = [1,2,3,4]
numeros.append(1)

print(numeros)

#pop se elemina el ultimo elemento de la lista o se puede pasar un index

numeros.pop()

print(numeros)

numeros.pop(1)

print(numeros)

#index pasa el indise dodne esta un valor

print(numeros.index(3))


#Tuplas inmodificable
mi_tupla = (1,2,3,4)
otra_tupla = ('hola','chau','adios')

tupla1 = (2,) #tupla de un numero

estaciones = ('invierno', 'primavera','verano','otoño')

#matrix

matrix = [[1,2,3],[4,5,6],[7,8,9]]

print(matrix[0])

gran_tupla = ('casa',30.45, (3,4,5), ['Alemania','Argentina','Brazil'])

gran_tupla[-1].append('colombia')

print(gran_tupla)
