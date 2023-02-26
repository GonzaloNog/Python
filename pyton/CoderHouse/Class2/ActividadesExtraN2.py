#1.Identifica el tipo de dato (int, float, string, list o touple) de los siguientes valores literales.

var1 = 'Hola mundo' #String
var2 = [1,10,100] #Lista
var3 = -25 #int
var4 = (8,100,-12) #tuple
var5 = 1.167 #float
var6 = ['hola', 'mundo'] #lista
var7 ='' #string
var8 = (1,-5,'hola!') #tuple

#2.Determina mentalmente (sin programar) el resultado que aparecerá por pantalla a partir de las siguientes variables:
a = 10
b = -5
c = "hola"
d = [1,2,3]
e = (4,5,6)

print(a*5)#50
print(a - b)#15
print(c + ' Mundo')#Hola mundo
print(c * 2)#holahola
print(c[-1])#a
print(c[1:])#ola
print(d + d)#[1,2,3,1,2,3]
print(e[1])#5
print(e + (7,8,9))#(4,5,6,7,8,9)

#3.El siguiente código pretende realizar una media entre 3 números,
# pero no funciona correctamente. ¿Eres capaz de identificar el problema 
# y solucionarlo?

numero_1 = 9
numero_2 = 3
numero_3 = 6

media = (numero_1 + numero_2 + numero_3)/3

print('La nota media es: ',media)

#4. A partir del ejercicio anterior, desarrolla un programa para calcular 
# la nota final. Para ello vamos a suponer que cada número es una nota 
# y que queremos obtener la nota media. Cada nota tiene un valor 
# porcentual:

#La primera nota vale un 15% del total
#La segunda nota vale un 35% del total
#La tercera nota vale un 50% del total


nota_media = ((numero_1 * 15) + (numero_2 * 35) + (numero_3 * 50))/100
print(nota_media)

# 5.La siguiente matriz (o lista con listas anidadas) debe cumplir una
#  condición: en cada fila el cuarto elemento siempre debe ser el 
# resultado de sumar los tres primeros. ¿Eres capaz de modificar las
#  sumas incorrectas utilizando la técnica del slicing?

matriz = [[1,5,1],[2,1,2],[3,0,1],[1,4,4]]
matriz[0].append(7)
matriz[1].append(5)
matriz[2].append(4)
matriz[3].append(9)
print(matriz)


