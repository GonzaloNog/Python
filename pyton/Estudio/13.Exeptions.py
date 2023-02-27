### Exception Handling ###

number_one, number_two = 5,1

number_two = '1'


#try except
try:
    print('hola')
    print(number_one + number_two)
    print('No se a producido un error')
except:
    print('Se ha producido un error')

#try except else
try:
    print(number_one + number_two)
    print('No se a producido un error')
except:
    print('Se ha producido un error')
else:#solo se ejecuta si entre try y exect no se a producido un error 
    print("La ejecucion continua correctamente")

#try except
try:
    print('hola')
    print(number_one + number_two)
    print('No se a producido un error')
except:
    print('Se ha producido un error')

#try except else finally
try:
    print(number_one + number_two)
    print('No se a producido un error')
except:
    print('Se ha producido un error')
else: #optional
    print("La ejecucion continua correctamente")
finally: #optional
    # Se ejecuta siempre
    print('La ejecucion continua')

#Exceptiones por tipo

try:
    print(number_one + number_two)
    print('No se a producido un error')
except TypeError:
    print('Se ha producido un error de typo')
except ValueError:
    print('Se ha producido un error de Valor')

# Captura de la informacion de la excepcion

try:
    print(number_one + number_two)
    print('No se a producido un error')
except TypeError as error:
    print(error)
except Exception as error:
    print(error)

