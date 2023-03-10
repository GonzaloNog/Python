'''
Descripción de la actividad. 

Escribir un programa que indique la generación correspondiente para un año de nacimiento indicado. 
Trabajarán con el notebook de clase Clase_4.ipynb

Importante: Para los años que no pertenezcan a ninguna generación, 
se deberá colocar: “No existe generación asociada”
'''


edad = int(input('Que edad tenes?'))

if edad >= 1920 and edad <=1940:
    print('Generacion Silenciosa')
elif edad >= 1946 and edad <= 1964:
    print('Generacion Boomer')
elif edad >= 1965 and edad <= 1979:
    print('Generacion X')
elif edad >= 1980 and edad <= 2000:
    print('Generacion Y')
elif edad >= 2001 and edad <= 2010:
    print('Generacion z')
else:
    print('No existe generación asociada')
