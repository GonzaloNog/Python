'''
Desafio numeros

La cantidad de partidos que debemos considerar a un equipo
para el ejemplo se detalla a continuacion
partidos_ganados 8
partidos_empatados 7
partidos_perdidos 5
'''

partidos_totales = 20
error = False
ganados = int(input("Ingrese partidos ganados"))
empatados = int(input("Ingrese partidos empatados"))
perdidos = int(input("Ingrese partidos perdidos"))

if((ganados + empatados + perdidos) == partidos_totales):
    promedio = (3*ganados + empatados)/partidos_totales
    print("Promedio de puntos: ",promedio)
else:
    print("Los partidos ingresados tienen que ser 20")


