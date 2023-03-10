'''
Un curso se ha dividido en dos grupos diferentes: A y B
de acuerdo al nombre y a una preferencia (Marvel o Capcom). 
El grupo A está formado por fans de Marvel con un nombre anterior 
a la M y los fans de Capcom con un nombre posterior a la N y el 
grupo B por el resto. Escribir un programa que pregunte al 
usuario su nombre y preferencia, y muestre por pantalla el grupo 
que le corresponde.
Ej.:
¿Cómo te llamas?  Alan
¿Cuál es tu preferencia (M o C)?  C
Tu grupo es B
Para preguntarle al usuario, recuerda usar input.
'''

nombre = str(input("Ingrese nombre"))   #input
fan = str(input("Ingrese preferencia M o C"))    #input

#Grupo A ------

#Fanatico de marvel

# fan == "Marvel"
# nombre < "M"

if (fan == "Marvel" and nombre < "M") or (fan == "Capcom" and nombre > "N"):

  print("SOS DEL GRUPO A")

else: 

  print("Sos del epico grupo B!!!!!!!!!")